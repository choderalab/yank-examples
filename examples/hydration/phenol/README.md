# Hydration Free Energy of Phenol

This example computes the hydration free energy of phenol in implicit 
and explicit solvent. 
This is a simple example that is designed to walk you through setting up 
a hydration free energy calculation in YANK.

## Tutorial

For a step-by-step walk through of using this example, please see 
[our phenol hydration tutorial](http://getyank.org/latest/examples/hydration-phenol-explicit.html).

## Running the simulation

Explicit solvent
```bash
yank script --yaml=explicit.yaml
```

Implicit solvent
```bash
yank script --yaml=implicit.yaml
```

Clean up and delete all simulation files:
```bash
yank cleanup --store=output
```
