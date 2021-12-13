%% Init
clear;
clc;
addpath('data');
addpath('functions');
rng(1);

%% Source test generation
disp('Generating source test cases...')
nTest = 100; %Number of test cases to generate
sourceTestSuite = generateTestCasesRandomly(nTest);

%% Followup test generation
disp('Generating follow-up test cases...')
MRIP={@(a) generateFollowUpMRIP1_1(a),@(a) generateFollowUpMRIP1_2(a),@(a) generateFollowUpMRIP1_3(a),@(a) generateFollowUpMRIP2(a),@(a) generateFollowUpMRIP3(a),@(a) generateFollowUpMRIP4(a)};
MRIP_Count = size(MRIP,2);
Mutants=["purePursuitUSCityCopia","Mutant_1_of_purePursuitUSCityCopia","Mutant_2_of_purePursuitUSCityCopia","Mutant_3_of_purePursuitUSCityCopia","Mutant_4_of_purePursuitUSCityCopia","Mutant_5_of_purePursuitUSCityCopia","Mutant_6_of_purePursuitUSCityCopia","Mutant_7_of_purePursuitUSCityCopia","Mutant_8_of_purePursuitUSCityCopia","Mutant_9_of_purePursuitUSCityCopia","Mutant_10_of_purePursuitUSCityCopia",...
    "Mutant_11_of_purePursuitUSCityCopia","Mutant_12_of_purePursuitUSCityCopia","Mutant_13_of_purePursuitUSCityCopia","Mutant_14_of_purePursuitUSCityCopia","Mutant_15_of_purePursuitUSCityCopia","Mutant_16_of_purePursuitUSCityCopia","Mutant_17_of_purePursuitUSCityCopia","Mutant_18_of_purePursuitUSCityCopia","Mutant_19_of_purePursuitUSCityCopia","Mutant_20_of_purePursuitUSCityCopia"];
Mutants_Count = size(Mutants,2);

followupTestSuite(Mutants_Count,MRIP_Count,nTest) = sourceTestSuite{1,1};

for mutant=0:Mutants_Count-1
    for mrip=0:MRIP_Count-2
        for test=1:nTest
            followupTestSuite(mutant+1,mrip+1,test) = MRIP{mrip+1}(sourceTestSuite{test});
        end
    end
end

% MRIP4 was generated last, and needs to be kept that way for RNG
% compatibility with original experiments
mrip = MRIP_Count-1;
for mutant=0:Mutants_Count-1
    for test=1:nTest
        followupTestSuite(mutant+1,mrip+1,test) = MRIP{mrip+1}(sourceTestSuite{test});
    end
end

%% Save testSuite
disp('Saving test suites...')
save('testSuite.mat', 'sourceTestSuite', 'followupTestSuite');

%% Follow-up test generation functions

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