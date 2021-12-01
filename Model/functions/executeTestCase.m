function QoSMeasure = executeTestCase(testCase, SUT)
    %setUpPurePursuitUSCity;
    
    
    %% add Image to the path
    addpath(genpath('Images'));

    %% load the scene data file generated from Driving Scenario Designer
    %load('USCity.mat');

    %% define reference points
    %refPose = data.ActorSpecifications(1,65).Waypoints;
    % refPose=generateWay(8,35,0);
    refPoseLocal=testCase.refPose;%(1,32,0);
    %refPose = evalin('base','refPoseLocal');
    assignin('base','refPose',refPoseLocal);
    xRefLocal = refPoseLocal(:,1);
    %xRef = evalin('base','xRefLocal');
    assignin('base','xRef',xRefLocal);
    
    yRefLocal = -refPoseLocal(:,2);
   % yRef = evalin('base','yRefLocal');
    assignin('base','yRef',yRefLocal);
    
    %% define reference time for plotting 
    TsLocal = 100; % simulation time
    %Ts = evalin('base','TsLocal');
    assignin('base','Ts',TsLocal);
    
    sLocal = size(xRefLocal);
    %s = evalin('base','sLocal');
    assignin('base','s',sLocal);
    
    tRefLocal = (linspace(0,TsLocal,sLocal(1)))'; % this time variable is used in the "2D Visulaization" for plotting the refernce points
    %tRef = evalin('base','tRefLocal');
    assignin('base','tRef',tRefLocal);
    
    %% define parameters used in the models
    %LLocal = 3; % bicycle length
   % L = evalin('base','LLocal');
    LLocal=testCase.l;
    assignin('base','L',LLocal);
    
    %ldLocal = 6; % lookahead distance
    %ld = evalin('base','ldLocal');
    ldLocal=testCase.ld;
    assignin('base','ld',ldLocal);
    
    
    X_oLocal = refPoseLocal(1,1); % initial vehicle position
    %X_o = evalin('base','X_oLocal');
    assignin('base','X_o',X_oLocal);
    
    Y_oLocal = -refPoseLocal(1,2); % initial vehicle position 
    %Y_o = evalin('base','Y_oLocal');
    assignin('base','Y_o',Y_oLocal);
    
    if(size(testCase.refPose,1)>11)
        psi_oLocal = yawCalculator(X_oLocal,Y_oLocal,xRefLocal(12,1),yRefLocal(12,1)); % initial yaw angle
    elseif (size(testCase.refPose,1)>10)
        psi_oLocal = yawCalculator(X_oLocal,Y_oLocal,xRefLocal(11,1),yRefLocal(11,1)); % initial yaw angle
    elseif (size(testCase.refPose,1)>9)
        psi_oLocal = yawCalculator(X_oLocal,Y_oLocal,xRefLocal(10,1),yRefLocal(10,1)); % initial yaw angle
    else
        psi_oLocal = yawCalculator(X_oLocal,Y_oLocal,xRefLocal(9,1),yRefLocal(9,1)); % initial yaw angle
    end
    %psi_o = evalin('base','psi_oLocal');
    assignin('base','psi_o',psi_oLocal);
    
    X_lastLocal=refPoseLocal(size(refPoseLocal,1),1);
    %X_last = evalin('base','X_lastLocal');
    assignin('base','X_last',X_lastLocal);
    
    Y_lastLocal=-refPoseLocal(size(refPoseLocal,1),2);
    %Y_last = evalin('base','Y_lastLocal');
    assignin('base','Y_last',Y_lastLocal);
    %% Other cars
    assignin('base','psi_1',testCase.psi1);
    assignin('base','psi_2',testCase.psi2);
    assignin('base','slope_x1',testCase.slopeX1);
    assignin('base','slope_x2',testCase.slopeX2);
    assignin('base','slope_y1',testCase.slopeY1);
    assignin('base','slope_y2',testCase.slopeY2);
    assignin('base','x_1',testCase.X1);
    assignin('base','x_2',testCase.X2);
    assignin('base','y_1',testCase.Y1);
    assignin('base','y_2',testCase.Y2);
    
    %% Speed asignation
    
    nominalSpeedLocal = testCase.nominalSpeed; %[6-15]
    minimalSpeedLocal = testCase.minimalSpeed; %[0.5-5]
    angVelGainLocal = testCase.angVelGain; %[0-100]
    approximationReductionGainLocal = testCase.approximationReductionGain; %[0.2-5] ? 
   
    assignin('base','nominalSpeed',nominalSpeedLocal);
    assignin('base','minimalSpeed',minimalSpeedLocal);
    assignin('base','angVelGain',angVelGainLocal);
    assignin('base','approximationReductionGain',approximationReductionGainLocal);

    simResults = sim(SUT);
    QoSMeasure.errorDistance = simResults.errorDistance;
    QoSMeasure.balancing = simResults.balancing;
    QoSMeasure.timeToDestination = simResults.timeToDestination;
    QoSMeasure.Distance=simResults.Distance;

    

end