function [x,y]=rightCurve(points,i,rute,x,y)
    if i>2
        if yawCalculator(points(rute(1,i-1),1),points(rute(1,i-1),2),points(rute(1,i),1),points(rute(1,i),2))~= yawCalculator(points(rute(1,i-2),1),points(rute(1,i-2),2),points(rute(1,i-1),1),points(rute(1,i-1),2))
            psi=yawCalculator(points(rute(1,i-1),1),points(rute(1,i-1),2),points(rute(1,i),1),points(rute(1,i),2));
            psi2=yawCalculator(points(rute(1,i-2),1),points(rute(1,i-2),2),points(rute(1,i-1),1),points(rute(1,i-1),2));
            if psi==0 && psi2==pi*1.5
                y=-3;
                x=-3;
            elseif psi==pi*0.5 && psi2==0
                y=+3;
                x=-3;
            elseif psi==pi && psi2==pi*0.5
                y=+3;
                x=3;
            elseif psi==1.5*pi && psi2==pi
                y=-3;
                x=+3;
            end
        end
    end

end