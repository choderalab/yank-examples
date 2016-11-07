#!/bin/bash

#
# phenol hydration free energy (serial mode)
#

# Run the simulation
echo "Running simulation..."
yank script --yaml=implicit.yaml

# Analyze the data
echo "Analyzing data..."
yank analyze --store=experiments
