import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
from lib.RandomSampling import *
import matplotlib.pyplot as plt

class Viz:

    def vizTrajs(allHitTraj,allMissTraj,d_ub,th1=0,th2=1):
        plt.figure()
        fig, ax = plt.subplots()

        H=len(allHitTraj)

        allHitX=[allHitTraj[t][th1][0] for t in range(H)]
        allHitY=[allHitTraj[t][th2][0] for t in range(H)]
        #plt.plot(allHitX,allHitY,label="All Hit", color='g',markersize=2,linewidth=3)

        #allMissX=[allMissTraj[t][th1][0] for t in range(H)]
        #allMissY=[allMissTraj[t][th2][0] for t in range(H)]
        #plt.plot(allHitX,allHitY,label="All Miss", color='r',markersize=2,linewidth=3)

        for t in range(H):
            0;
            ax.add_patch(plt.Circle((allHitTraj[t][th1][0], allHitTraj[t][th2][0]), d_ub, color='cyan',alpha=1))

        plt.plot(allHitX,allHitY,label="All Hit", color='g',markersize=2,linewidth=3)
        #plt.plot(allMissX,allMissY,label="All Miss", color='r',markersize=2,linewidth=3)

        plt.legend()
        plt.show()
