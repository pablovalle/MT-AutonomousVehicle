% Pure Pursuit Model Initialization
%
% Copyright 2020 The MathWorks, Inc.
%clear;
%rng(0);
%% add Image to the path
addpath(genpath('Images'));

%% load the scene data file generated from Driving Scenario Designer
load('USCity.mat');

%% define reference points
%refPose = data.ActorSpecifications(1,65).Waypoints;
% refPose=generateWay(8,35,0);
refPose=generateWay(1,4,0);

xRef = refPose(:,1);
yRef = -refPose(:,2);
%% define reference time for plotting 
Ts = 100; % simulation time
s = size(xRef);
tRef = (linspace(0,Ts,s(1)))'; % this time variable is used in the "2D Visulaization" for plotting the refernce points

%% define parameters used in the models
L = 3; % bicycle length
ld = 6; % lookahead distance
X_o = refPose(1,1); % initial vehicle position
Y_o = -refPose(1,2); % initial vehicle position 
psi_o = yawCalculator(X_o,Y_o,refPose(2,1),-refPose(2,2)); % initial yaw angle
X_last=refPose(size(refPose,1),1);
Y_last=-refPose(size(refPose,1),2);

%% define data for velocity lookup table
% lookUpt = readmatrix('velocityDistribution.xlsx');
% xlt = lookUpt(2:27,1);
% ylt = lookUpt(1,2:32);
% vel = lookUpt(2:27,2:32);

%% generate other vehicles
generateVehicles();
% generateVehiclesMiddle(xRef,yRef);
% % 
load('vehicles.mat');
% load('vehiclesMiddle.mat');
%% Config variables
nominalSpeed = 10; %[6-15]
minimalSpeed = 5; %[0.5-5]
angVelGain = 80; %[0-100]
approximationReductionGain = 0.4; %[0.2-5] ? 
Kpvel = 700; %[orig = 700]
Kivel = 1; %[orig = 1]


%% open simulator
%purePursuitUSCity