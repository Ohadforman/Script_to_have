function [value, units] = get_constant_value_units(constant, unitSystem)
% Get the value and units of a physical constant in the specified unit system

% Load the appropriate list of constants and units
if strcmp(unitSystem, 'SI')
    load('/Users/ohadformanair/Documents/Scripts/Matlab/Physics_constant_units/physical_constants.mat', 'const', 'units');
elseif strcmp(unitSystem, 'eV')
    load('/Users/ohadformanair/Documents/Scripts/Matlab/Physics_constant_units/physical_constants_eV.mat', 'const_eV', 'units_eV');
else
    error('Invalid unit system. Must be ''SI'' or ''eV''.');
end

% Get the value and units of the requested constant
if strcmp(unitSystem, 'SI')
    if isfield(const, constant)
        value = const.(constant);
        units = units.(constant);
    else
        error('Invalid constant name.');
    end
elseif strcmp(unitSystem, 'eV')
    if isfield(const_eV, constant)
        value = const_eV.(constant);
        units = units_eV.(constant);
    else
        error('Invalid constant name.');
    end
end

end
