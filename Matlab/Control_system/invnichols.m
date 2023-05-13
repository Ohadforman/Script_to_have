function [magout,phase,w] = invnichols(g)

%[magout,phase,w] = nichols(g);
nichols(g);

plot_handle = gca;
[nicgrid, nictext] = invnicchart(plot_handle);
axis([-270,0,-80,80]);
set(nictext, 'Visible', 'off');

title_handle = get(plot_handle, 'Title');
if(strcmp(get(title_handle, 'String'),''))
    if numel(nictext) >= 12 % add check for number of elements
        for i = 1:12
            position = get(nictext(i), 'Position');
            position(2) = -1 * position(2);
            set(nictext(i), 'Position', position);
        end

        set(nictext, 'Visible', 'on');
    end
    
    title('');
    set(title_handle, 'String', 'Inverse Nichols Chart');
end
