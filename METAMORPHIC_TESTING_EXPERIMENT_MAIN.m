clear;
clc;

%% Init
disp('Initializing...')
addpath('data');
addpath('functions');
addpath('ExperimentalMutants');
setUpPurePursuitUSCity;
%% Test generation
disp('Generating source test cases...')
rng(1);
if isfile("testSuite.mat")
    load('testSuite.mat');
    rng(rngstate);
    nTest = size(testSuite, 2);
else
    nTest = 100; %Number of test cases to generate
    testSuite = generateTestCasesRandomly(nTest);
    rngstate = rng();
    save('testSuite.mat', 'testSuite', 'rngstate');
end
%% Enumerate MRIPs and mutants
disp('Initializing MRIPs and Mutants...')
MRIP={@(a) generateFollowUpMRIP1_1(a),@(a) generateFollowUpMRIP1_2(a),@(a) generateFollowUpMRIP1_3(a),@(a) generateFollowUpMRIP2(a),@(a) generateFollowUpMRIP3(a),@(a) generateFollowUpMRIP4(a)};
MRIP_Names=["MRIP1_1","MRIP1_2","MRIP1_3","MRIP2","MRIP3", "MRIP4"];
Mutants=["purePursuitUSCity","Mutant_1_of_purePursuitUSCity","Mutant_2_of_purePursuitUSCity","Mutant_3_of_purePursuitUSCity","Mutant_4_of_purePursuitUSCity","Mutant_5_of_purePursuitUSCity","Mutant_6_of_purePursuitUSCity","Mutant_7_of_purePursuitUSCity","Mutant_8_of_purePursuitUSCity","Mutant_9_of_purePursuitUSCity","Mutant_10_of_purePursuitUSCity",...
    "Mutant_11_of_purePursuitUSCity","Mutant_12_of_purePursuitUSCity","Mutant_13_of_purePursuitUSCity","Mutant_14_of_purePursuitUSCity","Mutant_15_of_purePursuitUSCity","Mutant_16_of_purePursuitUSCity","Mutant_17_of_purePursuitUSCity","Mutant_18_of_purePursuitUSCity","Mutant_19_of_purePursuitUSCity","Mutant_20_of_purePursuitUSCity"];
%% Init Results table
ResultsTableFile = 'Experiment_Results.csv';
ResultsTableVariableNames={'Model','MRIP','Test Case','# of Waypoints','Error distance (Source)','Error distance (FollowUp)','Time to destination (Source)','Time to destination (FollowUp)','Balancing (Source)','Balancing (FollowUp)','Distance to the car Follow up','Distance to the car Source','Source exec time','Follow up exec time'};
ResultsTableCreated = false;
%% Test Execution
disp('Executing test cases...')
for i=0:size(Mutants,2)-1
    for ii=1:nTest
        tic;
        QoSMeasure = executeTestCase(testSuite{ii},Mutants(1,i+1));
        testDurSource = toc;
        for j=0:size(MRIP,2)-1
           tic;
           QoSMeasureFollowUp = executeTestCase(MRIP{j+1}(testSuite{ii}),Mutants(1,i+1));
           testDurFollowUp = toc;
           num=ii+(nTest*j)+i*nTest*size(MRIP,2);
           ResultsTable=table(Mutants(1,i+1),MRIP_Names(1,j+1),ii,size(testSuite{ii}.xRef,1),QoSMeasure.errorDistance,QoSMeasureFollowUp.errorDistance,QoSMeasure.timeToDestination,QoSMeasureFollowUp.timeToDestination,QoSMeasure.balancing,QoSMeasureFollowUp.balancing,QoSMeasureFollowUp.Distance,QoSMeasure.Distance,testDurSource,testDurFollowUp);   
           if ResultsTableCreated
            writetable(ResultsTable, ResultsTableFile, "WriteMode", "append", "WriteVariableNames", false);
           else
            ResultsTable.Properties.VariableNames=ResultsTableVariableNames;
            writetable(ResultsTable, ResultsTableFile);
            ResultsTableCreated = true;
           end
           disp('========================================')
           disp(['Test case = ' num2str(ii)])
           disp(['MRIP = ' num2str(j)]);
           disp(['Mutant = ' num2str(i)]);
           disp(['Number of Waypoints = ' num2str(size(xRef,1))]);
           disp(['Error distance(Source) = ' num2str(QoSMeasure.errorDistance)]); %a higher nominal speed shall have a higher error distance
           disp(['Error distance(FollowUP) = ' num2str(QoSMeasureFollowUp.errorDistance )]); %a higher nominal speed shall have a higher error distance
           disp(['Time to destination (Source) = ', num2str(QoSMeasure.timeToDestination)]); % a higher nominal speed and higher minimal speed shall have a lower time to destination
           disp(['Time to destination (FollowUp) = ', num2str(QoSMeasureFollowUp.timeToDestination)]); % a higher nominal speed and higher minimal speed shall have a lower time to destination   
           disp(['Balancing (Source) = ', num2str(QoSMeasure.balancing)]); % a higher norminal speed shall have a higher balancing || a higher bicycle length and lookahead distance shall have a higher balancing
           disp(['Balancing (FollowUp) = ', num2str(QoSMeasureFollowUp.balancing )]); % a higher norminal speed shall have a higher balancing || a higher bicycle length and lookahead distance shall have a higher balancing
           disp(['Execution time (Source) = ' num2str(testDurSource)]); 
           disp(['Execution time (FollowUP) = ' num2str(testDurFollowUp)]);
           t=datetime('now');
           disp(['Execution moment=  ' datestr(t)]);
        end
    end
    %writetable(ResultsTable,'Experiment_Results.xlsx');
