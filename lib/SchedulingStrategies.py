import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import math
import time
import copy
import numpy as np
import random as rd

class SchedStrat:
    '''
    Implements Bounded Tree Based method
    '''
    def __init__(self,systemObj,methodName,uncertainty=UNCERTAINTY,dim=DIM,u_range=UNCERTAINTY_RANGE):
        self.A=systemObj.A # Dynamics
        self.B=systemObj.B # Dynamics
        self.C=systemObj.C # Dynamics
        self.D=systemObj.D # Dynamics
        self.K=systemObj.K # Control
        self.methodName=methodName
        self.uncertainty=uncertainty
        self.u_range=u_range
        self.dim=dim

    def getReachSetSeqn(self,initSet,seqn):
        '''
        Given a sequence, it returns the reachable set
        '''
        if self.methodName=="HoldSkip-Next":
            return self.reachSetHoldSkipNext(initSet,seqn)
        elif self.methodName=="ZeroKill":
            return self.reachSetZeroKill(initSet,seqn)
        elif self.methodName=="HoldKill":
            return self.reachSetHoldKill(initSet,seqn)
        elif self.methodName=="ZeroSkip-Next":
            return self.reachSetZeroSkipNext(initSet,seqn)
        else:
            print(">> STATUS: FATAL ERROR - Unimplemented!")
            exit(0)

    def reachSetHoldSkipNext(self,initSet,seqn):
        rsList=[]
        #print(seqn)
        for initPoint in initSet:
            rsListVert=self.reachSetHoldSkipNext2(initPoint,seqn)
            rsList.append(rsListVert)
            #print("---")
        #exit()
        return rsList

    def reachSetHoldSkipNext2(self,initPoint,seqn):
        p, r = self.B.shape

        # Split apart the two pieces of K, if necessary
        K_x = -self.K[:,0:p]
        if self.K.shape[1] == p + r:
            K_u = -self.K[:,p:p+r+1]
        else:
            K_u = np.zeros((r, r))

        # Hit following hit
        A_HH = np.block([[self.A, np.zeros((p, p)), self.B],
                         [np.zeros((p, 2*p + r))],
                         [K_x, np.zeros((r, p)), K_u]])
        # Hit following miss
        A_MH = np.block([[self.A, np.zeros((p, p)), self.B],
                         [np.zeros((p, 2*p + r))],
                         [np.zeros((r, p)), K_x, K_u]])
        # Miss following hit
        A_HM = np.block([[self.A, np.zeros((p, p)), self.B],
                         [np.eye(p), np.zeros((p, p + r))],
                         [np.zeros((r, 2*p)), np.eye(r)]])
        # Miss following miss
        A_MM = np.block([[self.A, np.zeros((p, p)), self.B],
                         [np.zeros((p, p)), np.eye(p), np.zeros((p, r))],
                         [np.zeros((r, 2*p)), np.eye(r)]])

        rsList=[]

        rsList.append(copy.copy(initPoint))

        t_max=len(seqn)

        rs=np.matmul(A_HH,initPoint)
        rsList.append(copy.copy(rs))



        for t in range(t_max):
            if (t == 0 or seqn[t-1]==1) and seqn[t]==1:
                # Hit-Hit
                A = A_HH
            elif (t == 0 or seqn[t-1]==1) and seqn[t]==0:
                # Hit-Miss
                A = A_HM
            elif seqn[t-1]==0 and seqn[t]==1:
                # Miss-Hit
                A = A_MH
            elif seqn[t-1]==0 and seqn[t]==0:
                # Miss-Hit
                A = A_MM
            rs=np.matmul(A,rs)
            #print(A)

            if self.uncertainty==True:

                # Add uncertainty to `rs`
                rs_pert=np.zeros(rs.shape)
                for i in range(self.dim):
                    rs_pert[i][0]=rd.uniform(self.u_range[0],self.u_range[1])
                rs=rs+rs_pert

            rsList.append(copy.copy(rs))

        return rsList

    def reachSetZeroSkipNext(self,initSet,seqn):
        rsList=[]
        for initPoint in initSet:
            rsListVert=self.reachSetZeroSkipNext2(initPoint,seqn)
            rsList.append(rsListVert)
        return rsList

    def reachSetZeroSkipNext2(self,initPoint,seqn):

        p, r = self.B.shape

        # Split apart the two pieces of K, if necessary
        K_x = -self.K[:,0:p]
        if self.K.shape[1] == p + r:
            K_u = -self.K[:,p:p+r+1]
        else:
            K_u = np.zeros((r, r))

        # Hit following hit
        A_HH = np.block([[self.A, np.zeros((p, p)), self.B],
                         [np.zeros((p, 2*p + r))],
                         [K_x, np.zeros((r, p)), K_u]])
        # Hit following miss
        A_MH = np.block([[self.A, np.zeros((p, p)), self.B],
                         [np.zeros((p, 2*p + r))],
                         [np.zeros((r, p)), K_x, K_u]])
        # Miss following hit
        A_HM = np.block([[self.A, np.zeros((p, p)), self.B],
                         [np.eye(p), np.zeros((p, p + r))],
                         [np.zeros((r, 2*p)), np.zeros((r,r))]])
        # Miss following miss
        A_MM = np.block([[self.A, np.zeros((p, p)), self.B],
                         [np.zeros((p, p)), np.eye(p), np.zeros((p, r))],
                         [np.zeros((r, 2*p)), np.eye(r)]])

        rsList=[]

        rsList.append(copy.copy(initPoint))

        t_max=len(seqn)

        rs=np.matmul(A_HH,initPoint)
        rsList.append(copy.copy(rs))

        for t in range(1,t_max):
            if seqn[t-1]==1 and seqn[t]==1:
                # Hit-Hit
                A = A_HH
            elif seqn[t-1]==1 and seqn[t]==0:
                # Hit-Miss
                A = A_HM
            elif seqn[t-1]==0 and seqn[t]==1:
                # Miss-Hit
                A = A_MH
            elif seqn[t-1]==0 and seqn[t]==0:
                # Miss-Hit
                A = A_MM
            rs=np.matmul(A,rs)
            if self.uncertainty==True:
                # Add uncertainty to `rs`
                rs_pert=np.zeros(rs.shape)
                for i in range(self.dim):
                    rs_pert[i][0]=rd.uniform(self.u_range[0],self.u_range[1])
                rs=rs+rs_pert
            rsList.append(copy.copy(rs))

        return rsList

    def reachSetHoldKill(self,initSet,seqn):
        rsList=[]
        for initPoint in initSet:
            rsListVert=self.reachSetHoldKill2(initPoint,seqn)
            rsList.append(rsListVert)
        return rsList

    def reachSetHoldKill2(self,initPoint,seqn):
        rs=copy.copy(initPoint)
        p=self.A.shape[0]
        r=self.B.shape[1]

        arrZ1=np.zeros((r,r))
        arrZ2=np.zeros((r,p))
        arrI=np.identity(r)

        # Split apart the two pieces of K, if necessary
        K_x = -self.K[:,0:p]
        if self.K.shape[1] == p + r:
            K_u = -self.K[:,p:p+r+1]
        else:
            K_u = np.zeros((r, r))


        A_hit=np.vstack((np.hstack((self.A,self.B)),np.hstack((K_x,K_u))))
        A_miss=np.vstack((np.hstack((self.A,self.B)),np.hstack((arrZ2,arrI))))

        t_max = len(seqn)

        rsList=[]

        rsList.append(copy.copy(initPoint))

        for t in range(1,t_max+1):
            if seqn[t-1]==1:
                # Hit
                A = A_hit
            else:
                # Miss
                A = A_miss;
            rs=np.matmul(A,rs)
            if self.uncertainty==True:
                # Add uncertainty to `rs`
                rs_pert=np.zeros(rs.shape)
                for i in range(self.dim):
                    rs_pert[i][0]=rd.uniform(self.u_range[0],self.u_range[1])
                rs=rs+rs_pert
            rsList.append(copy.copy(rs))

        #np.set_printoptions(precision=3)
        #print(x)
        #exit(0)
        return rsList

    def reachSetZeroKill(self,initSet,seqn):
        rsList=[]
        for initPoint in initSet:
            rsListVert=self.reachSetZeroKill2(initPoint,seqn)
            rsList.append(rsListVert)
        return rsList

    def reachSetZeroKill2(self,initPoint,seqn):
        rs=copy.copy(initPoint)
        p=self.A.shape[0]
        r=self.B.shape[1]

        arrZ1=np.zeros((r,r))
        arrZ2=np.zeros((r,p))

        t_max = len(seqn)

        K_x = -self.K[:,0:p]
        # Split apart the two pieces of K, if necessary
        if self.K.shape[1] == p + r:
            K_u = -self.K[:,p:p+r+1]
        else:
            K_u = np.zeros((r, r))
        A_hit=np.vstack((np.hstack((self.A,self.B)),np.hstack((K_x,K_u))))
        A_miss=np.vstack((np.hstack((self.A,self.B)),np.hstack((arrZ2,arrZ1))))

        rsList=[]

        rsList.append(copy.copy(initPoint))

        for t in range(1,t_max+1):
            if seqn[t-1]==1:
                # Hit
                A = A_hit
            else:
                # Miss
                A = A_miss;
            rs=np.matmul(A,rs)
            if self.uncertainty==True:
                # Add uncertainty to `rs`
                rs_pert=np.zeros(rs.shape)
                for i in range(self.dim):
                    rs_pert[i][0]=rd.uniform(self.u_range[0],self.u_range[1])
                rs=rs+rs_pert
            rsList.append(copy.copy(rs))

        #np.set_printoptions(precision=3)
        #print(x)
        #exit(0)
        return rsList
