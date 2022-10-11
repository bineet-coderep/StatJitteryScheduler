import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
from lib.SchedulingStrategies import *
import numpy.random as nrd
import time


class RandSampling:

    def __init__(self,systemObj,H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=-1,rand_samp_met=RAND_SAMP_MET):
        self.systemObj=systemObj
        self.H=H
        self.schedPol=schedPol
        self.distro=distro
        self.K_miss=K_miss
        self.rand_samp_met=RAND_SAMP_MET
        if self.rand_samp_met=="RGA":
            self.l=self.buildLengthDict()

    def getARandSample(self,initSet):
        # Generate a sequence
        random.seed(time.time())
        if self.distro=="Uniform":
            seqn=[random.randint(0,1) for i in range(self.H)]
        elif self.distro=="K-Miss":
            seqn=self.getARandSampleKMisses()
        else:
            print(">> STATUS: FATAL ERROR - Unimplemented!")
            exit(0)
        # %%%%%%%%%%%%%%%%%%%%%%%%%%

        # Generate trajectory as per seqn
        schdStrat=SchedStrat(self.systemObj,self.schedPol)
        traj=schdStrat.getReachSetSeqn(initSet,seqn)
        return (seqn,traj)


    def getARandSampleKMisses(self):
        if RAND_SAMP_MET=="Discard":
            return self.getARandSampleKMissesDiscard()
        elif RAND_SAMP_MET=="RGA":
            return self.getARandSampleKMissesRGA()


    def getARandSampleKMissesRGA(self):
        q=0
        seqn=[]
        for i in range(1,self.H+1):
            d=self.l[q,self.H-i+1]
            if q==self.K_miss+1:
                prob_one=self.l[q,self.H-i]/d # probability of choosing one
            else:
                prob_one=self.l[0,self.H-i]/d # probability of choosing one
            rand_bit=nrd.binomial(1,prob_one)
            #print(prob_one)
            seqn.append(rand_bit)
            if rand_bit==1:
                if q==self.K_miss+1:
                    q=q
                else:
                    q=0
            else:
                if q==self.K_miss+1:
                    q=q
                else:
                    q=q+1

        return seqn

    def buildLengthDict(self):
        l={}
        for q in range(self.K_miss+2):
            if q==self.K_miss+1:
                # dummy state
                l[(q,0)]=0
            else:
                # all other states
                l[(q,0)]=1

        for i in range(1,self.H+1):
            for q in range(self.K_miss+2):
                if q==self.K_miss+1:
                    z=l[(q,i-1)]
                    o=l[(q,i-1)]
                else:
                    z=l[(q+1,i-1)]
                    o=l[(0,i-1)]

                l[(q,i)]=z+o

        return l


    def getARandSampleKMissesDiscard(self):
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




    def getSamples(self,initSet,K):
        sequences=[]
        trajectories=[]
        for i in range(K):
            seqn,traj=self.getARandSample(initSet)
            sequences.append(seqn)
            trajectories.append(traj)

        return (sequences,trajectories)

    def getAllHitTraj(self,initSet):
        schdStrat=SchedStrat(self.systemObj,self.schedPol)
        nomTraj=schdStrat.getReachSetSeqn(initSet,[1]*self.H)
        return nomTraj

    def getAllMissTraj(self,initSet):
        schdStrat=SchedStrat(self.systemObj,self.schedPol)
        nomTraj=schdStrat.getReachSetSeqn(initSet,[0]*self.H)
        return nomTraj
