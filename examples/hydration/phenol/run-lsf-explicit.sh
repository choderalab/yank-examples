#!/bin/bash
#  Batch script for mpirun job on cbio LSF cluster
#  Adjust your script as needed for your clusters!
#
# walltime : maximum wall clock time (hh:mm)
#BSUB -W 6:00
#
# Set Output file
#BSUB -o  phenol-explicit.%J.log
#
# Specify node group
#BSUB -m ls-gpu
#
# 4 CPU and 4 GPU on 1 node
#BSUB -n 4 -R "rusage[mem=8] span[ptile=4]"
#BSUB -gpu "num=1:j_exclusive=yes:mode=shared"
#
# Start MPS since Cbio GPUs are in exclusive mode
#BSUB -env "all, LSB_START_JOB_MPS=Y"
#
# job name (default = name of script file)
#BSUB -J "phenol-explicit"

# Run the simulation with verbose output:
echo "Running simulation via MPI..."
build_mpirun_configfile "yank script --yaml=explicit.yaml"
mpiexec.hydra -f hostfile -configfile configfile
date

