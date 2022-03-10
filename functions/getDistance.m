function distance=getDistance(xRef,yRef )
    distance=0;
    for j=2:size(xRef,1)
       distance=distance+ sqrt(abs(xRef(j,1)-xRef(j-1,1))^2+abs(yRef(j,1)-yRef(j-1,1))^2);
    end
end