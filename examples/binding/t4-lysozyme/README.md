# Binding to T4 lysozyme L99A. p-xylene, binders, and non-binders

## Tutorial

There are several tutorials contained in this folder.

For the introductory p-xylene binding in TIP3P water tutorial, please see: 
[our guide on the YANK web page](http://getyank.org/examples) *PLACEHOLDER*

For the example where we bind all binders and non-binders from two files 
with SMILES string, please see:
[our guide on the YANK web page](http://getyank.org/examples) *PLACEHOLDER*.
This particular example requires the OpenEye Toolkits 
to process the SMILES strings and makes use of the `!Combinatorial` argument.

## Example Manifest

### p-xylene files 
* `p-xylene-explicit.yaml` - YAML script for binding p-xylene in explicit TIP3P water 
* `p-xylene-implicit.yaml` - YAML script for binding p-xylene in implicit solvent.
* `run-p-xylene-explicit.sh` - Run the p-xylene binding example in explicit water.
* `run-p-xylene-implicit.sh` - Run the p-xylene binding example in implicit solvent.
* `run-torque-p-xylene-explicit.sh` - Run the p-xylene binding example in explicit water on a torque cluster. May require tweaking for your cluster.
* `run-torque-p-xylene-implicit.sh` - Run the p-xylene binding example in implicit solvent on a torque cluster. May require tweaking for your cluster.
* `input/ligand.tripos.mol2` - TRIPOS MOL2 file for para-xylene

### all-ligands files 
* `all-ligands-explicit.yaml` - YAML script for binding all-ligands in explicit TIP3P water 
* `all-ligands-implicit.yaml` - YAML script for binding all-ligands in implicit solvent.
* `run-all-ligands-explicit.sh` - Run the all-ligands binding example in explicit water.
* `run-all-ligands-implicit.sh` - Run the all-ligands binding example in implicit solvent.
* `run-torque-all-ligands-explicit.sh` - Run the all-ligands binding example in explicit water on a torque cluster. May require tweaking for your cluster.
* `run-torque-all-ligands-implicit.sh` - Run the all-ligands binding example in implicit solvent on a torque cluster. May require tweaking for your cluster.
* `input/L99A-binders.csv` - CSV file containing multiple known binders for T4 Lysozyme
* `input/L99-non-binders.csv` - CSV file containing multiple known non-binders for T4 Lysozyme

### Other Files
* `input/receptor.pdbfixer.pdb` - T4 Lysozyme L99A mutant. This has been pre-processed through PDBFixer. 
* `input/setup-protein.sh` - Regenerate the protein through PDBFixer.


## Running the simulations

### p-xylene binding 

This example uses mol2 files for both the ligand and the receptor to compute the free energy of binding 
in explicit (or implicit water)

Set up the simulation to alchemically decouple p-xylene from T4-Lysozyme, putting all the output files in `p-xylene-out/`:
```bash
$ sh run-p-xylene-explicit.sh
```

Clean up and delete all simulation files:
```bash
yank cleanup --store=p-xylene-out
```

Replace files with their appropriate implicit name for implicit solvent.

### "All Ligands" binding

This example uses CSV file to construct ligands from SMILES through the 
OpenEye Toolkits. Note that this example will take a long time to run 
due to the size of the binder/non-binder library.

This example takes advantage of the `!Combinatorial` command to setup and 
run multiple different simulations back to back to back. This lets you run 
all the molecules from a single command and YAML file

Set up the simulation to alchemically decouple p-xylene from T4-Lysozyme, putting all the output files in `all-ligands-out/`:
```bash
$ sh run-all-ligands-explicit.sh
```

Clean up and delete all simulation files:
```bash
yank cleanup --store=all-ligands-out
```

Replace files with their appropriate implicit name for implicit solvent.