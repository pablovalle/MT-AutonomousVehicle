function [time]=calcTime2Point(point,first,numCurve,refX,refY,speed)
    point=(point*10)+1;
    diff_x=refX(1,1)-refX(point,1);
    diff_y=refY(1,1)-refY(point,1);
    time_x=abs(diff_x/speed);
    time_y=abs(diff_y/speed);
    time=time_x+time_y+first*5+numCurve*3;

end