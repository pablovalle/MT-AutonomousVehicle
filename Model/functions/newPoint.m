function point= newPoint(source,destination,distance,iteration)

    if source<destination
        point=source+(distance*iteration/10);
    elseif source>destination
        point=source-(distance*iteration/10);
    else
        point=source;
    end
end