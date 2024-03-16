# Jahn-Teller-effect
Usage examples:

python Exe_JT_problem.py n l filename_1...filename_m -save_raw_pars

n is the maximum number of the lattice vibration's energy quantums
l is the energy of spin-orbit coupling

Specify the geometry of your system using vasprun.xml files

Optionally you can save the parameters that were read by the script from the vasprun.xml files.

It will create three or four .csv files.

The first one is the atomic_parameters.csv containing the atomic masses, names of the elements, basis vector coordinates, lattice energies.

The others contain the geometry


Examples:

Calculate second order Jahn-Teller interaction from three geometries and save raw parameters:

python Exe_JT_problem.py 12 1.0 SnV_D3d_vasprun.xml SnV_C2h_JT_vasprun.xml SnV_C2h_barrier_vasprun.xml -save_raw_pars

Calculate first order Jahn-Teller interaction from two geometries:

python Exe_JT_problem.py 12 1.0 SnV_D3d_vasprun.xml SnV_C2h_JT_vasprun.xml

Calculate second order Jahn-Teller interaction from previously saved raw parameters. These raw parameters can be modified by the user:

python Exe_JT_problem.py 12 1.0 par_df.csv symm_latt.csv JT_lattice.csv barrier_lattice.csv




