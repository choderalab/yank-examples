#!/bin/bash

#
# Compound 22 binding to c-Met Kinase in explicit solvent.
#

# Run the simulation with verbose output:
echo "Running simulation..."
yank script --yaml=explicit.yaml

# Analyze the data
echo "Analyzing data..."
yank analyze --store=explicit
