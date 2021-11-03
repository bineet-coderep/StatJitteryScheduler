import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
from lib.RandomSampling import *
from lib.Deviation import *
import time

class Heuristics:
    def __init__(self,systemObj,dim,initPoint,H=150,schedPol="HoldSkip-Next",distro="Uniform",heuName="RandSamp"):
        self.systemObj=systemObj
        self.H=H
        self.dim=dim
        self.initPoint=initPoint
        self.schedPol=schedPol
        self.distro=distro
        self.heuName=heuName

    def getD(self):
        if self.heuName=="RandSamp":
            return self.getDRandSamp()
        else:
            print(">> STATUS: FATAL ERROR - Unimplemented!")
            exit(0)

    def getDRandSamp(self,K=10,P=1.1):
        '''
        - Generate K random samples
        - Generate all miss trajectories
        - Compute distance from these two sets and bloat by P% and return
        '''
        randSamp=RandSampling(self.systemObj,self.H,self.schedPol,self.distro)


        (s,randTrajs)=randSamp.getSamples(self.initPoint,K)


        nomTraj=randSamp.getAllHitTraj(self.initPoint)

        allMissTraj=randSamp.getAllMissTraj(self.initPoint)


        (d,t)=Deviation.computeDevTrajectories(nomTraj,randTrajs+[allMissTraj],self.dim)


        return d*P
