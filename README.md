[![Travis Build Status](https://travis-ci.org/choderalab/yank.png)](https://travis-ci.org/choderalab/yank-examples)
[![Anaconda Cloud Badge](https://anaconda.org/omnia/yank/badges/version.svg)](https://anaconda.org/omnia/yank-examples)
[![Anaconda Cloud Downloads](https://anaconda.org/omnia/yank/badges/downloads.svg)](https://anaconda.org/omnia/yank-examples)
[//]: <> [![DOI](https://zenodo.org/badge/????????.svg)](https://zenodo.org/badge/latestdoi/????????)

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

* `binding/t4-lysozyme` - Absolute binding of para-xylene to T4-Lysozyme, both implicit and explicit solvent
* `binding/host-guest` - Host-Guest absolute binding system guest B2 to host cucurbit\[7\]uril in implciit solvent
