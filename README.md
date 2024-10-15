# Exe_DJT.py manual


## About the project

Exe_DJT.py script is for calculating
* <p>the E&#8855e dynamic Jahn-Teller effect</p>
* <p>ZPL (zero phonon line) shift </p>

from <em>ab initio</em> calculations.

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/tbalu98/Jahn-Teller-effect
   ```
2. Install python packages
   ```sh
   pip3 install -r requirements.txt
   ```

3. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## usage:
The script expects a configfile in which you can specify your Jahn-Teller active system.
```bash
python3 Exe_DJT.py config_files/SnV_ZPL_shift_vasprunxml.cfg 
```
### config file example using vasprunxml
<p>In order to perform calculations you need to have at least two geometric configuration of your Jahn-Teller active system. The highly symmteric geometry, Jahn-Teller distorted geometry which has minimum energy and optionally the saddle point geometry. You can specify them in the configfile by vasprunxml files.</p>
<p>Config files are made up of sections. The 'DEFAULT' section contains data about the maximum number of vibrational quanta in both direction, the output prefix which used as the prefix of the output files' names. In the 'system_parameters' section you need to specify your vasprunxml files, intrinsic spin-orbit coupling and the orbital reduction factor.

```
[DEFAULT]
maximum_number_of_vibrational_quanta = 12
output_prefix = SnV_gnd
output_folder = results/SnV_results
input_folder = data/SnV_data

[system_parameters]
saddle_point_geometry = SnV_gnd_saddle_point.xml
global_minimum_geometry = SnV_gnd_C2h.xml
high_symmetry_geometry = SnV_gnd_D3d.xml
#intrinsic spin-orbit coupling in GHz:
intrinsic_spin-orbit_coupling = 2001
orbital_reduction_factor =  0.328


```

The eigenenergies, states and the theoretical results such as reduction factors will be presented in the <em>output_folder</em>.

### ZPL calculation using vasprunxml files

You can specify the ground and excited state of your system in order to calculate the ZPL shift. In this case you need to specify the magnetic field in the 'magnetic_field' section where you can define the direction of the field in terms of the geometry's basis vectors and the field strengths.</p>

```
[DEFAULT]
maximum_number_of_vibrational_quanta = 12
output_prefix = SnV_ZPL_shift
output_folder = results/SnV_results
input_folder = data/SnV_data
save_raw_parameters = true
[ground_state_parameters]
saddle_point_geometry = SnV_gnd_saddle_point.xml
global_minimum_geometry = SnV_gnd_C2h.xml
high_symmetry_geometry = SnV_gnd_D3d.xml
#intrinsic spin-orbit coupling in GHz:
intrinsic_spin-orbit_coupling = 2001
orbital_reduction_factor =  0.328

[excited_state_parameters]
saddle_point_geometry = SnV_ex_saddle_point.xml
global_minimum_geometry = SnV_ex_C2h.xml
high_symmetry_geometry = SnV_ex_D3d.xml
#intrinsic spin-orbit coupling in GHz:
intrinsic_spin-orbit_coupling = 23200
orbital_reduction_factor =  0.782

[magnetic_field]
#In Tesla
minimum = 0.0
maximum = 10.0
direction_vector = 1.0, 1.0, 1.0
step_number = 11

```

### ZPL calculation using .csv files

<p> By setting save_raw_parameters = true in the 'DEFAULT' field the script saves atomic coordinates to .csv files and generates a new .cfg file which contains additional information related to atoms and structure such as atomic mass, names and lattice vectors. The new configfile looks as following  </p>

```
[DEFAULT]
maximum_number_of_vibrational_quanta = 12
output_prefix = SnV_ZPL_shift
output_folder = results/SnV_results
input_folder = data/SnV_data
save_raw_parameters = false

