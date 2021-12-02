function linecount = fcountlines(filename)
%FCOUNTLINES Count the lines in the given file. Returns -1 if file cannot
%be opened.
linecount = 0;
fid=fopen(filename);
if fid == -1
    linecount = -1;
    return;
end
while true
    if ~ischar(fgetl(fid)), break, end
    linecount = linecount + 1;
end
fclose(fid);
end
