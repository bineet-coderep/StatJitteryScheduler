import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
from lib.Heuristics import *
from lib.StatisticalVerifier import *
from lib.JFBF import *
import time

class DevCompStat:
    def __init__(self,systemObj,dim,initPoint,H=150,schedPol="HoldSkip-Next",distro="Uniform",heuName="RandSamp",B=1000,c=0.99):
        self.systemObj=systemObj
        self.H=H
        self.dim=dim
        self.initPoint=initPoint
        self.schedPol=schedPol
        self.distro=distro
        self.heuName=heuName
        self.JFB_params=JFB(B,c)

    def mainAlgo(self,P=1.1):
        '''
        Implements the main Statistical Algorithm
        '''
        print(">> Starting Main Algo.\tSched Policy: ",self.schedPol,".\tDistro: ",self.distro,".\tHeuristic Used: ",self.heuName)

        print("\t>> SUB-STATUS: Computing Initial d")
        time_taken=time.time()
        d_ub=Heuristics(self.systemObj,self.dim,self.initPoint,self.H,self.schedPol,self.distro,self.heuName).getD()
        statVerifier=StatVerJFB(self.systemObj,self.dim,self.initPoint,self.H,self.schedPol,self.distro,self.JFB_params.B,self.JFB_params.c)
        print("\t* d: ",d_ub)
        print("\t* Time Taken: ",time.time()-time_taken)
        print("\t>> SUB-STATUS: Initial d Computed!!")

        print()

        print("\t>> SUB-STATUS: Refinement Starts . . .")
        it=0
        while True:
            print("\t>> SUB-STATUS: Iteration Number: ",it)
            rslt=statVerifier.isSafe(d_ub)
            if rslt!=True:
                d_ub=rslt*P
            else:
                break;
            it=it+1
        print("\t>> SUB-STATUS: Refinement End . . .")

        print("\t* Time Taken: ",time.time()-time_taken)
        print("\t* Refinements Made: ",it)
        print("\t* Upper Bound d: ",d_ub)

        print(">> Main Algo Executed!!")

        return d_ub
