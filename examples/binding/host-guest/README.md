# host-guest system: cucurbit[7]uril with guest molecule B2

This example computes the binding affinity of host and guest molecules in an implicit solvent model.

A Flat Bottom restraint is used to keep the two molecules from drifting far away from each other. 
An argument can be made for a Harmonic Restraint instead, but due to the 
symmetric nature of where the guest can reside in this host, 
we choose to use Flat Bottom so the ligand can better explore the 
host.

Files acquired from [the AMBER tutorial of the same system](http://ambermd.org/tutorials/advanced/tutorial21/)

## Tutorial

For a step-by-step walk through of using this example, please see 
[our guide on the YANK web page](http://getyank.org/examples) *PLACEHOLDER*

## Running the simulation.

## Running the simulation.

Set up the simulation to alchemically decouple p-xylene from cucurbit[7]uril, 
putting all the output files in `hgoutput/`:

```bash
yank script --yaml=yank.yaml
```

Clean up and delete all simulation files:
```bash
yank cleanup --store=output
```
