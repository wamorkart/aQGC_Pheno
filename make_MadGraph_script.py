#! /usr/bin/env python3

import argparse
import numpy as np
import os
import sys


param_numbers = {"S0":1, "S1":2, "S2":3, "M0":4, "M1":5, "M2":6, "M3":7, "M4":8, "M5":9, "M6":10, "M7":11, "T0":12, "T1":13, "T2":14, "T3":15, "T4":16, "T5":17, "T6":18, "T7":19, "T8":20, "T9":21}
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Produce a MadGraph script for scanning EFT parameter over the specified values for different processes.")
    parser.add_argument("process", type=str, action="store", help="The process to generate.")
    parser.add_argument("EFT_param", type=str, action="store", help="The EFT parameter to scan.")  
    parser.add_argument("inclusive",type=str,action="store",help="check if the process to be generated is inclusive or not")  
    parser.add_argument("scan_values", type=float, action="store", help="Values to scan.")
    parser.add_argument("nevents", type=float, action="store", help="number of events to generate")

    # parser.add_argument("out_dir",type=str,action="store",help="output dir name")

    args = parser.parse_args()
    
    out_dir = args.process + "_" + args.EFT_param + "_" + str(args.scan_values) +"_" + str(args.inclusive)
    # out_dir = args.out_dir if args.out_dir else "."
    try:
        os.makedirs(out_dir)
    except FileExistsError:
        pass
    print ("inclusive: ", args.inclusive)
    # with open(out_dir+"/mg_script_{}_{}.txt".format(args.process, args.EFT_param), "w") as f:
    with open(out_dir+"/mg_script_{}_{}_{}.txt".format(args.process, args.EFT_param, args.scan_values), "w") as f:
        f.write("""#########################################
            
#########################################

import SM_Ltotal_Ind5v2020v2_UFO
define p = g u c d s u~ c~ d~ s~ b b~
define j = p
define z1 = z
define z2 = z
""")
        model = ""
        generate_lines = ""
        # if (args.EFT_param=="S0"):
        #     model = "import SM_Ltotal_Ind5v2020v2_UFO"
        if (args.process=="www"):
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ w+ w- QCD=0
add process p p > w- w- w+ QCD=0"""
            else:    
                generate_lines = """generate p p > w+ w+ w- QCD=0, w+ > l+ vl, w- > j j
add process p p > w- w- w+ QCD=0, w- > l- vl~, w+ > j j"""   
        elif (args.process=="wwz"):
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ w- z """
            else:    
                generate_lines  = """generate p p > w+ w- z, w+ > l+ vl, w- > l-  vl~, z > j j 
add process p p > w+ w- z, w+ > l+ vl, w- > j j, z > l+ l-
add process p p > w+ w- z, w+ > j j, w- > l-, vl~, z > l+ l-"""
        elif (args.process=="sswwjj"):
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ w+ j j QCD=0
add process p p > w- w- j j QCD=0"""
            else:    
                generate_lines = """generate p p > w+ w+ j j QCD=0, w+ > l+ vl
add process p p > w- w- j j QCD=0, w- > l- vl~"""
        elif (args.process=="oswwjj"):
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ w- j j QCD=0"""
            else:    
                generate_lines = """generate p p > w+ w- j j QCD=0, w+ > l+ vl, w- > l- vl~"""
        elif (args.process=="wzjj"):
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ z j j QCD=0
add process p p > w- z j j QCD=0"""
            else:    
                generate_lines = """generate p p > w+ z j j QCD=0, w+ > l+ vl, z > l+ l- 
add process p p > w- z j j QCD=0, w- > l- vl~, z > l+ l-"""
        elif (args.process=="zzjj"):
            if (args.inclusive=="1"):
                generate_lines = """generate p p > z z j j QCD=0"""
            else:    
                generate_lines = """generate p p > z z j j QCD=0, z > l+ l-
generate p p > z1 z2 j j QCD=0, z1 > l+ l-, z2 > j j"""    
        elif (args.process=="wzz"):
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ z z QCD=0
add process p p > w- z z QCD=0"""
            else:
                generate_lines = """generate p p > w+ z1 z2 QCD=0, w+ > l+ vl, z1 > l+ l-, z2 > j j
add process p p > w- z1 z2 QCD=0, w- > l- vl~, z1 > l+ l-, z2 > j j"""    
        elif (args.process=="zzz"):
            if (args.inclusive=="1"):
                generate_lines = """generate p p > z z z QCD=0"""
            else:
                generate_lines = """generate p p > z1 z1 z2 QCD=0, z1 > l+ l-, z2 > j j """                
        f.write("""{}

{}

output {}
launch {}

# shower=PYTHIA8
# detector=PGS
# analysis=MADANALYSIS_5
# madspin=OFF
# reweight=OFF
done""".format(model, generate_lines, out_dir, out_dir))

        f.write("""
#——————————————————————————————————————
## Set Run card and Param card values:
#——————————————————————————————————————

### param_card.dat:
""")
        for param in param_numbers:
            if (param != args.EFT_param):
                f.write("""
set anoinputs {} 1e-20 #{}
    """.format(param_numbers[param], param))
            else:
               f.write("""
set anoinputs {} {} #{}
    """.format(param_numbers[param], args.scan_values,param) )

        f.write("""
### run_card.dat:

set run_tag {}_{}_{}
set nevents {}
set bwcutoff 15.0
set ptb 20.0
set etab 5.0
set drbb 0.4
set drbj 0.4
set maxjetflavor 5
set iseed 0

done


launch {}_{}_{}_{}  -i
print_results --path=cross_section_{}_{}_{}_{}.txt --format=short 

exit

        """.format(args.process, args.EFT_param, args.scan_values, args.nevents, args.process, args.EFT_param, args.scan_values, args.inclusive, args.process, args.EFT_param, args.scan_values, args.inclusive  ))




       
