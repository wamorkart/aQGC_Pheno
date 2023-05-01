#!/bin/bash

process=$1
operator=$2
val=$3
# val="1e-20 1e-12 1e-11 1e10 1e-09 1e-08 1e-07"

for v in $val;
do
   echo /lcrc/group/ATLAS/users/twamorkar/MG5_aMC_v3_4_2/bin/mg5_aMC ${process}_${operator}_${v}_1/mg_script_${process}_${operator}_${v}.txt
   /lcrc/group/ATLAS/users/twamorkar/MG5_aMC_v3_4_2/bin/mg5_aMC ${process}_${operator}_${v}_1/mg_script_${process}_${operator}_${v}.txt

done

