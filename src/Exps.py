import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
from lib.Benchmarks import *
from lib.MainAlgo import *
from lib.System import *
from lib.RandomSampling import *
from lib.Visualization import *

class Exp:

    def test0(initPoint=[10,10],H=150,schedPol="HoldSkip-Next",distro="Uniform"):
        A=Benchmarks.DC.A
        B=Benchmarks.DC.B
        C=Benchmarks.DC.C
        D=Benchmarks.DC.D
        K=Benchmarks.DC.K
        n=A.shape[0]
        systemObj=System(A,B,C,D,K)

        initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)

        randSamp=RandSampling(systemObj,H,schedPol,distro)

        (s,randTrajs)=randSamp.getSamples(initPointArrayRep,1000)

        nomTraj=randSamp.getAllHitTraj(initPointArrayRep)

        d=Deviation.computeDevTrajectories(nomTraj,randTrajs,n)

        print(d)

    def test1(initPoint=[10,10],H=150,schedPol="HoldSkip-Next",distro="Uniform",heuName="RandSamp",B=1000,c=0.99):
        dynA=Benchmarks.DC.A
        dynB=Benchmarks.DC.B
        dynC=Benchmarks.DC.C
        dynD=Benchmarks.DC.D
        K=Benchmarks.DC.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)

        initPointArrayRep=np.array(initPoint+[0,0,0]).reshape(5,-1)
        devStat=DevCompStat(systemObj,n,initPointArrayRep,H,schedPol,distro,heuName,B,c)

        d_ub=devStat.mainAlgo()

        randSampObj=randSampObj=RandSampling(systemObj,H,schedPol,distro)
        nomTraj=randSampObj.getAllHitTraj(initPointArrayRep)
        allMissTraj=randSampObj.getAllMissTraj(initPointArrayRep)
        Viz.vizTrajs(nomTraj,allMissTraj,d_ub)

    def test2(initPoint=[10,10],H=150,schedPol="HoldSkip-Next",distro="Uniform",heuName="RandSamp",B=1000,c=0.99):
        dynA=Benchmarks.Steering.A
        dynB=Benchmarks.Steering.B
        dynC=Benchmarks.Steering.C
        dynD=Benchmarks.Steering.D
        K=Benchmarks.Steering.K
        n=dynA.shape[0]
        systemObj=System(dynA,dynB,dynC,dynD,K)

        initPointArrayRep=np.array(initPoint+[0,0,0,0]).reshape(6,-1)
        devStat=DevCompStat(systemObj,n,initPointArrayRep,H,schedPol,distro,heuName,B,c)

        d_ub=devStat.mainAlgo()

        randSampObj=randSampObj=RandSampling(systemObj,H,schedPol,distro)
        nomTraj=randSampObj.getAllHitTraj(initPointArrayRep)
        allMissTraj=randSampObj.getAllMissTraj(initPointArrayRep)
        Viz.vizTrajs(nomTraj,allMissTraj,d_ub)






if True:
    Exp.test1()
