[![Travis Build Status](https://travis-ci.org/choderalab/yank-examples.png)](https://travis-ci.org/choderalab/yank-examples)
[![Anaconda Cloud Badge](https://anaconda.org/omnia/yank-examples/badges/version.svg)](https://anaconda.org/omnia/yank-examples)
[![Anaconda Cloud Downloads](https://anaconda.org/omnia/yank-examples/badges/downloads.svg)](https://anaconda.org/omnia/yank-examples)
[![DOI](https://zenodo.org/badge/71493092.svg)](https://zenodo.org/badge/latestdoi/71493092)

# Examples for YANK

This repository houses the examples for [YANK](http://github.com/choderalab/yank). Here you will find all the files needed
to run sample simulations in YANK to see its functionality in action.

Detailed guides are available to guide you through these examples through 
[the YANK webpage](http://getyank.org/latest/examples/index.html).


# Installation Instructions

## Requirements

* YANK >= 0.12.0
* AmberMini >= 16.16.0

## Installing through `conda`

We make this repository through the `omnia` conda channel for easy 
install. The files will be put in `{Python Source Dir}/share/yank/examples`

```bash
conda install -c omnia yank-examples
```

## Installing from "source"

There is no source code with these examples per-se. Just clone the repository 
into any directory you prefer, so long as the pre-requisites are installed.


# Included Examples

All example files are in the `examples` folder.

* `binding/` - binding free energy calculations
* `   t4-lysozyme/` - Absolute binding of T4-Lysozyme, both implicit and explicit solvent
    * Binding for para-xylene from mol2 files
    * Binding for a series of binders and non-binders generated from SMILES strings (requires OpenEye Toolkits)
* `   host-guest/` - Host-Guest absolute binding system guest B2 to host cucurbit\[7\]uril in implciit solvent
* `   abl-imatinib/` - Absolute binding free energy calculation to three dominant protonation states of imatinib to Abl at pH 7.4
* `hydration/` - hydration free energies
* `   phenol/` - Hydration free energy of phenol molecule in water for both implicit and explicit solvents
* `   freesolv/` - Hydration free energy of a subset of the FreeSolv database.
    * Molecules generated from SMILES strings (requires OpenEye Toolkits)
    * Multiple simulations configured at once from YANK's `!Combinatorial` feature.