[ground_state_parameters]
intrinsic_spin-orbit_coupling = 2001.0
orbital_reduction_factor = 0.328
high_symmetry_geometry = SnV_ZPL_shift_ground_state_parameters_high_symmetry_geometry.csv
high_symmetric_geometry_energy = -5368.30679265
global_minimum_geometry = SnV_ZPL_shift_ground_state_parameters_global_minimum_geometry.csv
global_minimum_energy = -5368.32839163
saddle_point_energy = -5368.32682965
saddle_point_geometry = SnV_ZPL_shift_ground_state_parameters_saddle_point_geometry.csv

[excited_state_parameters]
intrinsic_spin-orbit_coupling = 23200.0
orbital_reduction_factor = 0.782
high_symmetry_geometry = SnV_ZPL_shift_excited_state_parameters_high_symmetry_geometry.csv
high_symmetric_geometry_energy = -5366.13656085
global_minimum_geometry = SnV_ZPL_shift_excited_state_parameters_global_minimum_geometry.csv
global_minimum_energy = -5366.21970743
saddle_point_energy = -5366.21291581
saddle_point_geometry = SnV_ZPL_shift_excited_state_parameters_saddle_point_geometry.csv

[atom_structure_parameters]
masses_of_atoms = 118.71, 12.011
names_of_atoms = Sn, C
numbers_of_atoms = 1, 510
basis_vector_1 = 14.17860889, 0.0, 0.0
basis_vector_2 = 0.0, 14.17860889, 0.0
basis_vector_3 = 0.0, 0.0, 14.17860889

[magnetic_field]
minimum = 0.0
maximum = 10.0
step_number = 11
direction_vector = 1.0, 1.0, 1.0



```

### ZPL calculation from the parameters of Jahn-Teller interaction

```

[DEFAULT]
maximum_number_of_vibrational_quanta = 12
output_prefix = SiC_ZPL_shift
output_folder = results/SiC_PBE_510_results
input_folder = data/SiC_PBE_510_atoms
save_raw_parameters = false

[ground_state_parameters]
intrinsic_spin-orbit_coupling = 2001.0
orbital_reduction_factor = 0.328
high_symmetry_geometry = SiC_ZPL_shift_ground_state_parameters_high_symmetry_geometry.csv
high_symmetric_geometry_energy = -3834.2711012
global_minimum_geometry = SiC_ZPL_shift_ground_state_parameters_global_minimum_geometry.csv
global_minimum_energy = -3834.27177822
saddle_point_energy = -3834.27112245
saddle_point_geometry = SiC_ZPL_shift_ground_state_parameters_saddle_point_geometry.csv

[excited_state_parameters]
intrinsic_spin-orbit_coupling = 45616
orbital_reduction_factor = 0.782
high_symmetry_geometry = SiC_ZPL_shift_excited_state_parameters_high_symmetry_geometry.csv
high_symmetric_geometry_energy = -3833.28508322
global_minimum_geometry = SiC_ZPL_shift_excited_state_parameters_global_minimum_geometry.csv
global_minimum_energy = -3833.31181977
saddle_point_energy = -3833.31160279
saddle_point_geometry = SiC_ZPL_shift_excited_state_parameters_saddle_point_geometry.csv

[atom_structure_parameters]
masses_of_atoms = 12.011, 28.085
names_of_atoms = C, Si
numbers_of_atoms = 255, 255
basis_vector_1 = 17.51682281, 0.0, 0.0
basis_vector_2 = 0.0, 17.51682281, 0.0
basis_vector_3 = 0.0, 0.0, 17.51682281

[magnetic_field]
minimum = 0.0
maximum = 10.0
step_number = 11
direction_vector = 1.0, 1.0, 1.0



```




### Complex and real eigenstates

<p>The script is capable to save the eigenstates in 
complex basis ( e<sub>+</sub>, e<sub>-</sub> ), where the electronic states are the superpositions of the degenerate orbitals (e<sub>x</sub>, e<sub>y</sub>) such that e<sub>+</sub> = e<sub>x</sub>+ie<sub>y</sub> and 
e<sub>-</sub> = e<sub>x</sub>-ie<sub>y</sub>. You just need to set eigen_states option in the DEFAUL field to complex.</p>

```
eigen_states = complex
```