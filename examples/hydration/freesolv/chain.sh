#!/bin/bash

script=run-torque-yank.sh
joblist=freesolv_jobs.txt
rm $joblist
INIT=$(qsub $script)
echo $INIT
echo $INIT >> $joblist 
for id in $(seq 2 17); do
 cont=$(qsub -W depend=afterany:$INIT $script)
 echo $cont
 echo $cont >> $joblist
 INIT=$cont
done
