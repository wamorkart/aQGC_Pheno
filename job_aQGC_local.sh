#!/bin/bash


process="sswwjj_inclusive oswwjj wzjj zzjj www wwz wzz www"
operator="S1"
for p in $process;
do
        for o in ${operator};
        do
                /home/twamorkar/MG5_aMC_v3_4_2/bin/mg5_aMC ${p}_aQGC_${o}_1/mg_script_${p}_${o}_SM_Ltotal_Ind5v2020v2_UFO.txt &
        done
done



