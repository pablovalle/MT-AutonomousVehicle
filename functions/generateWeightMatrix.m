function matrix=generateWeightMatrix()
    pointsReferences=importPointsReferences('Points-references.xlsx');
    matrix=zeros(size(pointsReferences,1));

    for i=1:size(matrix,1)
        row=pointsReferences(i,:);
        for j=1:size(matrix,2)
            is=isInto(j,row);
            if is==1
                matrix(i,j)=randi([1 20]);
                matrix(j,i)= matrix(i,j);
            end
        end
    end

end
