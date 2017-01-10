#!/bin/bash
#  Batch script for mpirun job on cbio cluster.
#
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
#PBS -N abl-imatinib-explicit
#
# Email me when done
#PBS -m bea
#PBS -M levi.naden+simulation.reporter@choderalab.org


if [ -n "$PBS_O_WORKDIR" ]; then 
    cd $PBS_O_WORKDIR
fi

cat $PBS_GPUFILE

nvcc --version

# Run the simulation with verbose output:
echo "Running simulation via MPI..."
source activate yex
export PREFIX="explicit"
build_mpirun_configfile --configfilepath $PREFIX.configfile "yank script --yaml=$PREFIX.yaml"
mpirun -configfile $PREFIX.configfile
date
