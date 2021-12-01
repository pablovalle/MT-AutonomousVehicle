function createNewScenarioDeg(refX,refY,deg)
    load('USCity.mat');
    for i=1:size(data.RoadSpecifications,2)
        for j=1:size(data.RoadSpecifications(1,i).Centers,1)
            data.RoadSpecifications(1,i).Centers(j,1)=data.RoadSpecifications(1,i).Centers(j,1)*cosd(deg)-data.RoadSpecifications(1,i).Centers(j,2)*sind(deg);
            data.RoadSpecifications(1,i).Centers(j,2)=data.RoadSpecifications(1,i).Centers(j,1)*sind(deg)+data.RoadSpecifications(1,i).Centers(j,2)*cosd(deg);
        end
    end
    for i=1: size(refX,1)
        refX(i,1)=refX(i,1)*cosd(deg)-refY(i,1)*sind(deg);
        refY(i,1)=refX(i,1)*sind(deg)+refY(i,1)*cosd(deg);
    end

    save('USCityDeg.mat','data','tag','refX','refY');
end