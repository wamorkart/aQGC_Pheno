# Pheno aQGC multiboson study

## Setup
These are instructions to perform the setup on LCRC:

1. Clone the repository:
```git clone git@github.com:wamorkart/aQGC_Pheno.git```
2. Setup MadGraph v3.4.2 inside the ```aQGC_Pheno``` directory:
The installation files can be found here:  [here](https://launchpad.net/mg5amcnlo/3.0/3.4.x)
3. Now you have everything you need in terms of installation

## Procedure
In this analysis, we are interested in exploring VBS and Tri-Boson process. They are:
- Opposite sign wwjj
- Same sign wwjj
- wzjj
- zzjj
- www
- wwz
- wzz
- zzz
1. The first step is calculating the SM cross-section for the above listed processes. This is done using the ```make_MadGraph_SM_script.py```. Some MadGraph reference can be found [here](https://arxiv.org/pdf/1405.0301.pdf).
   - How to run: ```python make_MadGraph_SM_script.py <process> <inclusive> <nevents> ```
   - If you want to generate the inclusive process, <inclusive> should be set equal to 1
   - Eg: To generate the process p p > z z z QCD=0 with 10k events you should do ```python make_MadGraph_SM_script.py zzz 1 10000 ```
   - You can also run a bash script which runs the python script, like so ```./run_MG_SM_script.sh <inclusive>```. For eg: ```./run_MG_SM_script.sh 1```