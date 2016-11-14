# Hydration free energy of the FreeSolv Database (reduced)

## Tutorial

For a walk through of the files in this example, and running it, please see 
[our guide on the YANK web page](http://getyank.org/latest/examples/freesolv-imp-exp.html)

## Description

This computes hydration free energies frm a subset of the FreeSolv 
database. Molecules are constructed from their SMILES string (through 
the OpenEye Toolkit) and both implicit and explicit simulations are run 
from single YAML file through the `!Combinatorial` argument.

This example is not meant to introduce anything new, but instead to show 
that even very complex ideas, like free energy of a database, are not 
very hard to set up in YANK, once you understand the basics from the 
other examples.

## Usage

## Running the simulation.

Set up the simulation to alchemically decouple p-xylene from T4-Lysozyme, putting all the output files in `output/`:
```bash
yank script --yaml=yank.yaml
```

Clean up and delete all simulation files:
```bash
yank cleanup --store=output
```

