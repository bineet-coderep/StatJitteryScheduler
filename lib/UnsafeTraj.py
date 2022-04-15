from Parameters import *
import random
from lib.SchedulingStrategies import *
from lib.RandomSampling import *
from lib.Deviation import *
from lib.JFBF import *
import time

class UnsafeTraj:

    def __init__(self,systemObj,initPoint,H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=-1,B=1000,c=0.99):
        self.systemObj=systemObj
        self.H=H
        self.initPoint=initPoint
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
            (s,randSamples)=self.randSampObj.getSamples(self.initPoint,self.JFB_params.K)
            nomTraj=self.randSampObj.getAllHitTraj(self.initPoint)
            vioTrajs=[]
            for traj in randSamples:
                (d,t)=Deviation.computeDev(traj,nomTraj)
                if d>safeDev:
                    vioTrajs.append(traj)
                if len(vioTrajs)>=nVio:
                    return vioTrajs
