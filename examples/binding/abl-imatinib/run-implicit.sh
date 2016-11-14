#!/bin/bash

#
# Abl binding to imatinib in implicit solvent.
#

# Run the simulation with verbose output:
echo "Running simulation..."
yank script --yaml=implicit.yaml

# Analyze the data
echo "Analyzing data..."
yank analyze --store=experiments
