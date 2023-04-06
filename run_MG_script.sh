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
# process="sswwjj oswwjj wzjj zzjj www wwz wzz zzz";
# process="sswwjj_inclusive"
# process="sswwjj_inclusive oswwjj wzjj zzjj www wwz wzz zzz"
process="zzz"
EFT_param="S0"
vals="1e-12 1e-11 1e-10 1e-09 1e-08 1e-07 "
ext="round1"
# model="sm loop_sm SM_Ltotal_Ind5v2020v2_UFO"
model="SM_Ltotal_Ind5v2020v2_UFO"
nevents="10000"
# process="zzz"
# EFT_param="1e-12 2e-12 4e-12 6e-12 8e-12 1e-11 2e-11 4e-11 6e-11 8e-11 1e-10 2e-10 4e-10 6e-10 8e-10 1e-9 2e-9 4e-9 6e-9 8e-9 1e-8 2e-8 4e-8 6e-8 8e-8 1e-7 2e-7 4e-7 6e-7 8e-7 1e-6";
# EFT_param="1e-20 1e-12 1e-11 1e-10 1e-09 1e-08 1e-07"
echo $inclusive
for p in $process;
do 
    for e in $EFT_param;
    do
        for m in ${model};
        do
            echo python make_MadGraph_script.py ${p} ${e} ${inclusive} ${vals} ${nevents} ${m} ${ext}
            python make_MadGraph_script.py ${p} ${e} ${inclusive} ${vals} ${nevents} ${m} ${ext}
        done
    done

    # echo MG5_aMC_v3_4_0/bin/mg5_aMC ${p}_${fileExt}/mg_script_${p}_S0.txt
    # MG5_aMC_v3_4_0/bin/mg5_aMC ${p}_${fileExt}/mg_script_${p}_S0.txt
done
