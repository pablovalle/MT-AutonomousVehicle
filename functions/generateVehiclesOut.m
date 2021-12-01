function generateVehiclesOut(sourceTestCase)
    is=1;
    while is==1
        is=0;
        point1= randi([1 size(sourceTestCase.points,1)]);
        for i=1:size(sourceTestCase.rute,2)
            if point1==sourceTestCase.rute(1,i)
                is=1;
            end
        end
    end
    is=1;
    while is==1
        is=0;
        point2= randi([1 size(sourceTestCase.points,1)]);
        for i=1:size(sourceTestCase.rute,2)
            if point2==sourceTestCase.rute(1,i)
                is=1;
            end
        end
    end
    x_1=sourceTestCase.points(point1,1);
    y_1=sourceTestCase.points(point1,2);
    slope_x1=0;
    slope_y1=0;
    x_2=sourceTestCase.points(point2,1);
    y_2=sourceTestCase.points(point2,2);
    slope_x2=0;
    slope_y2=0;
    psi_1=1.5*pi;
    psi_2=0;
    
%     if abs(psi0)>=(pi*0 -0.4) && abs(psi0)<=(pi*0+0.4)
%         x_1=sourceTestCase.xRef(point1,1)+0;
%         y_1=sourceTestCase.yRef(point1,1)+4;
%     elseif abs(psi0)>=(pi*0.5 -0.4) && abs(psi0)<=(pi*0.5+0.4)
%         x_1=sourceTestCase.xRef(point1,1)+4;
%         y_1=sourceTestCase.yRef(point1,1)+0;
%     elseif abs(psi0)>=(pi -0.4) && abs(psi0)<=(pi+0.4)
%         x_1=sourceTestCase.xRef(point1,1)+0;
%         y_1=sourceTestCase.yRef(point1,1)-4;
%     elseif abs(psi0)>=(pi*1.5 -0.4) && abs(psi0)<=(pi*1.5+0.4)
%         x_1=sourceTestCase.xRef(point1,1)-4;
%         y_1=sourceTestCase.yRef(point1,1)+0;
%     end
%     if psi_1>=2*pi
%         psi_1=psi_1-2*pi;
%     elseif psi_1<0
%         psi_1=psi_1+2*pi;
%     end
%     slope_x1= 0;
%     slope_y1= 0;
%     if abs(psi1)>=(pi*0 -0.4) && abs(psi1)<=(pi*0+0.4)
%         x_2=sourceTestCase.xRef(point2,1)+0;
%         y_2=sourceTestCase.yRef(point2,1)-4;
%         slope_x2= -1;
%         slope_y2= 0;
%     elseif abs(psi1)>=(pi*0.5 -0.4) && abs(psi1)<=(pi*0.5+0.4)
%         x_2=sourceTestCase.xRef(point2,1)-4;
%         y_2=sourceTestCase.yRef(point2,1)+0;
%         slope_x2= 0;
%         slope_y2= -1;
%     elseif abs(psi1)>=(pi -0.4) && abs(psi1)<=(pi+0.4)
%         x_2=sourceTestCase.xRef(point2,1)+0;
%         y_2=sourceTestCase.yRef(point2,1)+4;
%         slope_x2= 1;
%         slope_y2= 0;
%     elseif abs(psi1)>=(pi*1.5 -0.4) && abs(psi1)<=(pi*1.5+0.4)
%         x_2=sourceTestCase.xRef(point2,1)+4;
%         y_2=sourceTestCase.yRef(point2,1)+0;
%         slope_x2= 0;
%         slope_y2= 1;
%     end
%     psi_2= psi1+pi;
%     if psi_2>=2*pi
%         psi_2=psi_2-2*pi;
%     elseif psi_2<0
%         psi_2=pso_2+2*pi;
%     end
    
    
     save('vehiclesOut.mat','x_1','y_1','psi_1','slope_x1','slope_y1'...
        ,'x_2','y_2','psi_2','slope_x2','slope_y2');
end