import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
from lib.RandomSampling import *
from lib.Deviation import *
import time

class Heuristics:
    def __init__(self,systemObj,dim,initSet,H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=-1,heuName="RandSampKMiss",uncertainty=UNCERTAINTY,u_range=UNCERTAINTY_RANGE):
        self.systemObj=systemObj
        self.H=H
        self.dim=dim
        self.initSet=initSet
        self.schedPol=schedPol
        self.distro=distro
        self.K_miss=K_miss
        self.heuName=heuName
        self.uncertainty=UNCERTAINTY
        self.u_range=UNCERTAINTY_RANGE

    def getD(self):
        if self.heuName=="RandSamp":
            return self.getDRandSamp()
        elif self.heuName=="RandSampKMiss":
            return self.getDRandSampKMiss()
        else:
            print(">> STATUS: FATAL ERROR - Unimplemented!")
            exit(0)

    def getDRandSamp(self,K=R,P=EPSILON):
        '''initPoint
        - Generate K random samples
        - Generate all miss trajectories
        - Compute distance from these two sets and bloat by P% and return
        '''
        randSamp=RandSampling(self.systemObj,self.H,self.schedPol,self.distro,self.K_miss)


        (s,randTrajs)=randSamp.getSamples(self.initSet,K,self.uncertainty,self.dim,self.u_range)

        nomTraj=randSamp.getAllHitTraj(self.initSet,False,None,[0,0])

        #allMissTraj=randSamp.getAllMissTraj(self.initPoint)


        #(d,t)=Deviation.computeDevTrajectories(nomTraj,randTrajs+[allMissTraj],self.dim)
        (d,t)=Deviation.computeDevTrajectories(nomTraj,randTrajs,self.dim)


        return d+PinitPoint

    def getDRandSampKMiss(self,K=R,P=EPSILON):
        '''
        - Generate K random samples
        - Generate all miss trajectories
        - Compute distance from these two sets and bloat by P% and return
        '''
        randSamp=RandSampling(self.systemObj,self.H,self.schedPol,self.distro,self.K_miss)


        #(s,randTrajs)=randSamp.getSamples(self.initSet,K,self.uncertainty,self.dim,self.u_range)



        #nomTraj=randSamp.getAllHitTraj(self.initSet,False,None,[0,0])

        nomTraj=randSamp.getAllMissTraj(self.initSet,False,None,[0,0])


        print(len(nomTraj))
        for t in range(0,4):
            print(nomTraj[0][t])
            print(nomTraj[1][t])
            print(nomTraj[2][t])
            print(nomTraj[3][t])
            print("---")
        exit()



        #allMissTraj=randSamp.getAllMissTraj(self.initPoint)

        (d,t)=DeviationSet.computeDevTrajectories(nomTraj,randTrajs,self.dim)
        #(d,t)=DeviationSet.computeDevTrajectories(nomTraj,[nomTraj],self.dim)

        '''print(s[0])
        print(d)
        exit(0)'''



        '''print(ctMax,d)
        print(s[ctMax],len(s[ctMax]))
        print(randTrajs[ctMax][t])
        print(nomTraj[t])
        exit(0)'''



        return d+P
