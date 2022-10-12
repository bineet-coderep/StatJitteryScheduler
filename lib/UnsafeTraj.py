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

class UnsafeTraj:

    def __init__(self,systemObj,initSet,H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=-1,B=1000,c=0.99):
        self.systemObj=systemObj
        self.H=H
        self.initSet=initSet
        self.schedPol=schedPol
        self.distro=distro
        self.K_miss=K_miss
        self.B=B
        self.c=c
        self.JFB_params=JFB(B,c)
        self.randSampObj=RandSampling(self.systemObj,self.H,self.schedPol,self.distro,self.K_miss)

    def getVioTrajs(self,safeDev,nVio=5):
        # nVio: Number of violating trajectories

        while True:
            (s,randSamples)=self.randSampObj.getSamples(self.initSet,self.JFB_params.K)
            nomTraj=self.randSampObj.getAllHitTraj(self.initSet)
            vioTrajs=[]
            vioT=[]
            for traj in randSamples:
                (d,t)=DeviationSet.computeDev(traj,nomTraj)
                if d>safeDev:
                    vioTrajs.append(traj)
                    vioT.append(t)
                if len(vioTrajs)>=nVio:
                    return (vioTrajs,vioT)
