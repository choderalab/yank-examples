# p-xylene binding to T4 lysozyme L99A in TIP3P solvent with reaction-field electrostatics example

## Description

The ligand is parameterized using the GAFF forcefield with the AM1-BCC charge model.

The receptor (taken from 181L.pdb) is parameterized with the AMBER parm99sb-ildn forcefield.

The mbondi2 radii are used, with OBC GBSA in YANK.

## Usage

### Set up the system from scratch (not necessary unless source PDB or ligand files are modified):
```bash
./setup.sh
```

## Running the simulation.

Set up the simulation to alchemically decouple p-xylene from T4-Lysozyme, putting all the output files in `output/`:
```bash
yank script --yaml=yank.yaml
```

Clean up and delete all simulation files:
```bash
yank cleanup --store=output
```

