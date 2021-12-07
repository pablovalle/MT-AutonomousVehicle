clear;
clc;

%% Init
disp('Initializing...')
addpath('data');
addpath('functions');
addpath('ExperimentalMutants');
setUpPurePursuitUSCity;
%% Enumerate MRIPs and mutants
MRIP_Names=["MRIP1_1","MRIP1_2","MRIP1_3","MRIP2","MRIP3", "MRIP4"];
MRIP_Count = size(MRIP_Names,2);
Mutants=["purePursuitUSCity","Mutant_1_of_purePursuitUSCity","Mutant_2_of_purePursuitUSCity","Mutant_3_of_purePursuitUSCity","Mutant_4_of_purePursuitUSCity","Mutant_5_of_purePursuitUSCity","Mutant_6_of_purePursuitUSCity","Mutant_7_of_purePursuitUSCity","Mutant_8_of_purePursuitUSCity","Mutant_9_of_purePursuitUSCity","Mutant_10_of_purePursuitUSCity",...
    "Mutant_11_of_purePursuitUSCity","Mutant_12_of_purePursuitUSCity","Mutant_13_of_purePursuitUSCity","Mutant_14_of_purePursuitUSCity","Mutant_15_of_purePursuitUSCity","Mutant_16_of_purePursuitUSCity","Mutant_17_of_purePursuitUSCity","Mutant_18_of_purePursuitUSCity","Mutant_19_of_purePursuitUSCity","Mutant_20_of_purePursuitUSCity"];
Mutants_Count = size(Mutants,2);
%% Init Results table
ResultsTableFile = 'Experiment_Results.csv';
ResultsTableVariableNames={'Model','MRIP','Test Case','# of Waypoints','Error distance (Source)','Error distance (FollowUp)','Time to destination (Source)','Time to destination (FollowUp)','Balancing (Source)','Balancing (FollowUp)','Distance to the car Follow up','Distance to the car Source','Source exec time','Follow up exec time'};
%ResultsTableWrittenBefore = max(fcountlines(ResultsTableFile) - 1, 0);
%disp(['ResultsTableWrittenBefore = ' num2str(ResultsTableWrittenBefore)]);
ResultsTableCreated = false;
%% Init state
load testSuite;
nTest = size(sourceTestSuite, 2);
if isfile("experimentProgress.csv")
    disp('Loading state from experimentProgress.csv...')
    load('experimentProgress.csv');
    mutant_index = experimentProgress(1);
    mrip_index = experimentProgress(2);
    test_index = experimentProgress(3);
    ResultsTableCreated = mutant_index + mrip_index + test_index > 1;
else
    mutant_index = 0;
    mrip_index = 0;
    test_index = 1;
end
%% Test Execution
disp('Executing test cases...')
for i=mutant_index:Mutants_Count-1
    for j=mrip_index:MRIP_Count-1
        for ii=test_index:nTest
           % Store experiment progress
           save('experimentProgress.csv', 'i', 'j', 'ii', '-ascii');
           % Display current test execution
           disp('========================================')
           disp(['Mutant = ' num2str(i+1) '/' num2str(Mutants_Count)]);
           disp(['MRIP = ' num2str(j+1) '/' num2str(MRIP_Count)]);
           disp(['Test case = ' num2str(ii) '/' num2str(nTest)])
           disp(['Execution moment=  ' datestr(datetime('now'))]);
           % Execute source test case
           if j == 0 || exist('QoSMeasure','var') ~= 1
              tic;
              QoSMeasure = executeTestCase(sourceTestSuite{ii},Mutants(1,i+1));
              testDurSource = toc;
           end
           % Execute follow-up test case
           tic;
           QoSMeasureFollowUp = executeTestCase(followupTestSuite{i+1, j+1, ii},Mutants(1,i+1));
           testDurFollowUp = toc;
           num=ii+(nTest*j)+i*nTest*size(MRIP,2);
           ResultsTable=table(Mutants(1,i+1),MRIP_Names(1,j+1),ii,size(sourceTestSuite{ii}.xRef,1),QoSMeasure.errorDistance,QoSMeasureFollowUp.errorDistance,QoSMeasure.timeToDestination,QoSMeasureFollowUp.timeToDestination,QoSMeasure.balancing,QoSMeasureFollowUp.balancing,QoSMeasureFollowUp.Distance,QoSMeasure.Distance,testDurSource,testDurFollowUp);   
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
    %writetable(ResultsTable,'Experiment_Results.xlsx');
end
