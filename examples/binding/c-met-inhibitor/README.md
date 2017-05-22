# Absolute binding free energy calculations of c-Met kinase receptor and inhibitor

## Description

In this example, we compute the absolute binding free energy of the an inhibitor to c-Met Kinase. 
These structures were kindly provided by the Merck Serono Research & Development and Merck KGaA group and uploaded with 
permission.
 
Please see the [their paper](http://www.sciencedirect.com/science/article/pii/S0960894X15000955) for more detail

    Identification and optimization of pyridazinones as potent and selective c-Met kinase inhibitors
    Dorsch, D. et. al, Bioorganic & Medicinal Chemistry Letters, 25, 7, 2015
    10.1016/j.bmcl.2015.02.002
    
The ligand in this case is compound 22 (MSC2156119) from the cited paper.
 
vdw        : '800R3'
vdw_cutoff : 10.00
ele        : 'GB'
ele_cutoff : 15.00
d_in       : 1.00
d_out      : 80.00
T          : 300.00
ionC       : 0.10
pH = 10.00
 
## Running the example

### Explicit solvent

To run the simulation in explicit solvent (TIP3P):
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
```bash
yank cleanup --store=output
```

## Manifest
* `explicit.yaml` - YANK YAML input file for explicit solvent free energy calculation
* `implicit.yaml` - YANK YAML input file for implicit solvent free energy calculation
* `run-explicit.sh` - bash script for running explicit solvent calculation
* `run-torque-explicit.sh` - example Torque batch queue script for running explicit solvent calculation in parallel over multiple GPUs
* `run-torque-implicit.sh` - example Torque batch queue script for running implicit solvent calculation in parallel over multiple GPUs
* `run-lsf-implicit.sh` - example LSF batch queue script for running explicit solvent calculation in parallel over multiple GPUs
* `run-lsf-explicit.sh` - example LSF batch queue script for running explicit solvent calculation in parallel over multiple GPUs
* `input/` - initial protein and ligand structure files

### Notes on the cluster scripts
The Torque and LSF scripts have been modified to work on the High Performance Computing clusters at Memorial 
Sloan-Kettering Cancer Center. The Slrum scripts have been modified to run on the Merck KGaA GPU cluster. 
You may need to make small changes to the respective `#PBS`, `#BSUB`, or `#SBATCH` directives to work on your cluster.

