# Baseline oracle
TODO

## Running the experiments
1. Compute thresholds: `ComputeThresholds.py` outputs the optimal `TTD` and `TTO` thresholds according to the passed experiment results file, which can be written to a CSV file.
   * **Training thresholds (produces [thresholds_baseline2.csv](./results/thresholds_baseline2.csv)):** `./ComputeThresholds.py ./results/Experiment_ResultsBaseline2.csv ./results/experiment_distances_baseline2.csv`
   * **Perfect thresholds (produces [thresholds_perfect.csv](./results/thresholds_perfect.csv)):** `./ComputeThresholds.py ../results/Experiment_Results.csv ./results/experiment_distances.csv`
2. Run the oracle: Produces output like [ResultsPerfect.txt](./results/ResultsPerfect.txt)
   * `py ./EvaluateBaseline.py ../results/Experiment_Results.csv ./results/experiment_distances.csv <THRESHOLDS_FILE>`
