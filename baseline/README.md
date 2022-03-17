# Baseline oracle
This oracle checks that the performance metrics are not below a certain threshold. The thresholds are calculated for `TTD/distance` and `TTO/distance`, because both `TTD` and `TTO` increase over time, but their value should be roughly proportional to the distance that the vehicle must traverse.

## Running the experiments
1. Distances: Since the thresholds are calculated for `TTD/distance` and `TTO/distance`, the testcase distances need to be provided in a separate CSV file. The [TEST_CASE_DISTANCES.m](../TEST_CASE_DISTANCES.m) script will output these distances for a test suite.
2. Compute thresholds: `ComputeThresholds.py` outputs the optimal `TTD` and `TTO` thresholds according to the passed experiment results file, which can be written to a CSV file.
   * **Training thresholds (produces [thresholds_baseline2.csv](./results/thresholds_baseline2.csv)):** `./ComputeThresholds.py ./results/Experiment_ResultsBaseline2.csv ./results/experiment_distances_baseline2.csv`
   * **Perfect thresholds (produces [thresholds_perfect.csv](./results/thresholds_perfect.csv)):** `./ComputeThresholds.py ../results/Experiment_Results.csv ./results/experiment_distances.csv`
3. Run the oracle: Produces output like [ResultsPerfect.txt](./results/ResultsPerfect.txt)
   * `py ./EvaluateBaseline.py ../results/Experiment_Results.csv ./results/experiment_distances.csv <THRESHOLDS_FILE>`
