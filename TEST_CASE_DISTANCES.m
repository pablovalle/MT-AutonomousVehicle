clear;
clc;
%% Load test suite
load testSuite;
%% Iterate over source testcases
disp("testcase,distance");
for ii=1:size(sourceTestSuite, 2)
    disp(ii + "," + sourceTestSuite{ii}.distance);
end
