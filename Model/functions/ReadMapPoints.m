function pointsTable=ReadMapPoints()
    load('USCity.mat');
    k=1;
    points=zeros([1,2]);
    for i=1:size(data.RoadSpecifications,2)
        for j=1:size(data.RoadSpecifications(1,i).Centers,1)
            is=notInto(points,data.RoadSpecifications(1,i).Centers(j,1),data.RoadSpecifications(1,i).Centers(j,2));
            if is==0
                points(k,1)=data.RoadSpecifications(1,i).Centers(j,1);
                points(k,2)=data.RoadSpecifications(1,i).Centers(j,2);
                pointsTable(k,:)=table(data.RoadSpecifications(1,i).Centers(j,1),data.RoadSpecifications(1,i).Centers(j,2));
                k=k+1;
            end
        end   
    end
    pointsTable.Properties.VariableNames={'Xvalue','Yvalue'};
    writetable(pointsTable, 'MAP_POINTS.xlsx');
end



