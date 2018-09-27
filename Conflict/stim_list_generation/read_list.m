function [list_contents] = read_list(fname)
% loads the contents of an old list to a cell array

fid = fopen(fname,'r');
finished = false;
list_contents = {};
while ~finished
    thisLine = fgetl(fid);
    if isnumeric(thisLine) && thisLine==(-1)
        finished = true;
        continue;
    end
    list_contents{end+1,1} = thisLine;
end


