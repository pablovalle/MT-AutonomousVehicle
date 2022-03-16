%% Init
clear;
clc;
addpath('../data');
addpath('../functions');
addpath('../dijkstra');
rng(2);

%% Source test generation
disp('Generating source test cases...')
nTest = 1300; %Number of test cases to generate
sourceTestSuite = generateTestCasesRandomly(nTest);

disp('Saving test suites...')
save('testSuiteBaseline.mat', 'sourceTestSuite');
