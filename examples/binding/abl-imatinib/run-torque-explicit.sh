#!/bin/bash
#  Batch script for mpirun job on cbio cluster.
#
#
# walltime : maximum wall clock time (hh:mm:ss)
#PBS -l walltime=72:00:00
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
#PBS -l nodes=4:ppn=4:gpus=4:shared:gtx680
#
# export all my environment variables to the job
##PBS -V
#
# job name (default = name of script file)
#PBS -N abl-imatinib-explicit

if [ -n "$PBS_O_WORKDIR" ]; then 
    cd $PBS_O_WORKDIR
fi

cat $PBS_GPUFILE

nvcc --version

# Run the simulation with verbose output:
echo "Running simulation via MPI..."
export PREFIX="explicit"
build_mpirun_configfile --hostfilepath $PREFIX.hostfile --configfilepath $PREFIX.configfile "yank script --yaml=$PREFIX.yaml"
mpirun -f $PREFIX.hostfile -configfile $PREFIX.configfile
date
