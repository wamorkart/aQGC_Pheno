#!/bin/bash

inclusive=$1
fileExt=""
if [ $inclusive == 1 ] 
then
    fileExt="inclusive"
fi
process="sswwjj oswwjj wzjj zzjj www wwz wzz zzz";
EFT_param="1e-20 1e-12 1e-11 1e-10 2e-10 3e-10 4e-10 1e-9 5e-9 1e-8"
for p in $process;
# for process in wzz;
do 
    echo python make_MadGraph_script.py ${p} S0 1 ${EFT_param} ${p}_${fileExt}
    python make_MadGraph_script.py ${p} S0 1 ${EFT_param} ${p}_${fileExt}
done