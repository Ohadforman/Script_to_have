function [vec1, vec2] = set_2_col_vec(filename, col1name, col2name, directory)

    % construct the full file path
    filepath = fullfile(directory, filename);
    
    % read the data from the file
    data = readmatrix(filepath);
    
    % extract the data from the first and second columns
    vec1 = data(:,1);
    vec2 = data(:,2);
    
    % assign the vectors to the specified variable names
    assignin('base', col1name, vec1);
    assignin('base', col2name, vec2);
    
end
