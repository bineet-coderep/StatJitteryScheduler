import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
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

class DeviationSet:

    def computeDev2(traj1,traj2,dim=2):
        (d1Mx,mx1T)=DeviationSet.computeDevInner(traj1,traj2,dim)
        (d2Mx,mx2T)=DeviationSet.computeDevInner(traj2,traj1,dim)
        d=0
        mxT=0
        if d1Mx>d2Mx:
            d=d1Mx
            mxT=mx1T
        else:
            d=d2Mx
            mxT=mx2T
        return (d,mxT)

    def computeDev(traj1,traj2,dim=2):
        H=len(traj1[0])
        nVert=len(traj1)

        dMx=-np.inf
        mxT=-7
        for t in range(H):
            dt1=-np.inf
            for v in range(nVert):
                #traj1[v][t]
                dv=np.inf
                for v2 in range(nVert):
                    #traj2[v2][t]
                    dd=0
                    for d in range(dim):
                        p=traj1[v][t][d]
                        q=traj2[v2][t][d]
                        dd=dd+((p-q)**2)
                    d_12_v_v2=math.sqrt(dd)
                    if d_12_v_v2<dv:
                        dv=d_12_v_v2
                if dv>dt1:
                    dt1=dv
            dt2=-np.inf
            for v in range(nVert):
                #traj1[v][t]
                dv2=np.inf
                for v2 in range(nVert):
                    #traj2[v2][t]
                    dd=0
                    for d in range(dim):
                        p=traj2[v][t][d]
                        q=traj1[v2][t][d]
                        dd=dd+((p-q)**2)
                    d_12_v_v2=math.sqrt(dd)
                    if d_12_v_v2<dv2:
                        dv2=d_12_v_v2
                if dv2>dt2:
                    dt2=dv2
            dt=max(dt1,dt2)
            if dt>dMx:
                #print(d,dt)
                dMx=dt
                #print(d,dt)
                #print("--")
                mxT=t

        return (dMx,mxT)

    def computeDevTList(traj1,traj2,safeDev,dim=2):
        H=len(traj1[0])
        nVert=len(traj1)

        dTlist=[]

        for t in range(H):
            dt1=-np.inf
            for v in range(nVert):
                #traj1[v][t]
                dv=np.inf
                for v2 in range(nVert):
                    #traj2[v2][t]
                    dd=0
                    for d in range(dim):
                        p=traj1[v][t][d]
                        q=traj2[v2][t][d]
                        dd=dd+((p-q)**2)
                    d_12_v_v2=math.sqrt(dd)
                    if d_12_v_v2<dv:
                        dv=d_12_v_v2
                if dv>dt1:
                    dt1=dv
            dt2=-np.inf
            for v in range(nVert):
                #traj1[v][t]
                dv2=np.inf
                for v2 in range(nVert):
                    #traj2[v2][t]
                    dd=0
                    for d in range(dim):
                        p=traj2[v][t][d]
                        q=traj1[v2][t][d]
                        dd=dd+((p-q)**2)
                    d_12_v_v2=math.sqrt(dd)
                    if d_12_v_v2<dv2:
                        dv2=d_12_v_v2
                if dv2>dt2:
                    dt2=dv2
            dt=max(dt1,dt2)
            if dt>safeDev:
                #print(d,dt)
                #dMx=dt
                #print(d,dt)
                #print("--")
                #mxT=t
                dTlist.append(t)

        return dTlist


    def computeDevInner(traj1,traj2,dim=2):
        '''
        Compute the maximum distance between traj1 and traj2
        '''
        #print("Dim: ",dim)


        H=len(traj1[0])
        nVert=len(traj1)

        #print(nVert)

        #dim=traj1[0].shape[0]

        dMx=-np.inf
        mxT=-7
        for t in range(H):
            dt=-np.inf
            for v in range(nVert):
                #traj1[v][t]
                dv=np.inf
                for v2 in range(nVert):
                    #traj2[v2][t]
                    dd=0
                    for d in range(dim):
                        p=traj1[v][t][d]
                        q=traj2[v2][t][d]
                        dd=dd+((p-q)**2)
                    d_12_v_v2=math.sqrt(dd)
                    if d_12_v_v2<dv:
                        dv=d_12_v_v2
                if dv>dt:
                    dt=dv
            #print(dt)
            if dt>dMx:
                #print(d,dt)
                dMx=dt
                #print(d,dt)
                #print("--")
                mxT=t

        return (dMx,mxT)

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
            (d_i,t_i)=DeviationSet.computeDev(nomTraj,traj,dim)
            if d_i>d:
                #print(traj,ct,"\n\n")
                d=d_i
                tStep=t_i
                ctMax=ct
            ct=ct+1
        #print(ct)

        return (d,tStep)
