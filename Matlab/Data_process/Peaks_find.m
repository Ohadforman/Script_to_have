function peak_find = Peaks_find(directory, filename)

% Load the data using set_2_col_vec.m 
[x_data, y_data] = set_2_col_vec(filename, 'frequency', 'power', directory);

%remove outliers
prctiles = prctile(y_data, [0.8 98.5]);
y_data(y_data < prctiles(1) | y_data > prctiles(2)) = NaN;


% Plot the data
plot(x_data, y_data);
xlabel('x');
ylabel('y');

% Ask the user for the desired number of peaks
num_peaks = 0;
while true
    num_peaks_input = input(sprintf('Enter the desired number of peaks (currently %d): ', num_peaks));
    if isempty(num_peaks_input) % use previous value if no input is given
        num_peaks_input = num_peaks;
    end
    num_peaks = num_peaks_input;

    % Find the peaks
    [pks, locs] = findpeaks(y_data);

    % Get the indices of the top num_peaks peaks
    [~, sorted_indices] = sort(y_data(locs), 'descend');
    peak_indices = locs(sorted_indices(1:num_peaks));

    % Get the coordinates of the top num_peaks peaks
    x_peaks = x_data(peak_indices);
    y_peaks = y_data(peak_indices);

    % Plot the data with the peaks marked
    figure;
    grid on
    plot(x_data, y_data);
    hold on;
    plot(x_peaks, y_peaks, 'ro');
    hold off;

    % Ask the user if the plot is acceptable
    response = input('Is the plot acceptable? [y/n]: ', 's');
    if strcmpi(response, 'y') % plot is acceptable, break out of loop
        break;
    end
end

peak_table = table(x_peaks, y_peaks, 'VariableNames', {'x coor peak','y coor peak'});
peak_table = sortrows(peak_table, 'x')
% Ask the user if they want to save the plot
response = input('Do you want to save the plot? [y/n]: ', 's');
if strcmpi(response, 'y')
    % Prompt for x and y limits, x label, y label, and title
    x_limits = input('Enter the x limits (e.g. [0 2]): ');
    y_limits = input('Enter the y limits (e.g. [-50 0]): ');
    x_label = input('Enter the x label: ', 's');
    y_label = input('Enter the y label: ', 's');
    plot_title = input('Enter the plot title: ', 's');
    filename = input('Enter the filename to save the plot (e.g. plot1): ', 's');
    % Save the plot
    xlim(x_limits);
    ylim(y_limits);
    xlabel(x_label);
    ylabel(y_label);
    title(plot_title);
    grid on
    saveas(gcf, fullfile(directory, [filename, '.png']));
end

% Ask the user if they want to save the table to a latex file
response_latex = input('Do you want to save the table to latex file? [y/n]: ', 's');
if strcmpi(response_latex, 'y')
    x_col_name = input('x colomn name?: ', 's');
    y_col_name = input('y colomn name?: ', 's');
    peak_table = table(x_peaks, y_peaks, 'VariableNames', {x_col_name,y_col_name});
    table2latex(peak_table,filename)
end


