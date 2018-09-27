function [newList] = interpret_image_list(oldList)
% takes an old stimulus list in cell-array form and returns an equivalent
% list column with stimulus image file names in the new format

nTrials = size(oldList,1);
fprintf('List contains %d trials.\n',nTrials);
newList = cell(nTrials,1);

% loop over trials
for i = 1:nTrials
    thisEntry = oldList{i};
    
    % identify the stimulus type
    if any(strfind(thisEntry,'Faces')) || strcmp(thisEntry(2),'f')
        thisType = 'Faces';
    elseif any(strfind(thisEntry,'Houses')) || strcmp(thisEntry(2),'h')
        thisType = 'Houses';
    else
        keyboard
        error('trial type not identified for entry: %s',thisEntry);
    end
    
    % identify the stimulus image file
    imgID = upper(thisEntry(2:4));
    thisFile = fullfile('stimuli',thisType,[imgID,'.pict.jpg']);
    
    % add it to the list
    newList{i} = thisFile;
    
end % loop over trials

