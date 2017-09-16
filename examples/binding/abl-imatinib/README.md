# Absolute binding free energy calculations of imatinib binding to Abl kinase

## Description

In this example, we compute the absolute binding free energy of the three dominant protonation states of imatinib in solvent at pH 7.4 to Abl kinase.
Note that these free energies are not combined into an overall free energy of binding; this simply illustrates the sensitivity of the binding free energy to choice of ligand protonation state.

## Running the example

### Explicit solvent

To run the simulation in explicit solvent (TIP4P-EW):
```bash
yank script --yaml=explicit.yaml
```

### Implicit solvent

To run the simulation in implicit solvent (OBC GBSA):
```bash
yank script --yaml=implicit.yaml
```

### Cleaning up
To clean up and delete all simulation files:
```
yank cleanup --store=output
```

## Manifest
* `explicit.yaml` - YANK YAML input file for explicit solvent free energy calculation
* `implici.yaml` - YANK YAML input file for implicit solvent free energy calculation
* `run-explicit.sh` - bash script for running explicit solvent calculation
* `run-implicit.sh` - bash script for running implicit solvent calculation
* `run-torque-explicit.sh` - example Torque batch queue script for running explicit solvent calculation in parallel over multiple GPUs
* `run-torque-implicit.sh` - example Torque batch queue script for running implicit solvent calculation in parallel over multiple GPUs
* `run-lsf-explicit.sh` - example LSF batch queue script for running explicit solvent calculation in parallel over multiple GPUs
* `run-lsf-implicit.sh` - example LSF batch queue script for running implicit solvent calculation in parallel over multiple GPUs
* `input/` - initial protein and ligand structure files

