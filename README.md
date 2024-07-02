# Jahn-Teller-effect

## usage:

python Exe_JT_problem.py config_files_examples/PbV_gnd_JT_xml_config_EM_field.cfg -save_raw_pars

You have to specify your vasprun.xml files in a .cfg config file.
You may add spin-orbit coupling and electric field interaction to your system.

### config file example, if you use vasprun.xml:


[DEFAULT]<br/>
maximum_order_of_harmonic_oscillator = 12<br/>
calculation_name = PbV_ground_state_EM_field_1<br/>
data_folder = PbV_data<br/>
results_folder = PbV_results<br/>

<br/>

[vasprun.xml_files]<br/>
symmetric_lattice = PbV_D3d_vasprun.xml<br/>
barrier_lattice = PbV_C2h_barrier_vasprun.xml<br/>
Jahn-Teller_lattice = PbV_C2h_JT_vasprun.xml<br/>

<br/>

[spin_orbit_coupling]<br/>
lambda = 34.574180<br/>
gL =  0.328<br/>
calc_LzSz = 50<br/>

<br/>

[electric_field]<br/>

<br/>

E_x = 1.0<br/>
E_y = 0.0<br/>

<br/>

[magnetic_field]<br/>
<br/>
B_x = 0.0<br/>
B_y = 0.5<br/>
B_z = 0.2<br/>

Give the quantities in terms of meV.
The data_folder contains the vasprun.xml files. The results (eigen energies, eigen vectors, expectation value of the spin-orbit coupling) will be saved in the results_folder. In the calc_LzSz option you can specify the number of eigen vectors which LzSz expectation value should be calculated.


### -save_raw_pars optional field

Using the -save_raw_pars optional field the script will save the essential data about the atoms in a .cfg config file into the data_folder.

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

It saves atomic positions with regards to the geometries in separate .csv files. You can use these .cfg and .csv files, to run new calculations, and freely modify data, for instance atomic mass, position or lattice energy.

The first few lines of such file:

index,x_coordinates,y_coordinates,z_coordinates,atom_name<br />
0,-0.0,-0.0,0.0,Sn<br />
1,0.04151139,0.90046589,0.90046589,C<br />
2,0.95848863,0.09953411,0.09953411,C<br />
3,0.90046589,0.90046589,0.04151139,C<br />
...

### Config file example, if you generated .csv geometry files from your vasprun.xmls:

[DEFAULT]<br/>
maximum_order_of_harmonic_oscillator = 12<br/>
calculation_name = PbV_ground_state<br/>
data_folder = PbV_data<br/>
results_folder = PbV_results<br/>

<br/>

[.csv_files]<br/>
atom_parameters = PbV_ground_state_atom_parameters.cfg<br/>
symmetric_lattice = PbV_ground_state_symmetric_lattice.csv<br/>
barrier_lattice = PbV_ground_state_barrier_lattice.csv<br/>
Jahn-Teller_lattice = PbV_ground_state_JT_lattice.csv<br/>

<br/>

[spin_orbit_coupling]<br/>
lambda = 34.574180<br/>
gL =  0.328<br/>



### ZPL shift:
The ZPL_shift.py script can calculate zero-phonon line splitting of the four lowest energy state. You need to run python ZPL_shift.py config_files_examples/PbV_ZPL_config_xml.cfg command.
In order to calculate the ZPL shift, you need to have the ground and excited state's vasprun.xml files that contain the geometry of the system. 
PbV_ZPL_config_xml.cfg in the config_files_examples folder examplifies an ZPL config file.

[DEFAULT]<br/>
ground_state_cfg = PbV_gnd_JT_xml_config.cfg<br/>
excited_state_cfg = PbV_ex_JT_xml_config.cfg<br/>
cfg_data_folder = config_files_examples<br/>
results_folder = PbV_results<br/>
calculation_name = PbV ZPL shift<br/>
[magnetic_field]<br/>
B_min = 0.0<br/>
B_max = 7.0<br/>
step_num = 10<br/>

In this config file you need to specify the config files of the ground and excited state (PbV_gnd_JT_csv_config.cfg, PbV_ex_JT_csv_config.cfg). These files contains the name of the necessary vasprun.xml files, and other attributes in order to construct the Hamiltonian operators of the systems. You may also use .csv files that you have previously generated, using the Exe_JT_problem.py script with the -save_raw_pars optional field.

cfg_data_folder is the folder of the config files.

You need to specify the minimum and maximum magnetic field, and the number of field strengths that has to be evaluated.

The results will be shown in the results_folder. You will get 4 .csv files that contain the energy differences of the ground and excited state with respect to the magnetic field strength.
