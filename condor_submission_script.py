import os


if __name__ == '__main__':


    inputDir = os.getcwd()
    if not os.path.isdir('error'): os.mkdir('error')
    if not os.path.isdir('output'): os.mkdir('output')
    if not os.path.isdir('log'): os.mkdir('log')


    # Prepare condor jobs
    condor = '''executable              = run_script.sh
output                  = output/aQGCPheno.$(ClusterId).$(ProcId).out
error                   = error/aQGCPheno.$(ClusterId).$(ProcId).err
log                     = log/aQGCPheno.$(ClusterId).log
transfer_input_files    = run_script.sh
on_exit_remove          = (ExitBySignal == False) && (ExitCode == 0)
periodic_release        = (NumJobStarts < 3) && ((CurrentTime - EnteredCurrentStatus) > (60*60))
+JobFlavour             = "workday"
queue arguments from arguments.txt
    '''

    with open("condor_job.txt", "w") as cnd_out:
        cnd_out.write(condor)

    outputDir = os.getcwd()

    script = '''#!/bin/sh -e
PROCESS=$1;
EFT_PARAM=$2;
INCLUSIVE=$3;
PARAM_VAL=$4;
NEVENTS=$5;
python2.7 /afs/cern.ch/work/t/twamorka/aQGC_Pheno/MG5_aMC_v2_9_9/bin/mg5_aMC /afs/cern.ch/work/t/twamorka/aQGC_Pheno/${PROCESS}_${EFT_PARAM}_${PARAM_VAL}_${INCLUSIVE}/mg_script_${PROCESS}_${EFT_PARAM}_${PARAM_VAL}.txt
echo -e "DONE";
    '''

    arguments=[]

    process = ["sswwjj", "oswwjj", "wzjj", "zzjj", "www", "wwz", "wzz", "zzz"]
    eft_params = ["S0"]
    param_vals = [1e-20, 1e-12, 1e-11, 1e-10, 1e-9, 1e-8, 1e-7]
    #param_vals = [1e-12, 2e-12, 4e-12, 6e-12, 8e-12, 1e-11, 2e-11, 4e-11, 6e-11, 8e-11, 1e-10, 2e-10, 4e-10, 6e-10, 8e-10, 1e-9, 2e-9, 4e-9, 6e-9, 8e-9, 1e-8, 2e-8, 4e-8, 6e-8, 8e-8, 1e-7, 2e-7, 4e-7, 6e-7, 8e-7, 1e-6 ]
    inclusive = 1
    nevents = 10000
    for proc in process:
        for param in eft_params:
            for val in param_vals:
                arguments.append("{} {} {} {} {}".format(proc, param, str(inclusive), val, nevents))

    with open("arguments.txt", "w") as args:
     args.write("\n".join(arguments))
    with open("run_script.sh", "w") as rs:
     rs.write(script)
