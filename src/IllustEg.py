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

class IllustEg:

    def getD(initPoint=[10,10],H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=1,heuName="RandSampKMiss",B=415000,c=0.99):
        dynA=Benchmarks.IllustEg.A
        dynB=Benchmarks.IllustEg.B
        dynC=Benchmarks.IllustEg.C
        dynD=Benchmarks.IllustEg.D
        K=Benchmarks.IllustEg.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)


        if schedPol=="HoldKill":
            initPointArrayRep=np.array(initPoint+[0,0]).reshape(4,-1)
        elif schedPol=="ZeroKill":
            initPointArrayRep=np.array(initPoint+[0,0]).reshape(4,-1)
        elif schedPol=="HoldSkip-Next":
            initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
        elif schedPol=="ZeroSkip-Next":
            initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
        else:
            print(">> STATUS: FATAL ERROR - UNIMPLEMENETED!")

        devStat=DevCompStat(systemObj,n,initPointArrayRep,H,schedPol,distro,K_miss,heuName,B,c)

        d_ub,it,tot_time=devStat.mainAlgo()

        return d_ub,it,tot_time

    def varySchedPols(initPoint=[10,10],H=150,distro="K-Miss",K_miss=1,heuName="RandSampKMiss",B=415000,c=0.99):

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
                d_ub,it,tot_time=IllustEg.getD(initPoint,H,schedPol,distro,K_miss,heuName,B,c)
                runTime.append(tot_time)
                refinements.append(it)
                devs.append(d_ub)
            avgRunTime.append(stat.mean(runTime))
            avgItNum.append(stat.mean(refinements))
            avgD.append(stat.mean(devs))
            sdD.append(stat.stdev(devs))


        dynA=Benchmarks.IllustEg.A
        dynB=Benchmarks.IllustEg.B
        dynC=Benchmarks.IllustEg.C
        dynD=Benchmarks.IllustEg.D
        K=Benchmarks.IllustEg.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)
        initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
        randSampObj=randSampObj=RandSampling(systemObj,H,schedPol,distro,K_miss)
        nomTraj=randSampObj.getAllHitTraj(initPointArrayRep)
        (s,randSamps)=randSampObj.getSamples(initPointArrayRep,10)
        allMissTraj=randSampObj.getAllMissTraj(initPointArrayRep)

        print("\n\n\n>> IllustEg Network Report")

        for i in range(len(schedPols)):
            print(">>\t Scheduling Policy: ",schedPols[i],";\t Misses: ",K_miss)
            print("\t\t* Avg. Time Taken: ",avgRunTime[i])
            print("\t\t* Avg. Refinements Made: ",avgItNum[i])
            print("\t\t* Avg. Upper Bound d: ",avgD[i])
            print("\t\t* SD. Upper Bound d: ",sdD[i])

        Viz2.vizTrajs(nomTraj,randSamps,avgD[0],fname="IllustEg")










if True:
    initPoint=[100,100]
    H=5
    #IllustEg.varySchedPols(initPoint=[100,100],H=5,K_miss=2) # Set Parameter R=50 before executing
    #ECRTS21.varyC(initPoint=[10,10],H=150) # Set Parameter R=10 before executing
    IllustEg.getD(initPoint=[10,10],H=5,K_miss=2) # Set Parameter R=50 before executing
