# Set up p-xylene binding to T4 lysozyme L99A using AmberTools

## Rebuilding files from scratch

This section covers a how-to for generating the same input files that 
came bundled with these examples. 

### Recreating the Protein:

Run `setup-protein.sh`. Uses [PDBFixer](https://github.com/pandegroup/pdbfixer) 
(also available through the `omnia` conda channel, just like YANK is!)

### Recreating the p-xylene ligand

Change either `*.yaml` file in this example. Change 
`filepath: input/ligand.tripos.mol2` to `name: p-xylene`.

This uses the OpenEye Toolkit build the ligand on the fly. If you need 
the physical file, let YANK setup the simulation and then find the 
file in the `setup` directory of YANK's output directory.