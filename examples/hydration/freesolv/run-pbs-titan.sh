#!/bin/bash
#    Begin PBS directives
#
# Account to charge: our project number
#PBS -A chm126
#
# Set job name
#PBS -N freesolv
#
# Capture output and error
#PBS -j oe
#
# Production limit is six hours, but jobs can be chained
#PBS -l walltime=12:00:00,nodes=1300
#PBS -q killable
##PBS -l walltime=00:30:00,nodes=10
##PBS -q debug
#
# Use atlas scratch storage
#PBS -l gres=atlas1%atlas2
#
# Start GPUs in shared mode for YANK to work
#PBS -l feature=gpudefault
#
#    End PBS directives and begin shell commands

env

# Set paths
export PROJECT="chm126"
export USERNAME="`whoami`"
export SOFTWARE="$PROJWORK/$PROJECT/yank/$USERNAME"
export MINICONDA3="$SOFTWARE/miniconda3"
export PATH="$MINICONDA3/bin:$PATH"
# Titan nodes have messed-up paths that differ from login node, so we also need to set LD_LIBRARY_PATH
export LD_LIBRARY_PATH="$MINICONDA3/lib:$LD_LIBRARY_PATH"
export SCRATCH="/lustre/atlas/scratch/$USERNAME/$PROJECT/"
module add cudatoolkit
export OE_LICENSE="$SOFTWARE/openeye/oe_license.txt"
export EDITOR="emacs -nw"

env

# Change directory
cd $PBS_O_WORKDIR
pwd

# Configure CUDA
module load cudatoolkit
export OPENMM_CUDA_COMPILER=`which nvcc`
echo $OPENMM_CUDA_COMPILER

# Set up mpi environment
module remove PrgEnv-pgi
module add PrgEnv-gnu
module add cray-mpich

ls -ltr $OE_LICENSE
cat $OE_LICENSE

# Run YANK, one MPI process per node
aprun -n $PBS_NUM_NODES -N 1 -d 16 yank script --yaml=freesolv.yaml
