function generateVehicles()
%% first vehicle
x_1=-186.600;
y_1=0;
slope_x1=0;
slope_y1=15;
psi_1=yawCalculator(x_1,x_1,x_1+slope_x1,-(x_1+slope_y1));
% refPose1=generateWay(randi([1,51]),randi([1,51]),1);
% xRef1 = refPose1(:,1);
% yRef1 = -refPose1(:,2);
% X_o1 = refPose1(1,1); % initial vehicle position
% Y_o1 = -refPose1(1,2); % initial vehicle position 
% psi_o1 = yawCalculator(X_o1,Y_o1,refPose1(2,1),-refPose1(2,2)); % initial yaw angle
% X_last1=refPose1(size(refPose1,1),1);
% Y_last1=refPose1(size(refPose1,1),2);

%% second vehicle
x_2=-112.6;
y_2=112.500;
slope_x2=0;
slope_y2=0;
psi_2=yawCalculator(x_2,x_2,x_2+slope_x2,-(x_2+slope_y2));
% refPose2=generateWay(randi([1,51]),randi([1,51]),1);
% xRef2 = refPose2(:,1);
% yRef2 = -refPose2(:,2);
% X_o2 = refPose2(1,1); % initial vehicle position
% Y_o2 = -refPose2(1,2); % initial vehicle position 
% psi_o2 = yawCalculator(X_o2,Y_o2,refPose2(2,1),-refPose2(2,2)); % initial yaw angle
% X_last2=refPose2(size(refPose2,1),1);
% Y_last2=refPose2(size(refPose2,1),2);
% 
%% third vehicle
% x_3=-184;
% y_3=-50;
% slope_x3=0;
% slope_y3=9;
% psi_3=yawCalculator(x_3,x_3,x_3+slope_x3,-(x_3+slope_y3));
% refPose3=generateWay(randi([1,51]),randi([1,51]),1);
% xRef3 = refPose3(:,1);
% yRef3 = -refPose3(:,2);
% X_o3 = refPose3(1,1); % initial vehicle position
% Y_o3 = -refPose3(1,2); % initial vehicle position 
% psi_o3 = yawCalculator(X_o3,Y_o3,refPose3(2,1),-refPose3(2,2)); % initial yaw angle
% X_last3=refPose3(size(refPose3,1),1);
% Y_last3=refPose3(size(refPose3,1),2);
% 
%% fourth vehicle
% x_4=76.4000;
% y_4=-112.5000;
% slope_x4=-15;
% slope_y4=0;
% psi_4=yawCalculator(x_4,x_4,x_4+slope_x4,-(x_4+slope_y4));
% refPose4=generateWay(randi([1,51]),randi([1,51]),2);
% xRef4 = refPose4(:,1);
% yRef4 = -refPose4(:,2);
% X_o4 = refPose4(1,1); % initial vehicle position
% Y_o4 = -refPose4(1,2); % initial vehicle position 
% psi_o4 = yawCalculator(X_o4,Y_o4,refPose4(2,1),-refPose4(2,2)); % initial yaw angle
% X_last4=refPose4(size(refPose4,1),1);
% Y_last4=refPose4(size(refPose4,1),2);
% 
%% fifth vehicle
% x_5=76.4000;
% y_5=-2;
% slope_x5=-15;
% slope_y5=0;
% psi_5=yawCalculator(x_5,x_5,x_5+slope_x4,-(x_5+slope_y5));
% refPose5=generateWay(randi([1,51]),randi([1,51]),1);
% xRef5 = refPose5(:,1);
% yRef5 = -refPose5(:,2);
% X_o5 = refPose5(1,1); % initial vehicle position
% Y_o5 = -refPose5(1,2); % initial vehicle position 
% psi_o5 = yawCalculator(X_o5,Y_o5,refPose5(2,1),-refPose5(2,2)); % initial yaw angle
% X_last5=refPose5(size(refPose5,1),1);
% Y_last5=refPose5(size(refPose5,1),2);
% 
% %% sixth vehicle
% refPose6=generateWay(randi([1,51]),randi([1,51]),1);
% xRef6 = refPose6(:,1);
% yRef6 = -refPose6(:,2);
% X_o6 = refPose6(1,1); % initial vehicle position
% Y_o6 = -refPose6(1,2); % initial vehicle position 
% psi_o6 = yawCalculator(X_o6,Y_o6,refPose6(2,1),-refPose6(2,2)); % initial yaw angle
% X_last6=refPose6(size(refPose6,1),1);
% Y_last6=refPose6(size(refPose6,1),2);
% 
% %% seventh vehicle
% refPose7=generateWay(randi([1,51]),randi([1,51]),1);
% xRef7 = refPose7(:,1);
% yRef7 = -refPose7(:,2);
% X_o7 = refPose7(1,1); % initial vehicle position
% Y_o7 = -refPose7(1,2); % initial vehicle position 
% psi_o7 = yawCalculator(X_o7,Y_o7,refPose7(2,1),-refPose7(2,2)); % initial yaw angle
% X_last7=refPose7(size(refPose7,1),1);
% Y_last7=refPose7(size(refPose7,1),2);
% 
% %% eighth vehicle
% refPose8=generateWay(randi([1,51]),randi([1,51]),1);
% xRef8 = refPose8(:,1);
% yRef8 = -refPose8(:,2);
% X_o8 = refPose8(1,1); % initial vehicle position
% Y_o8 = -refPose8(1,2); % initial vehicle position 
% psi_o8 = yawCalculator(X_o8,Y_o8,refPose8(2,1),-refPose8(2,2)); % initial yaw angle
% X_last8=refPose8(size(refPose8,1),1);
% Y_last8=refPose8(size(refPose8,1),2);
% 
% %% nineth vehicle
% refPose9=generateWay(randi([1,51]),randi([1,51]),1);
% xRef9 = refPose9(:,1);
% yRef9 = -refPose9(:,2);
% X_o9 = refPose9(1,1); % initial vehicle position
% Y_o9 = -refPose9(1,2); % initial vehicle position 
% psi_o9 = yawCalculator(X_o9,Y_o9,refPose9(2,1),-refPose9(2,2)); % initial yaw angle
% X_last9=refPose9(size(refPose9,1),1);
% Y_last9=refPose9(size(refPose9,1),2);
% 
% %% tenth vehicle
% refPose10=generateWay(randi([1,51]),randi([1,51]),1);
% xRef10 = refPose10(:,1);
% yRef10 = -refPose10(:,2);
% X_o10 = refPose10(1,1); % initial vehicle position
% Y_o10 = -refPose10(1,2); % initial vehicle position 
% psi_o10 = yawCalculator(X_o10,Y_o10,refPose10(2,1),-refPose10(2,2)); % initial yaw angle
% X_last10=refPose10(size(refPose10,1),1);
% Y_last10=refPose10(size(refPose10,1),2);


%% save workspace
save('vehicles.mat');
end