#!/bin/bash

#
# Host-guest example run script (serial mode)
#

# Run YANK
yank script --yaml=sams.yaml

# Analyze the data
echo "Analyzing data..."
yank analyze --store=sams-explicit
