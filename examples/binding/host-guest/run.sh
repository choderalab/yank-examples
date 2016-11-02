#!/bin/bash

#
# Host-guest example run script (serial mode)
#

# Run YANK
yank script --yaml=yank.ymal

# Analyze the data
echo "Analyzing data..."
yank analyze --store=output
