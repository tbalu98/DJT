# Jahn-Teller-effect

## usage:

python Exe_JT_problem_cfg_file.py config_file.cfg -save_raw_pars

You have to specify your vasprun.xml files in a .cfg config file.
You may add spin-orbit coupling and electric field interaction to your system.

### config file example, if you use vasprun.xml:

[DEFAULT]<br />
maximum_order_of_harmonic_oscillator = 12<br />
calculation_name = SnV_ground_state_calc<br />
<br />
[vasprun.xml_files]<br />
symmetric_lattice = SnV_D3d_vasprun.xml<br />
barrier_lattice = SnV_C2h_JT_vasprun.xml<br />
Jahn-Teller_lattice = SnV_C2h_barrier_vasprun.xml<br />
<br />
[spin_orbit_coupling]<br />
lambda = 1.0<br />
<br />

[electric_field]<br />
<br />
E_x = 1.0<br />
E_y = 1.0<br />

## -save_raw_pars optional field

Using the -save_raw_pars optional field the script will save the essential data about the atoms in a .cfg config file.

### Generated atom parameters:

[atom_names]<br />
atom_1_name = Sn<br />
atom_2_name = C<br />
<br />
[atom_masses]<br />
atom_1_mass = 118.71<br />
atom_2_mass = 12.011<br />
<br />
[lattice_energies]<br />
symm_lattice_energy = -5368.30679265<br />
jt_lattice_energy = -5368.32682965<br />
barrier_lattice_energy = -5368.32839163<br />
<br />
[basis_vectors]<br />
basis_vector_1_x = 14.17860889<br />
basis_vector_1_y = 0.0<br />
basis_vector_1_z = 0.0<br />
basis_vector_2_x = 0.0<br />
basis_vector_2_y = 14.17860889<br />
basis_vector_2_z = 0.0<br />
basis_vector_3_x = 0.0<br />
basis_vector_3_y = 0.0<br />
basis_vector_3_z = 14.17860889<br />

### Saves the geometry

It also saves atomic positions with regards to the geometries in separate .csv files. You can use these .cfg and .csv files, to run new calculations, and freely modify data, for instance atomic mass, position or lattice energy.

The first few lines of such file:

index,x_coordinates,y_coordinates,z_coordinates,atom_name<br />
0,-0.0,-0.0,0.0,Sn<br />
1,0.04151139,0.90046589,0.90046589,C<br />
2,0.95848863,0.09953411,0.09953411,C<br />
3,0.90046589,0.90046589,0.04151139,C<br />
...

### Config file example, if you generated .csv geometry files from your vasprun.xmls:

['DEFAULT']<br />
maximum_order_of_harmonic_oscillator = 12<br />
<br />
[.csv_files]<br />
atom_parameters = atom_parameters.cfg<br />
symmetric_lattice = symm_latt.csv<br />
barrier_lattice = barrier_lattice.csv<br />
Jahn-Teller_lattice = JT_lattice.csv<br />
<br />
[spin_orbit_coupling]<br />
lambda = 1.0<br />

[electric_field]<br />
<br />
E_x = 1.0<br />

E_y = 1.0<br />
