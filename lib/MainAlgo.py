import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
from lib.Heuristics import *
from lib.StatisticalVerifier import *
from lib.JFBF import *
import time

class DevCompStat:
    def __init__(self,systemObj,dim,initPoint,H=150,schedPol="HoldSkip-Next",distro="K-Miss",K_miss=-1,heuName="RandSampKMiss",B=1000,c=0.99):
        self.systemObj=systemObj
        self.H=H
        self.dim=dim
        self.initPoint=initPoint
        self.schedPol=schedPol
        self.distro=distro
        self.K_miss=K_miss
        self.heuName=heuName
        self.JFB_params=JFB(B,c)

    def mainAlgo(self,P=EPSILON):
        '''
        Implements the main Statistical Algorithm
        '''
        print(">> Starting Main Algo.\tSched Policy: ",self.schedPol,".\tDistro: ",self.distro,".\tHeuristic Used: ",self.heuName)

        print("\t>> SUB-STATUS: Computing Initial d")
        time_taken=time.time()
        d_ub=Heuristics(self.systemObj,self.dim,self.initPoint,self.H,self.schedPol,self.distro,self.K_miss,self.heuName).getD()
        statVerifier=StatVerJFB(self.systemObj,self.dim,self.initPoint,self.H,self.schedPol,self.distro,self.K_miss,self.JFB_params.B,self.JFB_params.c)
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
                d_ub=rslt+P
                #print("\t>> SUB-STATUS: d: ",d_ub)
            else:
                break;
            it=it+1

        tot_time=time.time()-time_taken
        print("\t>> SUB-STATUS: Refinement End . . .")

        print("\t* Time Taken: ",tot_time)
        print("\t* Refinements Made: ",it)
        print("\t* Upper Bound d: ",d_ub)

        print(">> Main Algo Executed!!")

        return d_ub,it,tot_time
