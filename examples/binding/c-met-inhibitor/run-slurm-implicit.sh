#!/bin/bash
#
#Walltime
#SBATCH -t 72:00:00
#
#SBATCH -o "c-Met-imp.%j.out"
#
#Set the parition which as the GPUs we want (Merck KGaA configuration)
#SBATCH --partition=GTX
#
# Pack 8 CPU and 8 GPUs on 2 nodes
#SBATCH -N 2 -n 8 --gres=gpu:8
#
# Export all environment variables
#SBATCH --export=ALL
#
# Set the Job Name
#SBATCH --job-name="c-Met-imp"

# Run the simulation with verbose output:
echo "Running simulation via MPI..."
build_mpirun_configfile "yank script --yaml=implicit.yaml"
mpiexec.hydra -f hostfile -configfile configfile
date