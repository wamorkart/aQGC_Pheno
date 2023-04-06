#! /usr/bin/env python3

import argparse
import numpy as np
import os
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Produce a MadGraph script for scanning EFT parameter over the specified values for different processes.")
    parser.add_argument("process", type=str, action="store", help="The process to generate.")
    parser.add_argument("inclusive",type=str,action="store",help="check if the process to be generated is inclusive or not")  
    parser.add_argument("nevents", type=float, action="store", help="number of events to generate")

    # parser.add_argument("out_dir",type=str,action="store",help="output dir name")

    args = parser.parse_args()

    # print (args.inclusive)
    out_dir = args.process + "_loopSM_" + str(args.inclusive)
    # out_dir = args.out_dir if args.out_dir else "."
    try:
        os.makedirs(out_dir)
    except FileExistsError:
        pass
    print ("inclusive: ", args.inclusive)
    # with open(out_dir+"/mg_script_{}_{}.txt".format(args.process, args.EFT_param), "w") as f:
    with open(out_dir+"/mg_script_{}_loop_sm.txt".format(args.process), "w") as f:
        f.write("""#########################################
            
#########################################

import model loop_sm
define p = g u c d s u~ c~ d~ s~ b b~
define j = p
define z1 = z
define z2 = z
""")
        generate_lines = ""
        maxjetflavor = 5
        

        if (args.process=="www"):
            maxjetflavor = 4
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ w+ w- QCD=0
add process p p > w- w- w+  QCD=0"""
                 
            else:    
                generate_lines = """generate p p > w+ w+ w- , w+ > l+ vl, w- > j j
add process p p > w- w- w+  , w- > l- vl~, w+ > j j"""   
        elif (args.process=="wwz"):
            maxjetflavor = 4
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ w- z  QCD=0"""
            else:    
                generate_lines  = """generate p p > w+ w- z  , w+ > l+ vl, w- > l-  vl~, z > j j 
add process p p > w+ w- z, w+ > l+ vl, w- > j j, z > l+ l-
add process p p > w+ w- z, w+ > j j, w- > l-, vl~, z > l+ l-"""
        elif (args.process=="sswwjj_inclusive"):
            maxjetflavor = 5
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ w+ j j  QCD=0
add process p p > w- w- j j  QCD=0"""
            else:    
                generate_lines = """generate p p > w+ w+ j j  , w+ > l+ vl
add process p p > w- w- j j  , w- > l- vl~"""
        elif (args.process=="sswwjj_wp"):
            maxjetflavor = 5
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ w+ j j QCD=0 """
            else:    
                generate_lines = """generate p p > w+ w+ j j  , w+ > l+ vl"""
        elif (args.process=="sswwjj_wm"):
            maxjetflavor = 5
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w- w- j j QCD=0  """
            else:    
                generate_lines = """add process p p > w- w- j j  , w- > l- vl~"""                
        elif (args.process=="oswwjj"):
            maxjetflavor = 4
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ w- j j QCD=0 """
            else:    
                generate_lines = """generate p p > w+ w- j j  , w+ > l+ vl, w- > l- vl~"""
        elif (args.process=="wzjj"):
            maxjetflavor = 5
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ z j j  QCD=0
add process p p > w- z j j  QCD=0"""
            else:    
                generate_lines = """generate p p > w+ z j j  , w+ > l+ vl, z > l+ l- 
add process p p > w- z j j  , w- > l- vl~, z > l+ l-"""
        elif (args.process=="zzjj"):
            maxjetflavor = 5
            if (args.inclusive=="1"):
                generate_lines = """generate p p > z z j j  QCD=0"""
            else:    
                generate_lines = """generate p p > z z j j  , z > l+ l-
generate p p > z1 z2 j j  , z1 > l+ l-, z2 > j j"""    
        elif (args.process=="wzz"):
            maxjetflavor = 5
            if (args.inclusive=="1"):
                generate_lines = """generate p p > w+ z z  QCD=0
add process p p > w- z z  QCD=0"""
            else:
                generate_lines = """generate p p > w+ z1 z2  , w+ > l+ vl, z1 > l+ l-, z2 > j j
add process p p > w- z1 z2  , w- > l- vl~, z1 > l+ l-, z2 > j j"""    
        elif (args.process=="zzz"):
            maxjetflavor = 5
            if (args.inclusive=="1"):
                generate_lines = """generate p p > z z z  QCD=0"""
            else:
                generate_lines = """generate p p > z1 z1 z2  , z1 > l+ l-, z2 > j j """                
        f.write("""

{}

output /lcrc/project/aqgc/twamorkar/aqgc_pheno/{}_loop_sm
launch /lcrc/project/aqgc/twamorkar/aqgc_pheno/{}_loop_sm

# shower=PYTHIA8
# detector=PGS
# analysis=MADANALYSIS_5
# madspin=OFF
# reweight=OFF
done""".format(generate_lines, args.process, args.process ))

        f.write("""
#——————————————————————————————————————
## Set Run card and Param card values:
#——————————————————————————————————————

### run_card.dat:
set run_tag {}_loop_sm
set nevents {}
set bwcutoff 15.0
set ptb 20.0
set etab 5.0
set drbb 0.4
set drbj 0.4
""".format(args.process, args.nevents))

        f.write("""
set maxjetflavor {}
set iseed 0

done

""".format(maxjetflavor))
        f.write("""
launch /lcrc/project/aqgc/twamorkar/aqgc_pheno/{}_loop_sm  -i
print_results --path=/lcrc/project/aqgc/twamorkar/aqgc_pheno/cross_section_{}_loop_sm.txt --format=short 

        """.format(args.process, args.process))


