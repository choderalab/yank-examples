#!/bin/bash
# Maximum wall clock time (hh:mm)
#BSUB -W 72:00
#
# Output log
#BSUB -o c-Met-imp.%J.log
#
# Request 8 cores and 8 GPUs packed onto 2 nodes
# Note: MSKCC's LSF Cluster is configured so ngpus_excl_p behaves different from default
#BSUB -n 8 -R "rusage[ngpus_excl_p=1] span[ptile=4]"
#
# Submit to the queue which flips GPUs into shared mode from exclusive mode (MSKCC configuration)
#BSUB -q gpushared
#
# Job Name
#BSUB -J cMet-imp

# Run the simulation with verbose output:
echo "Running simulation via MPI..."
build_mpirun_configfile "yank script --yaml=implicit.yaml"
mpiexec.hydra -f hostfile -configfile configfile
date