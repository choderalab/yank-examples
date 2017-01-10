#!/bin/bash

script=run-torque.sh
joblist=jobids.txt
INIT=$(qsub $script)
echo $INIT
echo $INIT >> $joblist 
for id in $(seq 2 17); do
 cont=$(qsub -W depend=afterany:$INIT $script)
 echo $cont
 echo $cont >> $joblist
 INIT=$cont
done
