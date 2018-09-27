function [] = remake_lists()

% directories for the old and new versions of the lists
oldListDir = 'previous_lists';
newListDir = 'new_lists';

% identifiers for the four image positions
positions = {'north', 'south', 'west', 'east'};

% experimental blocks (each with its own variant of the stimulus lists)
blockIDs = {'A', 'AA', 'B', 'BB', 'DemoA', 'DemoB'};
nBks = numel(blockIDs);

% loop over blocks
% (each block has its own set of lists)
for bIdx = 1:nBks
    thisBlock = blockIDs{bIdx};
    fprintf('Processing block %s\n',thisBlock);
    
    % get the list column for each of the four image positions
    fprintf('Reading stimulus image lists...\n');
    for pIdx = 1:numel(positions)
        thisPos = positions{pIdx};
        pattern = ['bold_',thisBlock,'_*',thisPos,'.lst'];
        d = dir(fullfile(oldListDir,pattern));
        assert(numel(d)==1,'Old list file not uniquely identified');
        listFile = fullfile(oldListDir,d.name);
        listContents = read_list(listFile); % image files in old format
        col_img.(thisPos) = interpret_image_list(listContents); % image files in new format
    end
    
    % get the list column for ITI
    pattern = ['bold_',thisBlock,'_ITI.lst'];
    d = dir(fullfile(oldListDir,pattern));
    assert(numel(d)==1,'Old list file not uniquely identified');
    listFile = fullfile(oldListDir,d.name);
    iti_in_ms = read_list(listFile); % ITI values in ms
    col_iti = convert_ms_to_s(iti_in_ms); % ITI values converted to s
    
    % get the list column for correct response
    pattern = ['bold_',thisBlock,'_target*response.lst'];
    d = dir(fullfile(oldListDir,pattern));
    assert(numel(d)==1,'Old list file not uniquely identified');
    listFile = fullfile(oldListDir,d.name);
    col_corrResp = read_list(listFile); % correct response values
    
    % determine the target dimension (constant within each block)
    if any(strfind(d.name,'target_NS'))
        targDim = 'NS';
    elseif any(strfind(d.name,'target_WE'))
        targDim = 'WE';
    else
        error('target dimension not idenfied from filename: %s',d.name);
    end
    nTrials = size(col_corrResp,1);
    col_targDim = repmat({targDim},nTrials,1); % create a constant column
    
    % concatenate columns
    newListArray = [col_img.north, col_img.south, col_img.west, col_img.east,...
        col_iti, col_corrResp, col_targDim];
    % add column headers
    trialHeaders = {'imgNorth', 'imgSouth', 'imgWest', 'imgEast',...
        'ITI', 'correctResponse', 'targetDimension'};
    newListArray = [trialHeaders; newListArray]; %#ok<AGROW>
    
    % write out the file
    outfname = fullfile(newListDir,['trialList_',thisBlock,'.csv']);
    fprintf('Writing file: %s\n\n',outfname);
    fid = fopen(outfname,'w');
    newListArray = newListArray'; % transpose for output
    fprintf(fid,'%s,%s,%s,%s,%s,%s,%s\n',newListArray{:});
    fclose(fid);
    
end % loop over blocks



