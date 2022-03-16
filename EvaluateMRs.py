#!/usr/bin/env python3

import numpy as np
import pandas as pd

ORIGINAL_MODEL = 'purePursuitUSCity'
METRICS = {
    'TTD': ['Time to destination (Source)', 'Time to destination (FollowUp)'],
    'TTO': ['Balancing (Source)', 'Balancing (FollowUp)'],
}

EPSILON_TTO = .1

THRESHOLD_TTD = .1
THRESHOLD_TTD_MRIP3 = .15
THRESHOLD_TTO = .15

def MRIP1(metric, source, followup, t):
    '''Faster vehicles'''
    return {
        'TTD': lambda: followup <= (source * (1.0 + THRESHOLD_TTD)), # followup <= source
        'TTO': lambda: followup/t >= (source/t * (1.0 - THRESHOLD_TTO)), # followup >= source
    }[metric]()

def MRIP2(metric, source, followup, t):
    '''Additional obstacles'''
    return {
        'TTD': lambda: followup >= (source * (1.0 - THRESHOLD_TTD)), # followup >= source
        'TTO': lambda: followup/t <= source/t * (1.0 + THRESHOLD_TTO) and followup/t >= (source/t * (1.0 - THRESHOLD_TTO)), # followup == source
    }[metric]()

def MRIP3(metric, source, followup, t):
    '''Reversed path'''
    return {
        'TTD': lambda: followup <= (source * (1.0 + THRESHOLD_TTD_MRIP3)) and followup >= (source * (1.0 - THRESHOLD_TTD_MRIP3)), # followup == source
        'TTO': lambda: followup/t <= source/t * (1.0 + THRESHOLD_TTO) and followup/t >= (source/t * (1.0 - THRESHOLD_TTO)), # followup == source
    }[metric]()

def MRIP4(metric, source, followup, t):
    '''Fewer guidance points'''
    return {
        'TTD': lambda: followup <= (source * (1.0 + THRESHOLD_TTD)) and followup >= (source * (1.0 - THRESHOLD_TTD)), # followup == source
        'TTO': lambda: followup/t >= (source/t * (1.0 - THRESHOLD_TTO)), # followup >= source
    }[metric]()

MRIPS = {
    'MRIP1_1': MRIP1,
    'MRIP1_2': MRIP1,
    'MRIP1_3': MRIP1,
    'MRIP2': MRIP2,
    'MRIP3': MRIP3,
    'MRIP4': MRIP4,
}
MRIPS_SORTED = list(MRIPS.keys())
MRIPS_SORTED.sort()

def evaluate_results(results):
    failures = { 
        metric: {}
        for metric in METRICS 
    }
    false_positives = set()
    skipped = set()
    for i in range(len(results)):
        model = results.loc[i, "Model"]
        if model is not np.NaN:
            for metric in METRICS:
                failures[metric].setdefault(model, { mrip: 0 for mrip in MRIPS })
            mrip = results.loc[i, "MRIP"]
            source = str(int(results.loc[i, "Test Case"]))
            followup = f'{source}:{mrip}'
            TTD_s = results.loc[i, METRICS['TTD'][0]]
            TTD_f = results.loc[i, METRICS['TTD'][1]]
            if model == ORIGINAL_MODEL and (TTD_s >= 99999 or TTD_f >= 99999):
                # value >= 99999 means that the car did not arrive to destination, skip test case
                skipped.add(followup)
                continue
            for metric in METRICS:
                t = results.loc[i, METRICS['TTD'][0]]
                value_source = results.loc[i, METRICS[metric][0]]
                value_followup = results.loc[i, METRICS[metric][1]]
                if metric == 'TTO':
                    value_source = max(value_source, EPSILON_TTO)
                    value_followup = max(value_followup, EPSILON_TTO)
                if not MRIPS[mrip](metric, value_source, value_followup, t):
                    if model == ORIGINAL_MODEL:
                        failures[metric][model][mrip] += 1
                        false_positives.add(followup)
                    elif followup not in false_positives:
                        failures[metric][model][mrip] += 1

    return failures, skipped

def main():
    import sys
    if len(sys.argv) != 3:
        print(f'./EvaluateMRs.py <RESULTS_FILE> <OUTPUT_FILE>')
        exit(0)
    results_file = sys.argv[1]
    output_file = sys.argv[2]

    data = None
    if results_file.endswith('.xlsx'):
        data = pd.read_excel(results_file, engine='openpyxl')
    else:
        data = pd.read_csv(results_file)
    
    failures, skipped = evaluate_results(results=data)

    print(f'Skipped: {skipped}')

    failures_pd = { 
        metric: pd.DataFrame({ column: [] for column in ("Mutant", *MRIPS_SORTED) })
        for metric in METRICS 
    }
    for metric in METRICS:
        for model in failures[metric]:
            failures_pd[metric] = failures_pd[metric].append(
                { column: [model, *(failures[metric][model][mrip] for mrip in MRIPS_SORTED)][i] for i, column in enumerate(("Mutant", *MRIPS_SORTED)) },
                ignore_index=True,
            )

    if output_file.endswith('.xlsx'):
        failures_pd['TTO'].to_excel(output_file, sheet_name="FAILURES_TO", index=False, header=True)
        with pd.ExcelWriter(output_file,engine="openpyxl" ,mode='a') as writer: 
            failures_pd['TTD'].to_excel(writer, sheet_name="FAILURES_TD", index=False, header=True)  
    else:
        failures_pd['TTO'].to_csv(output_file.format(sheet_name='FAILURES_TO'), index=False, header=True)
        failures_pd['TTD'].to_csv(output_file.format(sheet_name='FAILURES_TD'), index=False, header=True)

if __name__ == '__main__':
    main()
