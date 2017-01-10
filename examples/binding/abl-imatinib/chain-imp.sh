#!/bin/bash

script=run-torque-implicit.sh
rm impjobs.txt
INIT=$(qsub $script)
echo $INIT
echo $INIT >> impjobs.txt
for id in $(seq 2 17); do
 cont=$(qsub -W depend=afterany:$INIT $script)
 echo $cont
 echo $cont >> impjobs.txt
 INIT=$cont
done
