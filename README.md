# Autonomous-vehicle
This repository contains the replication package for the autonomous vehicle experiments presented in the "Performance-Driven Metamorphic Testing of Cyber-Physical Systems" paper.

These experiments are based on an open source autonomous vehicle model published by MathWorks: https://github.com/mathworks/vehicle-pure-pursuit.

## Running the experiments
1. Install the [requirements](#requirements) for the [simulation](#simulation) and the [evaluation script](#evaluation-script).
2. Run `GENERATE_TESTSUITE.m` (Can be skipped by copying `Results/testSuite.mat` to the project's root directory).
3. Run `METAMORPHIC_TESTING_EXPERIMENT_MAIN.m` ([It takes a while](#experiment-runtime), can be skipped by copying `Results/ExperimentResults.csv` to the project's root directory).
4. Run `EvaluateMRs.py .\results\Experiment_Results.xlsx EvaluationNew.xlsx` (Should produce results similar to `Results/EvaluationNew.xlsx`).

`ExperimentResults.*` contains all the simulation results. By default we use the CSV format, but XLSX can also be used by tweaking `METAMORPHIC_TESTING_EXPERIMENT_MAIN.m` a bit.

`Evaluation*` contains the failures for each mutant (and the original) and metamorphic test, as well as the number of possible metamorphic test failures. With this data, the false positives, mutation score, and failure detection ratio can be calculated. The evaluation results consist of 2 workbooks, so they can only be stored in a single file if the XLSX format is used (`Evaluation.xlsx`), and for CSV, the workbooks are written into 2 different `Evaluation_*.csv` files instead.

## Requirements

### Simulation
The requirements to execute the simulations (`GENERATE_TESTSUITE.m` and `METAMORPHIC_TESTING_EXPERIMENT_MAIN.m`) can be found in the following file:

https://github.com/mathworks/vehicle-pure-pursuit/blob/a90aa52bd80676ae54b87e659d86901c5ef0f09d/README.md

Under the **3_USCity** section.

Our experimental setup does not require the 3D visualization environment, so the GPU requirement can be ignored. The simulations have also been successfuly run on a machine with only 8GB of available RAM.

### Evaluation script
The final results are compiled by the `EvaluateMRs.py` script, which requires (tested under Windows 10):
* **Python 3** (`CPython 3.7.0`)
* **pandas** (`pip install pandas==1.1.5`)
* **(Optional) openpyxl** (`pip install openpyxl==3.0.9`) (For reading and/or writing XLSX files, but CSV can be used instead)

Requirement versions are the exact ones used to verify the replication package, other versions may work.

## Experiment runtime
Running the simulations (`METAMORPHIC_TESTING_EXPERIMENT_MAIN.m`) took around 7 days in total (~8 hours per mutant) on a laptop with the following specs:
* CPU: Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz   2.59 GHz
* RAM: 8GB
* OS: Windows 10
* Matlab version: 2021b

The evaluation results presented in the paper (`Results/Evaluation*`) are based on the system outputs collected in `Results/Experiment_Results*`, which were obtained with Matlab version 2020a under Windows 10. The system outputs obtained, and thus the evaluation results, might differ slightly on different systems.

## Directory structure
* The `ExperimentalMutants` directory includes the mutants used in this evaluation.
* The `functions` directory includes the functions needed by the Matlab scripts.
* The `data` directory includes some data needed to run the experiments.
* The `Results` directory includes al the intermediate and final experimental data, so that the expensive simulation and other steps can be skipped.
* The `baseline` directory includes the scripts and data for the baseline (threshold-based oracle) experiments.
