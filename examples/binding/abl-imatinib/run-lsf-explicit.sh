#!/bin/bash
#  Batch script for mpirun job on cbio LSF cluster
#  Adjust your script as needed for your clusters!
#
# walltime : maximum wall clock time (hh:mm)
#BSUB -W 72:00
#
# Set Output file
#BSUB -o  abl-imatinib-explicit.%J.log
#
# Specify node group
#BSUB -m ls-gpu
#
# nodes: number of nodes and GPU request
# 8 CPU and GPU over 2 nodes
#BSUB -n 8 -R "rusage[mem=8] span[ptile=4]"
#BSUB -gpu "num=1:j_exclusive=yes:mode=shared"
#
# job name (default = name of script file)
#BSUB -J " abl-imatinib-explicit"


# Run the simulation with verbose output:
echo "Running simulation via MPI..."
export PREFIX="explicit"
build_mpirun_configfile --hostfilepath $PREFIX.hostfile --configfilepath $PREFIX.configfile "yank script --yaml=$PREFIX.yaml"
mpiexec.hydra -f $PREFIX.hostfile -configfile $PREFIX.configfile
date

