#!/bin/bash
#  Batch script for mpirun job on cbio cluster.
#  Adjust your script as needed for your clusters!
#
# walltime : maximum wall clock time (hh:mm:ss)
#PBS -l walltime=6:00:00
#
# join stdout and stderr
#PBS -j oe
#
# spool output immediately
#PBS -k oe
#
# specify queue
#PBS -q gpu
#
# nodes: number of nodes
#   ppn: how many cores per node to use
#PBS -l nodes=2:ppn=4:gpus=4:shared:gtx680
#
# export all my environment variables to the job
##PBS -V
#
# job name (default = name of script file)
#PBS -N host-guest

if [ -n "$PBS_O_WORKDIR" ]; then
    cd $PBS_O_WORKDIR
fi

cat $PBS_GPUFILE

# Run the simulation with verbose output:
echo "Running simulation via MPI..."
source activate yex
build_mpirun_configfile "yank script --yaml=yank.yaml"
mpiexec.hydra -configfile configfile
date
