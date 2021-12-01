function [travel, rute]=generateWay(source,destination,al)
    addpath('dijkstra');
    points=ReadMapPoints();
    points=table2array(points);
    matrix=generateWeightMatrix();
    if source==destination && destination>=49
        destination=destination-3;
    elseif al==1 && destination<=49
        destination=destination+3;
    elseif al==1 && destination>=49
        destination=destination-3;
    end
    
    [cost, rute]=dijkstra(matrix,source,destination);

    i=size(rute,2);
    z=0;
    a=0;
    [x,y]=calculoDesfase(points(rute(1,size(rute,2)),1),points(rute(1,size(rute,2)-1),1),points(rute(1,size(rute,2)),2),points(rute(1,size(rute,2)-1),2));
    travel(1,1)=points(source,1)+x;
    travel(1,2)=points(source,2)+y;
    while i>1
        way(1,1)=abs(abs(points(rute(1,i),1))-abs(points(rute(1,i-1),1)));
        way(1,2)=abs(abs(points(rute(1,i),2))-abs(points(rute(1,i-1),2)));
        [x,y]=calculoDesfase(points(rute(1,i),1),points(rute(1,i-1),1),points(rute(1,i),2),points(rute(1,i-1),2));
        if rute(1,i-1)==39
            z=z-1;
            a=1;
            travel(z*10+10+1+a,1)=points(rute(1,i-1),1)+x;
            travel(z*10+10+1+a,2)=points(rute(1,i-1),2)+y;
            i=i-1;
            z=z+1;
        else
            for j=1:9
                travel(z*10+j+1+a,1)=newPoint(points(rute(1,i),1),points(rute(1,i-1),1),way(1,1),j)+x;
                travel(z*10+j+1+a,2)=newPoint(points(rute(1,i),2),points(rute(1,i-1),2),way(1,2),j)+y;
            end
            [x,y]=rightCurve(points,i,rute,x,y);
            travel(z*10+10+1+a,1)=points(rute(1,i-1),1)+x;
            travel(z*10+10+1+a,2)=points(rute(1,i-1),2)+y;
            i=i-1;
            z=z+1;
        end
    end   

end
