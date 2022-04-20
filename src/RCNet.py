import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

import statistics as stat

from Parameters import *
from lib.Benchmarks import *
from lib.MainAlgo import *
from lib.System import *
from lib.RandomSampling import *
from lib.Visualization import *
from lib.UnsafeTraj import *
import pandas as pd

class RC:

    def getD(initPoint=[10,10],H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=3,heuName="RandSampKMiss",B=415000,c=0.99):
        dynA=Benchmarks.DC.A
        dynB=Benchmarks.DC.B
        dynC=Benchmarks.DC.C
        dynD=Benchmarks.DC.D
        K=Benchmarks.DC.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)


        if schedPol=="HoldKill":
            initPointArrayRep=np.array(initPoint+[0]).reshape(3,-1)
        elif schedPol=="ZeroKill":
            initPointArrayRep=np.array(initPoint+[0]).reshape(3,-1)
        elif schedPol=="HoldSkip-Next":
            initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
        elif schedPol=="ZeroSkip-Next":
            initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
        else:
            print(">> STATUS: FATAL ERROR - UNIMPLEMENETED!")

        devStat=DevCompStat(systemObj,n,initPointArrayRep,H,schedPol,distro,K_miss,heuName,B,c)

        d_ub,it,tot_time=devStat.mainAlgo()

        return d_ub,it,tot_time

    def varySchedPols(initPoint=[10,10],H=150,distro="K-Miss",K_miss=3,heuName="RandSampKMiss",B=415000,c=0.99):

        schedPols=["HoldKill","ZeroKill","HoldSkip-Next","ZeroSkip-Next"]
        schedPols=["HoldSkip-Next"]
        avgRunTime=[]
        avgItNum=[]
        avgD=[]
        sdD=[]

        for schedPol in schedPols:
            runTime=[]
            refinements=[]
            devs=[]
            for e in range(EPOCH):
                d_ub,it,tot_time=RC.getD(initPoint,H,schedPol,distro,K_miss,heuName,B,c)
                runTime.append(tot_time)
                refinements.append(it)
                devs.append(d_ub)
            avgRunTime.append(stat.mean(runTime))
            avgItNum.append(stat.mean(refinements))
            avgD.append(stat.mean(devs))
            sdD.append(stat.stdev(devs))


        dynA=Benchmarks.DC.A
        dynB=Benchmarks.DC.B
        dynC=Benchmarks.DC.C
        dynD=Benchmarks.DC.D
        K=Benchmarks.DC.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)
        initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
        randSampObj=randSampObj=RandSampling(systemObj,H,schedPol,distro,K_miss)
        nomTraj=randSampObj.getAllHitTraj(initPointArrayRep)
        (s,randSamps)=randSampObj.getSamples(initPointArrayRep,10)
        allMissTraj=randSampObj.getAllMissTraj(initPointArrayRep)

        print("\n\n\n>> RC Network Report")

        for i in range(len(schedPols)):
            print(">>\t Scheduling Policy: ",schedPols[i],";\t Misses: ",K_miss)
            print("\t\t* Avg. Time Taken: ",avgRunTime[i])
            print("\t\t* Avg. Refinements Made: ",avgItNum[i])
            print("\t\t* Avg. Upper Bound d: ",avgD[i])
            print("\t\t* SD. Upper Bound d: ",sdD[i])

        Viz2.vizTrajs(nomTraj,randSamps,avgD[0],fname="rc_network")

    def varyC(initPoint=[10,10],H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=3,heuName="RandSampKMiss",B=415000):
        listC=[]
        listD=[]
        listSDD=[]
        listItNum=[]
        STEP=20
        c=0.51
        stepSize=float((0.99-c)/STEP)

        cDev=[]
        for i in range(STEP):
            #runTime=[]
            #refinements=[]
            #devs=[]
            for e in range(EPOCH):
                d_ub,it,tot_time=RC.getD(initPoint,H,schedPol,distro,K_miss,heuName,B,c)
                #runTime.append(tot_time)
                #refinements.append(it)
                #devs.append(d_ub)
                cDev.append([c,d_ub])
            #listC.append(c)
            #listItNum.append(stat.mean(refinements))
            #listD.append(stat.mean(devs))
            #listSDD.append(stat.stdev(devs))
            c=c+stepSize

        mean_var_df = pd.DataFrame(cDev,columns=['c','dev'])


        Viz2.vizVaryC(mean_var_df,fname="rc")

    def varK_miss(initPoint=[10,10],H=150,schedPol="HoldSkip-Next",distro="K-Miss",heuName="RandSampKMiss",B=415000,c=0.99):
        K_miss_list=[2,4,8,16]
        avgRunTime=[]
        avgItNum=[]
        avgD=[]
        sdD=[]

        for K_miss in K_miss_list:
            runTime=[]
            refinements=[]
            devs=[]
            for e in range(EPOCH):
                d_ub,it,tot_time=RC.getD(initPoint,H,schedPol,distro,K_miss,heuName,B,c)
                runTime.append(tot_time)
                refinements.append(it)
                devs.append(d_ub)
            avgRunTime.append(stat.mean(runTime))
            avgItNum.append(stat.mean(refinements))
            avgD.append(stat.mean(devs))
            sdD.append(stat.stdev(devs))


        print("\n\n\n>> RC Network Report")

        for i in range(len(K_miss_list)):
            print(">>\t Scheduling Policy: ",schedPol,";\t Misses: ",K_miss_list[i])
            print("\t\t* Avg. Time Taken: ",avgRunTime[i])
            print("\t\t* Avg. Refinements Made: ",avgItNum[i])
            print("\t\t* Avg. Upper Bound d: ",avgD[i])
            print("\t\t* SD. Upper Bound d: ",sdD[i])

    def varySchedPolsShowViolation(initPoint=[10,10],H=150,distro="K-Miss",K_miss=3,heuName="RandSampKMiss",B=415000,c=0.99):

        schedPols=["HoldKill","ZeroKill","HoldSkip-Next","ZeroSkip-Next"]
        schedPols=["HoldSkip-Next"]
        avgRunTime=[]
        avgItNum=[]
        avgD=[]
        sdD=[]

        for schedPol in schedPols:
            runTime=[]
            refinements=[]
            devs=[]
            for e in range(EPOCH):
                d_ub,it,tot_time=RC.getD(initPoint,H,schedPol,distro,K_miss,heuName,B,c)
                runTime.append(tot_time)
                refinements.append(it)
                devs.append(d_ub)
            avgRunTime.append(stat.mean(runTime))
            avgItNum.append(stat.mean(refinements))
            avgD.append(stat.mean(devs))
            sdD.append(stat.stdev(devs))


        dynA=Benchmarks.DC.A
        dynB=Benchmarks.DC.B
        dynC=Benchmarks.DC.C
        dynD=Benchmarks.DC.D
        K=Benchmarks.DC.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)
        initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
        randSampObj=randSampObj=RandSampling(systemObj,H,schedPol,distro,K_miss)
        nomTraj=randSampObj.getAllHitTraj(initPointArrayRep)
        (s,randSamps)=randSampObj.getSamples(initPointArrayRep,10)
        allMissTraj=randSampObj.getAllMissTraj(initPointArrayRep)

        uTrajObj=UnsafeTraj(systemObj,initPointArrayRep,H,schedPol,distro,K_miss+1,B,c)
        randSampsVio=uTrajObj.getVioTrajs(avgD[0],1)


        Viz2.vizTrajsVio(nomTraj,randSamps,randSampsVio,avgD[0],fname="rc_network_trajs_vio")








if True:
    initPoint=[10,10]
    H=150
    #RC.varySchedPols(initPoint=[10,10],H=150) # Set Parameter R=50 before executing
    RC.varyC(initPoint=[10,10],H=150) # Set Parameter R=10 before executing
    #RC.varK_miss(initPoint=[10,10],H=150) # Set Parameter R=50 before executing
    #RC.varySchedPolsShowViolation(initPoint=[10,10],H=150) # Set Parameter R=50 before executing
