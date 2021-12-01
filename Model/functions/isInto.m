function is= isInto(num, row)
i=1;
is=0;
while i<=size(row,2) && is==0
    if num== row(1,i)
        is=1;
    end
    i=i+1;
end
end