function [x,y,psi,slopeX,slopeY]=calcPos(time,point,refX,refY)
    point=(point*10);
    psi_array(:,1)=[0,pi,pi*0.5,pi*1.5];
    psi_0=yawCalculator(refX(point-1,1),refY(point-1,1),refX(point,1),refY(point,1));
    if(point+9<=size(refX,1))
        psi_1=yawCalculator(refX(point,1),refY(point,1),refX(point+9,1),refY(point+9,1));
    else
        psi_1=psi_0;
    end
    if psi_0<0
        psi_0=psi_0+2*pi;
    end
    if psi_1<0
        psi_1=psi_1+2*pi;
    end
    a=randi([1 4]);
    psi=psi_array(a,1);
    if (abs(psi_0)>=(pi*1 -0.4) && abs(psi_0)<=(pi*1+0.4)) || (abs(psi_0)>=(pi*0 -0.4) && abs(psi_0)<=(pi*0+0.4))
        a=randi([3 4]);
        psi=psi_array(a,1);
        while abs(psi)>=(psi_1-0.4) && abs(psi)<=(psi_1+0.4)
            a=randi([3 4]);
            psi=psi_array(a,1);
        end
    elseif (abs(psi_0)>=(pi*0.5 -0.4) && abs(psi_0)<=(pi*0.5+0.4)) || (abs(psi_0)>=(pi*1.5 -0.4) && abs(psi_0)<=(pi*1.5+0.4))
        a=randi([1 2]);
        psi=psi_array(a,1);
        while abs(psi)>=(psi_1-0.4) && abs(psi)<=(psi_1+0.4)
            a=randi([1 2]);
            psi=psi_array(a,1);
        end
    end
    
    
    if abs(psi)>=(pi*0 -0.1) && abs(psi)<=(pi*0+0.1)
        x=refX(point+1,1)-50;
        y=refY(point+1,1);
        slopeX=(50/time);
        slopeY=0;
    elseif abs(psi)>=(pi*0.5 -0.1) && abs(psi)<=(pi*0.5+0.1)
        x=refX(point+1,1);
        y=refY(point+1,1)-50;
        slopeX=0;
        slopeY=50/time;
    elseif abs(psi)>=(pi*1 -0.1) && abs(psi)<=(pi*1+0.1)
        x=refX(point+1,1)+50;
        y=refY(point+1,1);
        slopeX=(-50/time);
        slopeY=0;
    elseif abs(psi)>=(pi*1.5 -0.1) && abs(psi)<=(pi*1.5+0.1)
        x=refX(point+1,1);
        y=refY(point+1,1)+50;
        slopeX=0;
        slopeY=(-50/time);
    end
end