#!/usr/bin/env python3

import numpy as np
import pandas as pd

ORIGINAL_MODEL = 'purePursuitUSCity'
THRESHOLD_KEYS = {
    'TTD': ['Time to destination (Source)', 'Time to destination (FollowUp)'],
    'TTO': ['Balancing (Source)', 'Balancing (FollowUp)'],
}

def compute_thresholds(results, test_distances):
    thresholds = { key: -np.inf for key in THRESHOLD_KEYS }
    skipped = set()
    for i in range(len(results)):
        model = results.loc[i, "Model"]
        if model == ORIGINAL_MODEL:
            source = str(int(results.loc[i, "Test Case"]))
            followup = f'{source}:{results.loc[i, "MRIP"]}'
            distance = test_distances[source]
            for threshold_key in THRESHOLD_KEYS:
                for test_num, results_col in enumerate(THRESHOLD_KEYS[threshold_key]):
                    if results_col in results.columns:
                        test_id = (source, followup)[test_num]
                        if test_id not in skipped:
                            value = results.loc[i, results_col]
                            if value >= 99999:
                                # value >= 99999 means that the car did not arrive to destination, skip test case
                                skipped.add(test_id)
                                continue
                            thresholds[threshold_key] = max(thresholds[threshold_key], value / distance)
    return thresholds, skipped

def main():
    import sys
    if len(sys.argv) != 3:
        print(f'./ComputeThresholds.py <RESULTS_FILE> <TEST_DISTANCES_FILE>')
        exit(0)
    results_file = sys.argv[1]
    test_distances_file = sys.argv[2]
    results = None
    if results_file.endswith('.xlsx'):
        results = pd.read_excel(results_file, engine='openpyxl')
    else:
        results = pd.read_csv(results_file)
    test_distances = None
    if test_distances_file.endswith('.xlsx'):
        test_distances = pd.read_excel(test_distances_file, engine='openpyxl')
    else:
        test_distances = pd.read_csv(test_distances_file)
    test_distances = { 
        str(test_distances.loc[i, "testcase"]): test_distances.loc[i, "distance"] 
        for i in range(len(test_distances))
    }
    thresholds, skipped = compute_thresholds(results=results, test_distances=test_distances)
    threshold_keys = list(THRESHOLD_KEYS.keys())
    print(','.join(threshold_keys))
    print(','.join((str(thresholds[key]) for key in threshold_keys)))
    print(f'Skipped={skipped}')

if __name__ == '__main__':
    main()

