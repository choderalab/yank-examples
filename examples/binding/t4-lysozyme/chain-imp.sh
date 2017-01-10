#!/bin/bash

script=run-torque-all-ligands-implicit.sh
joblist=all_lig_imp_jobs.txt
rm $joblist
INIT=$(qsub $script)
echo $INIT
echo $INIT >> $joblist 
for id in $(seq 2 17); do
 cont=$(qsub -W depend=afterok:$INIT $script)
 echo $cont
 echo $cont >> $joblist
 INIT=$cont
done
