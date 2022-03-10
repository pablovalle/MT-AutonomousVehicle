#!/usr/bin/env python3

import numpy as np
import pandas as pd

ORIGINAL_MODEL = 'purePursuitUSCity'
THRESHOLD_KEYS = {
    'TTD': ['Time to destination (Source)', 'Time to destination (FollowUp)'],
    'TTO': ['Balancing (Source)', 'Balancing (FollowUp)'],
}

def evaluate_results(results, thresholds):
    false_positives = set()
    possible_failures = 0
    failures = 0
    mutants_killed = set()
    skipped = set()
    for i in range(len(results)):
        model = results.loc[i, "Model"]
        if model is not np.NaN:
            source = str(int(results.loc[i, "Test Case"]))
            followup = f'{source}:{results.loc[i, "MRIP"]}'
            failure = [False, False]
            for threshold_key in THRESHOLD_KEYS:
                threshold = thresholds[threshold_key]
                for test_num, results_col in enumerate(THRESHOLD_KEYS[threshold_key]):
                    test_id = (source, followup)[test_num]
                    if test_id not in skipped:
                        value = results.loc[i, results_col]
                        if model == ORIGINAL_MODEL and value >= 99999:
                            # value >= 99999 means that the car did not arrive to destination, skip test case
                            skipped.add(test_id)
                            continue
                        if model != ORIGINAL_MODEL:
                            possible_failures += 1
                        if value > threshold:
                            failure[test_num] = True
            if model == ORIGINAL_MODEL:
                if failures:
                    raise Exception('Original system results appeared after mutant results')
                if failure[0]:
                    false_positives.add(source)
                if failure[1]:
                    false_positives.add(followup)
            else:
                if failure[0] and source not in false_positives:
                    failures += 1
                    mutants_killed.add(model)
                if failure[1] and followup not in false_positives:
                    failures += 1
                    mutants_killed.add(model)
    return false_positives, possible_failures, failures, mutants_killed, skipped

def main():
    import sys
    if len(sys.argv) != 3:
        print(f'./Evaluate.py <RESULTS_FILE> <THRESHOLDS_FILE>')
        exit(0)
    results_file = sys.argv[1]
    thresholds_file = sys.argv[2]
    results = None
    if results_file.endswith('.xlsx'):
        results = pd.read_excel(results_file, engine='openpyxl')
    else:
        results = pd.read_csv(results_file)
    thresholds = None
    if thresholds_file.endswith('.xlsx'):
        thresholds = pd.read_excel(thresholds_file, engine='openpyxl')
    else:
        thresholds = pd.read_csv(thresholds_file)
    thresholds = { key: thresholds.loc[0, key] for key in THRESHOLD_KEYS }
    false_positives, possible_failures, failures, mutants_killed, skipped = evaluate_results(results=results, thresholds=thresholds)
    print(f'DetectedFailures={failures}/{possible_failures}')
    print(f'FPsCount={len(false_positives)}')
    print(f'MutantsKilledCount={len(mutants_killed)}')
    print(f'FPs={false_positives}')
    print(f'MutantsKilled={mutants_killed}')
    print(f'Skipped={skipped}')

if __name__ == '__main__':
    main()
