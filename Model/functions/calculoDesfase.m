function [x,y]=calculoDesfase(source_X, destination_X,source_Y,destination_Y)

    if source_Y<destination_Y
        x=2;
        y=0;
    elseif source_Y>destination_Y
        x=-2;
        y=0;
    elseif source_X<destination_X
        x=0;
        y=-2;
    else
        x=0;
        y=2;
    end
    
end