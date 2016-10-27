# Set up p-xylene binding to T4 lysozyme L99A using AmberTools

## Manifest
* `setup.sh` - shell script to run whole setup pipeline to regenerate YANK input files
     Requires OpenEye Python toolkits, pdbfixer, and AmberTools
* `generate-mol2-from-name.py` - Python script to generate ligand Tripos mol2 file from IUPAC or common name
     Requires OpenEye Python toolkits.
* `setup.leap.in` - input file for AmberTools tleap
* `187L.pdb` - source PDB file for p-xylene bound to T4 lysozyme L99A
* `p-xylene.tripos.mol2` - p-xylene in Tripos mol2 format
* `run.sh` - shell script to run YANK simulation
* `run-torque.sh` - shell script to run YANK on a cluster, will need customized for your system