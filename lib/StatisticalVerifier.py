import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
from lib.SchedulingStrategies import *
from lib.RandomSampling import *
from lib.Deviation import *
from lib.JFBF import *
import time

class StatVerJFB:

    def __init__(self,systemObj,dim,initSet,H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=-1,B=1000,c=0.99,uncertainty=UNCERTAINTY,u_range=UNCERTAINTY_RANGE):
        self.systemObj=systemObj
        self.H=H
        self.dim=dim
        self.initSet=initSet
        self.schedPol=schedPol
        self.distro=distro
        self.K_miss=K_miss
        self.B=B
        self.c=c
        self.uncertainty=uncertainty
        self.u_range=u_range
        self.JFB_params=JFB(B,c)
        self.randSampObj=RandSampling(self.systemObj,self.H,self.schedPol,self.distro,self.K_miss)

    def isSafe(self,d_ub):
        '''
        Check, using JFB, if d_ub is a correct upper-bound
        '''
        print(">> STATUS: Statistically Verifying . . .")
        time_taken=time.time()
        # Generate random samples according to JFB
        #print(self.JFB_params.K)
        (s,randSamples)=self.randSampObj.getSamples(self.initSet,self.JFB_params.K,self.uncertainty,self.dim,self.u_range)
        nomTraj=self.randSampObj.getAllHitTraj(self.initSet,False,None,None)
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Compute deviation from the samples
        (dSamp,t)=DeviationSet.computeDevTrajectories(nomTraj,randSamples)
        if dSamp>d_ub:
            print("\t* Hypothesis Accepted: ",False)
            print("\t* Time Taken: ",time.time()-time_taken)
            print(">> STATUS: Statistically Verified!!")
            return dSamp
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        print("\t* Hypothesis Accepted: ",True)
        print("\t* Time Taken: ",time.time()-time_taken)
        print(">> STATUS: Statistically Verified!!")
        return True
