# Autonomous-vehicle

This repository shares the experiments used in the "Performance-Driven Metamorphic Testing ofCyber-Physical Systems" paper for replicability purposes:

## Files
"METAMORPHIC_TESTING_EXPERIMENT_MAIN.m" is the main script to execute the test cases on the system and its mutants.

"CompileEvaluationResults.py" is the script that compiles the final evaluation results from the system outputs produced by the previous step.

### Directory structure
* The "ExperimentalMutants" includes the mutants used in this evaluation.
* The "functions" folder includes the functions needed to perform the execution.
* The "data" folder includes the data needed to run the experiments.
* The "results" folder includes the test execution outputs, so that the expensive simulation step can be skipped, as well as the final evaluation results.

## Requirements
The requirements to execute the experiments can be found in the following file:

https://github.com/mathworks/vehicle-pure-pursuit/blob/a90aa52bd80676ae54b87e659d86901c5ef0f09d/README.md

Under the **3_USCity** section.

Our experimental setup does not require the 3D visualization environment, so the GPU requirement can be ignored. The simulations have also been successfuly run on a machine with only 8GB of available RAM.

# Experiment runtime
Running the simulations (METAMORPHIC_TESTING_EXPERIMENT_MAIN.m) took around 7 days in total (~8 hours per mutant) on a laptop with the following specs:
* CPU: Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz   2.59 GHz
* RAM: 8GB
* OS: Windows 10
* Matlab version: 2021b

The evaluation results presented in the paper are based on the system outputs collected in "results/Experiment_Results_Paper.csv", which were obtained with Matlab version 2020a under Windows 10. The system outputs obtained, and thus the evaluation results, might differ slightly on different systems.
