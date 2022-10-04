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
TYPE=$2;
EFT_PARAM=$3;
./mg5amcnlo/bin/mg5_aMC ${PROCESS}_${TYPE}/mg_script_${PROCESS}_${EFT_PARAM}.txt
echo -e "DONE";
    '''

    arguments=[]

    process = ["sswwjj", "oswwjj", "wzjj", "zzjj", "www", "wwz", "wzz", "zzz"]
    type = ["inclusive"]
    eft_param = ["S0"]

    for p in process:
        for t in type:
            for param in eft_param:
                arguments.append("{} {} {}".format(p, t, param))

    with open("arguments.txt", "w") as args:
     args.write("\n".join(arguments))
    with open("run_script.sh", "w") as rs:
     rs.write(script)