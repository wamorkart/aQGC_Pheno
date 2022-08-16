#! /usr/bin/env python3

import argparse
import numpy as np
import os
import sys



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Produce a MadGraph script for scanning EFT parameter over the specified values for different processes.")
    parser.add_argument("process", type=str, action="store", help="The process to generate.")
    parser.add_argument("EFT_param", type=str, action="store", help="The EFT parameter to scan.")  
    parser.add_argument("inclusive",type=bool,action="store",help="check if the process to be generated is inclusive or not")  
    parser.add_argument("scan_values", nargs="+", help="Values to scan.")
    parser.add_argument("out_dir",type="str",action="store",help="output dir name")

    args = parser.parse_args()

    out_dir = args.output if args.output else "."
    try:
        os.makedirs(out_dir)
    except FileExistsError:
        pass

    # with open(out_dir+"/mg_script_{}_{}.txt".format(args.process, args.EFT_param), "w") as f:
    with open(out_dir+"/mg_script_{}_{}.txt".format(args.process, args.EFT_param), "w") as f:
        f.write("""#########################################
#########################################


define p = g u c d s u~ c~ d~ s~ b b~
define j = p
define z1 = z
define z2 = z
""")
        model = ""
        generate_lines = ""
        if (args.EFT_param=="S0"):
            model = "import SM_LS012"
        if (args.process=="www"):
            if (args.inclusive==True):
                generate_lines = """generate p p > w+ w+ w- QCD=0
                add process p p > w- w- w+ QCD=0"""
            else:    
                generate_lines = """generate p p > w+ w+ w- QCD=0, w+ > l+ vl, w- > j j
add process p p > w- w- w+ QCD=0, w- > l- vl~, w+ > j j"""   
        elif (args.process=="wwz"):
            if (args.inclusive==True):
                generate_lines = """generate p p > w+ w- z """
            else:    
                generate_lines  = """generate p p > w+ w- z, w+ > l+ vl, w- > l-  vl~, z > j j 
add process p p > w+ w- z, w+ > l+ vl, w- > j j, z > l l
add process p p > w+ w- z, w+ > j j, w- > l-, vl~, z > l l"""
        elif (args.process=="sswwjj"):
            if (args.inclusive==True):
                generate_lines = """generate p p > w+ w+ j j QCD=0
                add process p p > w- w- j j QCD=0"""
            else:    
                generate_lines = """generate p p > w+ w+ j j QCD=0, w+ > l+ vl
            add process p p > w- w- j j QCD=0, w- > l- vl~"""
        elif (args.process=="oswwjj"):
            if (args.inclusive==True):
                generate_lines = """generate p p > w+ w- j j QCD=0"""
            else:    
                generate_lines = """generate p p > w+ w- j j QCD=0, w+ > l+ vl, w- > l- vl~"""
        elif (args.process=="wzjj"):
            if (args.inclusive==True):
                generate_lines = """generate p p > w+ z j j QCD=0
                add process p p > w- z j j QCD=0"""
            else:    
                generate_lines = """generate p p > w+ z j j QCD=0, w+ > l+ vl, z > l+ l- 
            add process p p > w- z j j QCD=0, w- > l- vl~, z > l+ l-"""
        elif (args.process=="zzjj"):
            if (args.inclusive==True):
                generate_lines = """generate p p > z z j j QCD=0"""
            else:    
                generate_lines = """generate p p > z z j j QCD=0, z > l+ l-
            generate p p > z1 z2 j j QCD=0, z1 > l l, z2 > j j"""    
        elif (args.process=="wzz"):
            if (args.inclusive==True):
                generate_lines = """generate p p > w+ z z QCD=0
                add process p p > w- z z QCD=0"""
            else:
                generate_lines = """generate p p > w+ z1 z2 QCD=0, w+ > l+ vl, z1 > l+ l-, z2 > j j
                add process p p > w- z1 z2 QCD=0, w- > l- vl~, z1 > l+ l-, z2 > j j"""    
        elif (args.process=="zzz"):
            if (args.inclusive==True):
                generate_lines = """generate p p > z z z QCD=0"""
            else:
                generate_lines = """generate p p > z1 z1 z2 QCD=0, z1 > l+ l-, z2 > j j """                
        f.write("""{}

{}

output {}_aQGC_L{}
launch {}_aQGC_L{}

shower=PYTHIA8
detector=PGS
analysis=MADANALYSIS_5
madspin=OFF
reweight=OFF
done
#——————————————————————————————————————
## Set Run card and Param card values:
#——————————————————————————————————————

### param_card.dat:

set anoinputs 1 1.000000e-20  #FS0
set anoinputs 2 1.000000e-20  #FS1
set anoinputs 3 1.000000e-20  #FS2
set anoinputs 4 1.000000e-20  #FM0
set anoinputs 5 1.000000e-20  #FM1
set anoinputs 6 1.000000e-20  #FM2
set anoinputs 7 1.000000e-20  #FM3
set anoinputs 8 1.000000e-20  #FM4
set anoinputs 9 1.000000e-20  #FM5
set anoinputs 10 1.000000e-20  #FM6
set anoinputs 11 1.000000e-20  #FM7
set anoinputs 12 1.000000e-20  #FT0
set anoinputs 13 1.000000e-20  #FT1
set anoinputs 14 1.000000e-20  #FT2
set anoinputs 15 1.000000e-20  #FT3
set anoinputs 16 1.000000e-20  #FT4
set anoinputs 17 1.000000e-20  #FT5
set anoinputs 18 1.000000e-20  #FT6
set anoinputs 19 1.000000e-20  #FT7
set anoinputs 20 1.000000e-20  #FT8
set anoinputs 21 1.000000e-20  #FT9

### run_card.dat:

set run_tag {}_aQGC_F{}_1e-20_events
set nevents 50000
set bwcutoff 15.0
set ptb 20.0
set etab 5.0
set drbb 0.4
set drbj 0.4
set maxjetflavor 5
#set event_norm sum

done""".format(model, generate_lines, args.process, args.EFT_param, args.process, args.EFT_param, args.process, args.EFT_param))
## Loop over scan values
        f.write("""
#########################################
## Run through coupling parameters \n""")
        for scan_value in args.scan_values:
            f.write("""launch {}_aQGC_L{}
done
set run_tag {}_aQGC_F{}_{}
set anoinputs 1 {}  #FS0
done \n""".format(args.process, args.EFT_param, args.process, args.EFT_param, scan_value, scan_value))

        f.write("""launch {}_aQGC_L{} -i 
print_results --path=./cross_section_{}_aQGC_L{}.txt --format=short
exit

exit""".format(args.process, args.EFT_param, args.process, args.EFT_param))


       