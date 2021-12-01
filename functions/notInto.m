function ret=notInto(points,x,y)
i=1;
ret=0;
    while i<=size(points,1) && ret==0
        if points(i,1)==x && points(i,2)==y
            ret=1;
        end
        i=i+1;
    end
end