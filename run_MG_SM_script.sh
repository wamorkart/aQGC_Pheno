#!/bin/bash

inclusive=$1
fileExt=""
if [ $inclusive == 1 ] 
then
    fileExt="inclusive"
fi
if [ $inclusive == 0 ] 
then
    fileExt="hadronic"
fi

process="sswwjj_inclusive oswwjj wzjj zzjj www wwz wzz zzz"

nevents="10000"
echo $inclusive
for p in $process;
do 
            echo python make_MadGraph_SM_script.py ${p} ${inclusive} ${nevents} 
            python make_MadGraph_SM_script.py ${p} ${inclusive} ${nevents} 

done
