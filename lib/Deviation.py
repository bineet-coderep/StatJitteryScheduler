import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
import numpy as np
import math

class Deviation:

    def computeDev(traj1,traj2,dim=2):
        '''
        Compute the maximum distance between traj1 and traj2
        '''

        H=len(traj1)

        #dim=traj1[0].shape[0]

        d=-np.inf
        tStep=-7

        for t in range(H):
            dTmp1=0
            for i in range(dim):
                p=traj1[t][i][0]
                q=traj2[t][i][0]
                dTmp1=dTmp1+((p-q)**2)
            d_t=math.sqrt(dTmp1)
            if d_t>d:
                d=d_t
                tStep=t

        return (d,tStep)

    def computeDevTrajectories(nomTraj,trajs,dim=2):
        '''
        Compute the maximum distance between the set of trajectories trajs
        and nomTraj
        '''

        d=-np.inf
        tStep=-7
        ctMax=-7
        ct=0
        for traj in trajs:
            (d_i,t_i)=Deviation.computeDev(nomTraj,traj,dim)
            if d_i>d:
                #print(traj,ct,"\n\n")
                d=d_i
                tStep=t_i
                ctMax=ct
            ct=ct+1
        #print(ct)

        return (d,tStep)
