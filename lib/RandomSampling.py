import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
from lib.SchedulingStrategies import *

class RandSampling:

    def __init__(self,systemObj,H=150,schedPol="HoldSkip-Next",distro="Uniform",K_miss=-1):
        self.systemObj=systemObj
        self.H=H
        self.schedPol=schedPol
        self.distro=distro
        self.K_miss=K_miss

    def getARandSample(self,initPoint):
        # Generate a sequence
        if self.distro=="Uniform":
            seqn=[random.randint(0,1) for i in range(self.H)]
        elif self.distro=="K-Miss":
            seqn=self.getARandSampleKMisses(initPoint)
        else:
            print(">> STATUS: FATAL ERROR - Unimplemented!")
            exit(0)
        # %%%%%%%%%%%%%%%%%%%%%%%%%%

        # Generate trajectory as per seqn
        schdStrat=SchedStrat(self.systemObj)
        traj=schdStrat.getReachSetSeqn(initPoint,seqn)
        return (seqn,traj)

    def getARandSampleKMisses(self,initPoint):
        '''
        Generate a random sample with K consecutive misses
        '''
        seqn=[]

        while True:
            seqn=[random.randint(0,1) for i in range(self.H)]
            fg=RandSampling.isKMiss(seqn,self.K_miss)
            if fg==True:
                return seqn

    def isKMiss(seqn,K_miss):
        '''
        Check if the sample has at most K consecutive misses
        '''
        L=len(seqn)
        for i in range(L):
            subSeq=seqn[i:i+K_miss+1]
            if subSeq==[0]*(K_miss+1):
                return False
        return True




    def getSamples(self,initPoint,K):
        sequences=[]
        trajectories=[]
        for i in range(K):
            seqn,traj=self.getARandSample(initPoint)
            sequences.append(seqn)
            trajectories.append(traj)

        return (sequences,trajectories)

    def getAllHitTraj(self,initPoint):
        schdStrat=SchedStrat(self.systemObj)
        nomTraj=schdStrat.getReachSetSeqn(initPoint,[1]*self.H)
        return nomTraj

    def getAllMissTraj(self,initPoint):
        schdStrat=SchedStrat(self.systemObj)
        nomTraj=schdStrat.getReachSetSeqn(initPoint,[0]*self.H)
        return nomTraj
