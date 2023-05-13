function live_plot(func)
%live_plot - plots a function of the parameter t live in time
%define for eample: func = @(t)10*exp(-t/10)
%func - function of t to plot live

% set up figure
fig = figure;
hold on

% convert function handle to string
func_str = func2str(func);

% create LaTeX string for title
title_str = ['$y=' func_str '$'];

% set initial limits of the x-axis
xlim([0, 2])

% iterate until user stops
while ishandle(fig)
    % initialize min and max values of y
    y_min = 0;
    y_max = 1;

    % iterate through time
    for t = 0:0.01:Inf
        % evaluate function
        y = func(t);

        % update min and max values of y
        y_min = min(y_min, y);
        y_max = max(y_max, y);

        % plot point
        plot(t, y, 'ro', 'MarkerSize', 2)

        % set title to LaTeX string
        title(title_str, 'Interpreter', 'latex',FontSize=16)

        % set x-axis label
        xlabel('time')

        % set y-axis limits
        y_range = y_max - y_min;
        ylim([y_min - 0.05*y_range, y_max + 0.05*y_range])

        % set x-axis limit based on current time
        xlim([0, t+2])

        % pause to show live plot
        pause(0.01)
        
        % check if figure is still valid
        if ~ishandle(fig)
            break
        end
    end
end

end
