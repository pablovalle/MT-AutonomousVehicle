function [numCurve1,numCurve2]=calcNumCurve(refX,refY,point1,point2)
    numPoints=(size(refX,1)-1)/10;
    x_0=refX(1,1);
    y_0=refY(1,1);
    psi1=yawCalculator(x_0,y_0,refX(11,1),refY(11,1));
    numCurve1=0;
    numCurve2=0;
    for i=2:numPoints
        j=i-1;
        psi2=yawCalculator(refX((10*j)+1,1),refY((10*j)+1,1),refX((10*i)+1,1),refY((10*i)+1,1));
        if j<point1 && (psi1<=psi2-0.4 || psi1>=psi2+0.4)
            numCurve1=numCurve1+1;
        end
        if j<point2 && (psi1<=psi2-0.4 || psi1>=psi2+0.4)
            numCurve2=numCurve2+1;
        end
        psi1=psi2;
    end
end