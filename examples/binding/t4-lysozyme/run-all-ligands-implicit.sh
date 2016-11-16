#!/bin/bash

#
# multiple ligands binding to T4 lysozyme L99A example run script (serial mode)
#

# Run the simulation
echo "Running simulation..."
yank script --yaml=all-ligands-implicit.yaml

# Analyze the data
echo "Analyzing data..."
yank analyze --store=all-ligands-implicit-output
