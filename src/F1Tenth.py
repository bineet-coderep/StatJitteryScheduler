import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
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

class F1Tenth:

    def getD(initSet=[[10,10],[12,10],[12,12],[10,12]],H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=3,heuName="RandSampKMiss",B=415000,c=0.99):
        dynA=Benchmarks.F1Tenth.A
        dynB=Benchmarks.F1Tenth.B
        dynC=Benchmarks.F1Tenth.C
        dynD=Benchmarks.F1Tenth.D
        K=Benchmarks.F1Tenth.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)

        initPointArrayReps=[]

        if schedPol=="HoldKill" or schedPol=="ZeroKill":
            for initPoint in initSet:
                initPointArrayRep=np.array(initPoint+[0]).reshape(3,-1)
                initPointArrayReps.append(initPointArrayRep)
        elif schedPol=="HoldSkip-Next" or schedPol=="ZeroSkip-Next":
            for initPoint in initSet:
                initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
                initPointArrayReps.append(initPointArrayRep)
        else:
            print(">> STATUS: FATAL ERROR - UNIMPLEMENETED!")

        devStat=DevCompStat(systemObj,n,initPointArrayReps,H,schedPol,distro,K_miss,heuName,B,c)

        d_ub,it,tot_time=devStat.mainAlgo()

        return d_ub,it,tot_time

    def varySchedPols(initSet=[[10,10],[12,10],[12,12],[10,12]],H=150,distro="K-Miss",K_miss=3,heuName="RandSampKMiss",B=415000,c=0.99):

        schedPols=["HoldKill","ZeroKill","HoldSkip-Next","ZeroSkip-Next"]
        #schedPols=["HoldSkip-Next"]
        avgRunTime=[]
        avgItNum=[]
        avgD=[]
        sdD=[]

        for schedPol in schedPols:
            runTime=[]
            refinements=[]
            devs=[]
            for e in range(EPOCH):
                #print("++++++++")
                d_ub,it,tot_time=F1Tenth.getD(initSet,H,schedPol,distro,K_miss,heuName,B,c)
                runTime.append(tot_time)
                refinements.append(it)
                devs.append(d_ub)
            avgRunTime.append(stat.mean(runTime))
            avgItNum.append(stat.mean(refinements))
            avgD.append(stat.mean(devs))
            sdD.append(stat.stdev(devs))


        dynA=Benchmarks.F1Tenth.A
        dynB=Benchmarks.F1Tenth.B
        dynC=Benchmarks.F1Tenth.C
        dynD=Benchmarks.F1Tenth.D
        K=Benchmarks.F1Tenth.K
        n=dynA.shape[0]
        initPointArrayReps=[]
        systemObj=System(dynA,dynB,dynC,dynD,K)
        if schedPol=="HoldKill" or schedPol=="ZeroKill":
            for initPoint in initSet:
                initPointArrayRep=np.array(initPoint+[0]).reshape(3,-1)
                initPointArrayReps.append(initPointArrayRep)
        elif schedPol=="HoldSkip-Next" or schedPol=="ZeroSkip-Next":
            for initPoint in initSet:
                initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
                initPointArrayReps.append(initPointArrayRep)
        else:
            print(">> STATUS: FATAL ERROR - UNIMPLEMENETED!")
        randSampObj=randSampObj=RandSampling(systemObj,H,schedPol,distro,K_miss)
        nomTraj=randSampObj.getAllHitTraj(initPointArrayReps)
        (s,randSamps)=randSampObj.getSamples(initPointArrayReps,10,UNCERTAINTY,n,UNCERTAINTY_RANGE)
        allMissTraj=randSampObj.getAllMissTraj(initPointArrayReps)

        print("\n\n\n>> F1Tenth  Report")

        for i in range(len(schedPols)):
            print(">>\t Scheduling Policy: ",schedPols[i],";\t Misses: ",K_miss)
            print("\t\t* Avg. Time Taken: ",avgRunTime[i])
            print("\t\t* Avg. Refinements Made: ",avgItNum[i])
            print("\t\t* Avg. Upper Bound d: ",avgD[i])
            print("\t\t* SD. Upper Bound d: ",sdD[i])

        #Viz2.vizTrajs(nomTraj,randSamps,avgD[0],fname="F1Tenth_Trajs")

    def varyC(initSet=[[10,10],[12,10],[12,12],[10,12]],H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=3,heuName="RandSampKMiss",B=415000):
        listC=[]
        listD=[]
        listSDD=[]
        listItNum=[]
        STEP=20
        c=0.55
        stepSize=float((0.99-c)/STEP)

        cDev=[]

        for i in range(STEP):
            #runTime=[]
            #refinements=[]
            #devs=[]
            for e in range(EPOCH):
                d_ub,it,tot_time=F1Tenth.getD(initSet,H,schedPol,distro,K_miss,heuName,B,c)
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

        Viz2.vizVaryC(mean_var_df,fname="F1Tenth_varC")

    def varK_miss(initSet=[[10,10],[12,10],[12,12],[10,12]],H=150,schedPol="HoldSkip-Next",distro="K-Miss",heuName="RandSampKMiss",B=415000,c=0.99):
        K_miss_list=[2,4,8,16]
        #K_miss_list=[1,2,3,4]
        avgRunTime=[]
        avgItNum=[]
        avgD=[]
        sdD=[]

        for K_miss in K_miss_list:
            runTime=[]
            refinements=[]
            devs=[]
            for e in range(EPOCH):
                d_ub,it,tot_time=F1Tenth.getD(initSet,H,schedPol,distro,K_miss,heuName,B,c)
                runTime.append(tot_time)
                refinements.append(it)
                devs.append(d_ub)
            avgRunTime.append(stat.mean(runTime))
            avgItNum.append(stat.mean(refinements))
            avgD.append(stat.mean(devs))
            sdD.append(stat.stdev(devs))


        print("\n\n\n>> F1Tenth Network Report")

        for i in range(len(K_miss_list)):
            print(">>\t Scheduling Policy: ",schedPol,";\t Misses: ",K_miss_list[i])
            print("\t\t* Avg. Time Taken: ",avgRunTime[i])
            print("\t\t* Avg. Refinements Made: ",avgItNum[i])
            print("\t\t* Avg. Upper Bound d: ",avgD[i])
            print("\t\t* SD. Upper Bound d: ",sdD[i])

    def varySchedPolsShowViolation(initSet=[[10,10],[12,10],[12,12],[10,12]],H=150,distro="K-Miss",K_miss=1,heuName="RandSampKMiss",B=415000,c=0.99):

        #schedPols=["HoldKill","ZeroKill","HoldSkip-Next","ZeroSkip-Next"]
        schedPols=["HoldSkip-Next"]
        schedPol="HoldSkip-Next"
        avgRunTime=[]
        avgItNum=[]
        avgD=[]
        sdD=[]

        '''
        for schedPol in schedPols:
            runTime=[]
            refinements=[]
            devs=[]
            for e in range(EPOCH):
                #print("++++++++")
                d_ub,it,tot_time=F1Tenth.getD(initSet,H,schedPol,distro,K_miss,heuName,B,c)
                runTime.append(tot_time)
                refinements.append(it)
                devs.append(d_ub)
            avgRunTime.append(stat.mean(runTime))
            avgItNum.append(stat.mean(refinements))
            avgD.append(stat.mean(devs))
            sdD.append(stat.stdev(devs))
        '''

        dynA=Benchmarks.F1Tenth.A
        dynB=Benchmarks.F1Tenth.B
        dynC=Benchmarks.F1Tenth.C
        dynD=Benchmarks.F1Tenth.D
        K=Benchmarks.F1Tenth.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)

        initPointArrayReps=[]
        if schedPol=="HoldKill" or schedPol=="ZeroKill":
            for initPoint in initSet:
                initPointArrayRep=np.array(initPoint+[0]).reshape(3,-1)
                initPointArrayReps.append(initPointArrayRep)
        elif schedPol=="HoldSkip-Next" or schedPol=="ZeroSkip-Next":
            for initPoint in initSet:
                initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
                initPointArrayReps.append(initPointArrayRep)
        else:
            print(">> STATUS: FATAL ERROR - UNIMPLEMENETED!")


        randSampObj=randSampObj=RandSampling(systemObj,H,schedPol,distro,K_miss)
        nomTraj=randSampObj.getAllHitTraj(initPointArrayReps)
        (s,randSamps)=randSampObj.getSamples(initPointArrayReps,10,UNCERTAINTY,n,UNCERTAINTY_RANGE)
        allMissTraj=randSampObj.getAllMissTraj(initPointArrayReps)

        #print("C1")


        uTrajObj=UnsafeTraj(systemObj,initPointArrayReps,H,schedPol,distro,K_miss+1,B,c,UNCERTAINTY,n,UNCERTAINTY_RANGE)
        #randSampsVio,vioT=uTrajObj.getVioTrajs(avgD[0]+2,1)
        randSampsVio,vioT=uTrajObj.getVioTrajs(17.1+2,1)

        #print("C2")


        #Viz2.vizTrajsVio(nomTraj,randSamps,randSampsVio,vioT,avgD[0],fname="F1Tenth_Trajs")
        Viz2.vizTrajsVio(nomTraj,randSamps,randSampsVio,vioT,17.1,fname="F1Tenth_Trajs")










if True:
    initSet=[[10,10],[12,10],[12,12],[10,12]]
    #initSet=[[10,10],[10,10],[10,10],[10,10]]
    H=150
    #F1Tenth.getD(initSet,schedPol="HoldKill")
    #F1Tenth.varySchedPols(initSet,H=150,K_miss=3,c=0.99) # Set Parameter R=50 before executing
    #F1Tenth.varyC(initSet,H=150,K_miss=3) # Set Parameter R=10 before executing
    F1Tenth.varK_miss(initSet,H=150) # Set Parameter R=50 before executing
    #F1Tenth.getD(initPoint=[10,10],H=150,schedPol="HoldKill",c=0.9999) # Set Parameter R=50 before executing
    #F1Tenth.varySchedPolsShowViolation(initSet,H=150,K_miss=3) # Set Parameter R=50 before executing
