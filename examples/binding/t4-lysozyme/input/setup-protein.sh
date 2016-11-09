#!/bin/bash

# Prepare receptor by filling in missing atoms and expunging waters and ions.
# NOTE: Requires pdbfixer tool be installed and PDBFIXER_HOME environment variable set.
echo "Preparing receptor by adding missing atoms..."
rm -f receptor.pdbfixer.pdb
pdbfixer --pdbid=187L --keep-heterogens=none --add-atoms=heavy --ph=7.0 --replace-nonstandard --output=receptor.pdbfixer.pdb
