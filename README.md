# Jahn-Teller-effect

## usage:

python Exe_JT_problem_cfg_file.py config_file.cfg -save_raw_pars

You have to specify your vasprun.xml files in a .cfg config file.
You may add spin-orbit coupling and electric field interaction to your system.

### config file example, if you use vasprun.xml:

['DEFAULT']
maximum_order_of_harmonic_oscillator = 12

[vasprun.xml_files]
symmetric_lattice = SnV_D3d_vasprun.xml
barrier_lattice = SnV_C2h_JT_vasprun.xml
Jahn-Teller_lattice = SnV_C2h_barrier_vasprun.xml

[spin_orbit_coupling]
lambda = 1.0


[electric_field]

E_x = 1.0
E_y = 1.0

## -save_raw_pars optional field

Using the -save_raw_pars optional field the script will save the essential data about the atoms in a .cfg config file.

### Generated atom parameters:

[atom_names]
atom_1_name = Sn
atom_2_name = C

[atom_masses]
atom_1_mass = 118.71
atom_2_mass = 12.011

[lattice_energies]
symm_lattice_energy = -5368.30679265
jt_lattice_energy = -5368.32682965
barrier_lattice_energy = -5368.32839163

[basis_vectors]
basis_vector_1_x = 14.17860889
basis_vector_1_y = 0.0
basis_vector_1_z = 0.0
basis_vector_2_x = 0.0
basis_vector_2_y = 14.17860889
basis_vector_2_z = 0.0
basis_vector_3_x = 0.0
basis_vector_3_y = 0.0
basis_vector_3_z = 14.17860889

### Saves the geometry

It also saves atomic positions with regards to the geometries in separate .csv files. You can use these .cfg and .csv files, to run new calculations, and freely modify data, for instance atomic mass, position or lattice energy.

The first few lines of such file:

index,x_coordinates,y_coordinates,z_coordinates,atom_name
0,-0.0,-0.0,0.0,Sn
1,0.04151139,0.90046589,0.90046589,C
2,0.95848863,0.09953411,0.09953411,C
3,0.90046589,0.90046589,0.04151139,C
...

### Config file example, if you generated .csv geometry files from your vasprun.xmls:

['DEFAULT']
maximum_order_of_harmonic_oscillator = 12

[.csv_files]
atom_parameters = atom_parameters.cfg
symmetric_lattice = symm_latt.csv
barrier_lattice = barrier_lattice.csv
Jahn-Teller_lattice = JT_lattice.csv

[spin_orbit_coupling]
lambda = 1.0

[electric_field]

E_x = 1.0

E_y = 1.0
