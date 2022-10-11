import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
from lib.Benchmarks import *
from lib.MainAlgo import *
from lib.System import *
from lib.RandomSampling import *
from lib.Visualization import *

class Exp:

    def test0(initSet=[[10,10],[12,10],[12,12],[10,12]],H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=3,heuName="RandSampKMiss",B=415000,c=0.99):
        initSet=[[10,10],[10,10],[10,10],[10,10]]
        dynA=Benchmarks.DC.A
        dynB=Benchmarks.DC.B
        dynC=Benchmarks.DC.C
        dynD=Benchmarks.DC.D
        K=Benchmarks.DC.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)

        initPointArrayReps=[]
        for initPoint in initSet:
            initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
            initPointArrayReps.append(initPointArrayRep)

        devStat=DevCompStat(systemObj,n,initPointArrayReps,H,schedPol,distro,K_miss,heuName,B,c)

        d_ub=devStat.mainAlgo()

        exit()

        randSampObj=randSampObj=RandSampling(systemObj,H,schedPol,distro,K_miss)
        nomTraj=randSampObj.getAllHitTraj(initPointArrayReps)
        (s,randSamps)=randSampObj.getSamples(initPointArrayReps,10)
        allMissTraj=randSampObj.getAllMissTraj(initPointArrayReps)

        Viz2.vizTrajs(nomTraj,randSamps,2)
        exit(0)

    def test1(initPoint=[10,10],H=150,schedPol="ZeroSkip-Next",distro="K-Miss",K_miss=3,heuName="RandSampKMiss",B=1000,c=0.99):
        dynA=Benchmarks.Steering.A
        dynB=Benchmarks.Steering.B
        dynC=Benchmarks.Steering.C
        dynD=Benchmarks.Steering.D
        K=Benchmarks.Steering.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)

        initPointArrayRep=np.array(initPoint+[0,0,0,0]).reshape(6,-1)
        devStat=DevCompStat(systemObj,n,initPointArrayRep,H,schedPol,distro,K_miss,heuName,B,c)

        d_ub=devStat.mainAlgo()

        randSampObj=randSampObj=RandSampling(systemObj,H,schedPol,distro,K_miss)
        nomTraj=randSampObj.getAllHitTraj(initPointArrayRep)
        allMissTraj=randSampObj.getAllMissTraj(initPointArrayRep)
        (s,randSamps)=randSampObj.getSamples(initPointArrayRep,10)
        Viz.vizTrajs(nomTraj,randSamps,d_ub)

    def test2(initPoint=[10,10],H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=10,heuName="RandSampKMiss",B=1000,c=0.99):
        dynA=Benchmarks.ECRTS21.A
        dynB=Benchmarks.ECRTS21.B
        dynC=Benchmarks.ECRTS21.C
        dynD=Benchmarks.ECRTS21.D
        K=Benchmarks.ECRTS21.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)

        initPointArrayRep=np.array(initPoint+[0,0,0,0]).reshape(6,-1)
        devStat=DevCompStat(systemObj,n,initPointArrayRep,H,schedPol,distro,K_miss,heuName,B,c)

        d_ub=devStat.mainAlgo()

        randSampObj=randSampObj=RandSampling(systemObj,H,schedPol,distro,K_miss)
        nomTraj=randSampObj.getAllHitTraj(initPointArrayRep)
        allMissTraj=randSampObj.getAllMissTraj(initPointArrayRep)
        (s,randSamps)=randSampObj.getSamples(initPointArrayRep,10)
        Viz.vizTrajs(nomTraj,randSamps,d_ub)



if True:
    Exp.test0()
