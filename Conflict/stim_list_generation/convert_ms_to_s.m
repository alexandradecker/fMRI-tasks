function [newCol] = convert_ms_to_s(oldCol)
% for ITIs stored in a cell array of strings, converts units from ms to s

nTrials = size(oldCol,1);
newCol = cell(size(oldCol));
for i = 1:nTrials
    itiVal = str2double(oldCol{i});
    newCol{i} = sprintf('%1.3f',itiVal/1000);
end

