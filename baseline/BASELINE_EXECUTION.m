clear;
clc;

%% Init
disp('Initializing...')
addpath('../data');
addpath('../functions');
addpath('../dijkstra');
addpath('mutants');
%% Enumerate MRIPs and mutants
Mutants=["../purePursuitUSCity","Mutant_1_1_of_purePursuitUSCity","Mutant_2_1_of_purePursuitUSCity","Mutant_3_1_of_purePursuitUSCity","Mutant_4_1_of_purePursuitUSCity","Mutant_5_1_of_purePursuitUSCity"];
Mutants_Count = size(Mutants,2);
%% Init Results table
ResultsTableFile = 'Experiment_Results2.xlsx';
ResultsTableVariableNames={'Model','Test Case','# of Waypoints','Error distance (Source)','Time to destination (Source)','Balancing (Source)','Distance to the car Source','Source exec time'};
ResultsTableCreated = false;
%% Init state
load testSuiteBaseline;
nTest = size(sourceTestSuite, 2);
if isfile("experimentProgress.csv")
    disp('Loading state from experimentProgress.csv...')
    load('experimentProgress.csv');
    mutant_index = experimentProgress(1);
    test_index = experimentProgress(2);
    ResultsTableCreated = mutant_index + test_index > 1;
else
    mutant_index = 0;
    test_index = 1;
end
%% Load models
disp('Loading SUT models...')
for i=mutant_index:Mutants_Count-1
    load_system(Mutants(i+1));
end
%% Empty QoSMeasure struct for preallocation
QoSMeasureEmpty.errorDistance = -inf;
QoSMeasureEmpty.balancing = -inf;
QoSMeasureEmpty.timeToDestination = -inf;
QoSMeasureEmpty.Distance = -inf;
%% Test Execution
disp('Executing test cases...')
for i=mutant_index:Mutants_Count-1
    QoSMeasureSource = repmat(QoSMeasureEmpty, nTest);
    for ii=test_index:nTest
       % Store experiment progress
       save('experimentProgress.csv', 'i', 'ii', '-ascii');
       % Reset for next iterations after loading
       mutant_index = 0;
       test_index = 1;
       % Display current test execution
       disp('========================================')
       disp(['Mutant = ' num2str(i+1) '/' num2str(Mutants_Count)]);
       disp(['Test case = ' num2str(ii) '/' num2str(nTest)])
       disp(['Execution moment=  ' datestr(datetime('now'))]);
       % Execute source test case
       if QoSMeasureSource(ii).timeToDestination == -inf
          tic;
          QoSMeasureSource(ii) = executeTestCase(sourceTestSuite{ii},Mutants(1,i+1));
          testDurSource = toc;
       else
          testDurSource = 0;
       end
       QoSMeasure = QoSMeasureSource(ii);
       % Execute follow-up test case
       tic;
       ResultsTable=table(Mutants(1,i+1),ii,size(sourceTestSuite{ii}.xRef,1),QoSMeasure.errorDistance,QoSMeasure.timeToDestination,QoSMeasure.balancing,QoSMeasure.Distance,testDurSource);   
       % Write results table
       if ResultsTableCreated
            writetable(ResultsTable, ResultsTableFile, "WriteMode", "append", "WriteVariableNames", false);
       else
            ResultsTable.Properties.VariableNames=ResultsTableVariableNames;
            writetable(ResultsTable, ResultsTableFile);
            ResultsTableCreated = true;
       end
    end
    
end
