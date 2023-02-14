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
process="sswwjj oswwjj wzjj zzjj www wwz wzz zzz";
# process="sswwjj";

EFT_param="S0"
value="1e-20 1e-12 1e-11 1e-10 1e-9 1e-8 1e-7"
nevents=10000
for p in $process;
# for process in wzz;
do
    for v in $value;
    do
    
       echo python3 make_MadGraph_script.py ${p} ${EFT_param} ${inclusive} ${v} ${nevents}
       python3 make_MadGraph_script.py ${p} ${EFT_param} ${inclusive} ${v} ${nevents}
    done
    # echo MG5_aMC_v3_4_0/bin/mg5_aMC ${p}_${fileExt}/mg_script_${p}_S0.txt
    # MG5_aMC_v3_4_0/bin/mg5_aMC ${p}_${fileExt}/mg_script_${p}_S0.txt
done
