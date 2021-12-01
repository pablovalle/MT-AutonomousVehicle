function generateVehiclesMiddle(refX,refY, speed)
    numPoints=(size(refX,1)-mod(size(refX,1),10))/10;
       
    if numPoints>1
        point1=randi([1 numPoints-1]);
        point2=randi([1 numPoints-1]);
    else
        point1=1;
        point2=1;
    end
    
    while point1==point2 && numPoints>=3
        point2=randi([1 numPoints-1]);
    end
    [numCurve1, numCurve2]=calcNumCurve(refX,refY,point1,point2);
    
    if point1<point2
        first=0;
        second=1;
    else
        first=1;
        second=0;
    end
    time2First=calcTime2Point(point1,first, numCurve1,refX,refY,speed);
    time2Second=calcTime2Point(point2,second, numCurve2,refX,refY,speed);
    
    [x_1, y_1,psi_1,slope_x1,slope_y1]=calcPos(time2First,point1,refX,refY);
    
    [x_2, y_2, psi_2,slope_x2,slope_y2]=calcPos(time2Second,point2,refX,refY);

    save('vehiclesMIddle.mat','x_1','y_1','psi_1','slope_x1','slope_y1'...
        ,'x_2','y_2','psi_2','slope_x2','slope_y2');
end