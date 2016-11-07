# Binding multiple ligands to T4 lysozyme L99A in separate simulations

## Tutorial

For a step-by-step walk through of using this example, please see 
[our guide on the YANK web page](http://getyank.org/examples) *PLACEHOLDER*

## Description

This example looks at a series of binders and non-binders for L99A mutant 
of T4 lysozyme. This particular example requires the OpenEye Toolkits 
to process the SMILES strings.

This example also makes use of the `!Combinatorial` argument.

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

