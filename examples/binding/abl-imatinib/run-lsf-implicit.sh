#!/bin/bash
#  Batch script for mpirun job on cbio LSF cluster
#  Adjust your script as needed for your clusters!
#
# walltime : maximum wall clock time (hh:mm)
#BSUB -W 72:00
#
# Set Output file
#BSUB -o  abl-imatinib-implicit.%J.log
#
# Specify node group
#BSUB -m ls-gpu
#
# nodes: number of nodes and GPU request
# 8 CPU and GPU over 2 nodes
#BSUB -n 8 -R "rusage[ngpus_excl_p=1,mem=8] span[ptile=4]"
#
# Start MPS since Cbio GPUs are in exclusive mode
#BSUB -env "all, LSB_START_JOB_MPS=Y"
#
# job name (default = name of script file)
#BSUB -J " abl-imatinib-implicit"


# Run the simulation with verbose output:
echo "Running simulation via MPI..."
export PREFIX="implicit"
build_mpirun_configfile --configfilepath $PREFIX.configfile "yank script --yaml=$PREFIX.yaml"
mpiexec.hydra -configfile $PREFIX.configfile
date