end


function testCase = generateFollowUpMRIP1_1(sourceTestCase)
    %MRIP: increment nominal speed
    testCase = sourceTestCase;
    testCase.nominalSpeed = testCase.nominalSpeed *1.1;
    
end

function testCase = generateFollowUpMRIP1_2(sourceTestCase)
    %MRIP: increment nominal speed
    testCase = sourceTestCase;
    testCase.nominalSpeed = testCase.nominalSpeed *1.2;
end
function testCase = generateFollowUpMRIP1_3(sourceTestCase)
    %MRIP: increment nominal speed
    testCase = sourceTestCase;
    testCase.nominalSpeed = testCase.nominalSpeed *1.3;
end

function testCase = generateFollowUpMRIP2(sourceTestCase)
    %MRIP: Generate vehicles inside of the vehicle's path
    generateVehiclesMiddle(sourceTestCase.xRef,sourceTestCase.yRef,sourceTestCase.nominalSpeed);
    load('vehiclesMIddle.mat');
    testCase=sourceTestCase;
    testCase.psi1=psi_1;
    testCase.psi2=psi_2;
    testCase.slopeX1=slope_x1;
    testCase.slopeX2=slope_x2;
    testCase.slopeY1=slope_y1;
    testCase.slopeY2=slope_y2;
    testCase.X1=x_1;
    testCase.X2=x_2;
    testCase.Y1=y_1;
    testCase.Y2=y_2;
    
end

function testCase = generateFollowUpMRIP3(sourceTestCase)
    %MRIP: change of the waypoints from a direction to another
    testCase = sourceTestCase;
    testCase.xRef = flip(testCase.xRef);
    testCase.yRef = flip(testCase.yRef);
    testCase.refPose=flip(testCase.refPose);
end

function testCase=generateFollowUpMRIP4(sourceTestCase)
    %MRIP: Remove 20% of the guidance points
    testCase = sourceTestCase;
    toDelete=randi([2,size(sourceTestCase.xRef,1)-1],round(size(sourceTestCase.xRef,1)*0.2),1);
    for j=1: size(toDelete,1)
        testCase.xRef(toDelete(j,1),1)=1000;
        testCase.yRef(toDelete(j,1),1)=1000;
    end
    testCase.xRef=testCase.xRef(testCase.xRef~=1000);
    testCase.yRef=testCase.yRef(testCase.yRef~=1000);
    refPose(:,1)=testCase.xRef(:,1);
    refPose(:,2)=testCase.yRef(:,1);
    testCase.refPose=refPose;
end
