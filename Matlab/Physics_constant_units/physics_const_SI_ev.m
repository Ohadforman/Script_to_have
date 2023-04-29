% Define the units for each constant
units = struct();
units.h = 'J s';
units.hbar = 'J s';
units.G = 'm^3 kg^-1 s^-2';
units.c = 'm s^-1';
units.e = 'C';
units.me = 'kg';
units.mp = 'kg';
units.mn = 'kg';
units.kb = 'J K^-1';
units.R = 'J K^-1 mol^-1';
units.sigma = 'W m^-2 K^-4';
units.hc = 'J m';
units.NA = 'mol^-1';
units.mu0 = 'N A^-2';
units.eps0 = 'F m^-1';
units.Rinf = 'm^-1';
units.alpha = '';
units.k_e = 'N m^2 C^-2';
units.m_e_c2 = 'J';
units.m_p_c2 = 'J';
units.pi ='rad';

% Define the physical constants in SI units
const.h = 6.62607015e-34;      % Planck constant
const.hbar = const.h/(2*pi);  % Reduced Planck constant
const.G = 6.67430e-11;        % Gravitational constant
const.c = 299792458;          % Speed of light in vacuum
const.e = 1.602176634e-19;    % Elementary charge
const.me = 9.1093837015e-31;  % Electron mass
const.mp = 1.67262192369e-27; % Proton mass
const.mn = 1.67492749804e-27; % Neutron mass
const.kb = 1.380649e-23;      % Boltzmann constant
const.R = 8.314462618;        % Gas constant
const.sigma = 5.670374419e-8; % Stefan-Boltzmann constant
const.hc = const.h*const.c;   % Energy per photon of a photon with wavelength 1 meter
const.NA = 6.02214076e23;     % Avogadro's number
const.mu0 = 4*pi*1e-7;        % Vacuum permeability
const.eps0 = 1/(const.mu0*const.c^2); % Vacuum permittivity
const.Rinf = 10973731.568508; % Rydberg constant
const.alpha = 1/137.035999139; % Fine-structure constant
const.k_e = 8.9875517923e9;   % Coulomb constant
const.m_e_c2 = const.me*const.c^2; % Electron rest energy
const.m_p_c2 = const.mp*const.c^2; % Proton rest energy
const.pi=pi;
% Save the physical constants and units to a file
save('/Users/ohadformanair/Documents/Scripts/Matlab/Physics_constant_units/physical_constants.mat', 'const', 'units')


% Define the units for each constant in eV
units_eV = struct();
units_eV.h = 'eV s';
units_eV.hbar = 'eV s';
units_eV.G = 'm^3 kg^-1 s^-2 eV^-1';
units_eV.c = 'm s^-1';
units_eV.e = 'eV';
units_eV.me = 'eV/c^2';
units_eV.mp = 'eV/c^2';
units_eV.mn = 'eV/c^2';
units_eV.kb = 'eV K^-1';
units_eV.R = 'eV K^-1 mol^-1';
units_eV.sigma = 'W m^-2 K^-4';
units_eV.hc = 'eV m';
units_eV.NA = 'mol^-1';
units_eV.mu0 = 'N A^-2';
units_eV.eps0 = 'F m^-1';
units_eV.Rinf = 'm^-1';
units_eV.alpha = '';
units_eV.k_e = 'N m^2 C^-2 eV^-2';
units_eV.m_e_c2 = 'eV';
units_eV.m_p_c2 = 'eV';
units_eV.pi = 'rad';

% Define the physical constants in eV
const_eV.h = 4.1357e-15; % Planck constant
const_eV.hbar = 6.5821e-16; % Reduced Planck constant
const_eV.G = 7.4258e-29; % Gravitational constant
const_eV.c = 299792458; % Speed of light in vacuum
const_eV.e = 1.6022e-19; % Elementary charge
const_eV.me = 5.4858e-4; % Electron mass
const_eV.mp = 7.7240e-1; % Proton mass
const_eV.mn = 8.0713e-1; % Neutron mass
const_eV.kb = 8.6173e-5; % Boltzmann constant
const_eV.R = 8.3145/1.6022e-19; % Gas constant
const_eV.sigma = 5.6704e-8; % Stefan-Boltzmann constant
const_eV.hc = 1.9864e-25; % Energy per photon of a photon with wavelength 1 meter
const_eV.NA = 6.0221e23; % Avogadro's number
const_eV.mu0 = 1.2566e-6; % Vacuum permeability
const_eV.eps0 = 8.8542e-12; % Vacuum permittivity
const_eV.Rinf = 1.0974e7; % Rydberg constant
const_eV.alpha = 7.2974e-3; % Fine-structure constant
const_eV.k_e = 8.9876e9; % Coulomb constant
const_eV.m_e_c2 = 5.1097e5; % Electron rest energy
const_eV.m_p_c2 = 9.3827e8; % Proton rest energy
const_eV.pi = pi; % Value of pi
% Save the physical constants and units to a file
save('/Users/ohadformanair/Documents/Scripts/Matlab/Physics_constant_units/physical_constants_eV.mat', 'const_eV', 'units_eV')
