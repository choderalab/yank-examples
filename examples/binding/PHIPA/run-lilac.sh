#!/bin/bash
#BSUB -W 6:00
#BSUB -q gpuqueue
#BSUB -R "rusage[mem=2]"
#BSUB -n 1
#BSUB -R "span[ptile=1]"
#BSUB -gpu "num=1:mode=shared:mps=no:j_exclusive=yes"
#BSUB -m "lt-gpu ls-gpu lu-gpu lp-gpu"
#BSUB -o %J.PHIPA.out
#BSUB -J "PHIPA[1-128]"
JOBID=$LSB_JOBINDEX
NJOBS=128  # This is usually the total number of experiments but can be less than that.


source ~/.bashrc

echo "Job $JOBID/$NJOBS"
echo "LSB_HOSTS: $LSB_HOSTS"
echo "CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES"
module add cuda/10.1
nvcc --version
source activate yank
python run_yank.py --yaml=all-ligands-explicit.yaml --jobid=$JOBID --njobs=$NJOBS
