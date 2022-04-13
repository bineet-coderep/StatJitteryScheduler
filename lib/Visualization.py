import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
from lib.RandomSampling import *
import matplotlib.pyplot as plt

class Viz2:

    def vizTrajs(allHitTraj,randTrajs,d_ub,th1=0,th2=1,fname="benchmark"):
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

        #plt.plot(allMissX,allMissY,label="All Miss", color='r',markersize=2,linewidth=3)
        for traj in randTrajs:
            X=[traj[t][th1][0] for t in range(H)]
            Y=[traj[t][th2][0] for t in range(H)]
            plt.plot(X,Y, color='r',markersize=1,linewidth=1,linestyle='--')

        plt.plot(allHitX,allHitY,label="All Hit", color='g',markersize=2,linewidth=3)

        #plt.legend()
        #plt.show()
        plt.savefig(OUTPUT_PATH+'/'+fname+"_safety_envelope"+'.pdf', format='pdf')

    def get_colors(n):
        return list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF),range(n)))

    def vizTrajsAllPols(allHitTraj,randTrajs,labels,d_ubs,th1=0,th2=1):
        plt.figure()
        fig, ax = plt.subplots()

        H=len(allHitTraj)
        L=len(labels)
        clrs=Viz.get_colors(L)

        allHitX=[allHitTraj[t][th1][0] for t in range(H)]
        allHitY=[allHitTraj[t][th2][0] for t in range(H)]

        for i in range(L):
            d_ub=d_ubs[i]
            label=labels[i]
            print(d_ub,label)
            for t in range(H):
                circ=plt.Circle((allHitTraj[t][th1][0], allHitTraj[t][th2][0]), d_ub ,alpha=0.2, color=clrs[i])
                ax.add_patch(circ)

            #plt.plot(allMissX,allMissY,label="All Miss", color='r',markersize=2,linewidth=3)
        for traj in randTrajs:
            X=[traj[t][th1][0] for t in range(H)]
            Y=[traj[t][th2][0] for t in range(H)]
            plt.plot(X,Y, color='r',markersize=1,linewidth=1,linestyle='--')

        plt.plot(allHitX,allHitY,label="All Hit", color='g',markersize=2,linewidth=3)

        #plt.legend()
        plt.show()

    def vizVaryC(listC,listD,listVar,listItNum,fname="benchmark"):

        plt.figure()
        plt.xlabel("c",fontsize=21)
        plt.ylabel("Max. Deviation",fontsize=21)
        #plt.ylabel("Deviation and Refi",fontsize=20)

        err_up = [a + b for a, b in zip(listD, listVar)]
        err_down = [a - b for a, b in zip(listD, listVar)]
        plt.plot(listC,err_up,color='cyan',label="SD")
        plt.plot(listC,err_down,color='cyan')
        plt.plot(listC,listD,label="Mean")
        #plt.plot(listC,listItNum,label="Refinements")

        plt.legend(fontsize=20)
        plt.savefig(OUTPUT_PATH+'/'+fname+'_varyC.pdf', format='pdf')


class Viz:

    def plotSafetyEnv(nominalRS,dList,maxT,safeDev,fname):
        th1=0
        th2=1

        plt.figure()
        fig, ax = plt.subplots()
        nominal=SetOp.getSimpleRep(nominalRS)
        H=len(nominal)
        nominalX=[nominal[t][th1] for t in range(H)]
        nominalY=[nominal[t][th2] for t in range(H)]

        for t in range(H):
            #print(nominal[t][th1],nominal[t][th2])
            circ1=ax.add_patch(plt.Circle((nominal[t][th1], nominal[t][th2]), safeDev, color='cyan',alpha=1))
            ax.add_patch(circ1)

        for t in range(H):
            circ2=ax.add_patch(plt.Circle((nominal[t][th1], nominal[t][th2]), dList[t], color='green',alpha=0.2))
            ax.add_patch(circ2)

        for t in range(H):
            if dList[t]>safeDev:
                #plt.scatter(nominal[t][th1], nominal[t][th2],marker='X',markersize=3,color='r')
                circ2=ax.add_patch(plt.Circle((nominal[t][th1], nominal[t][th2]), dList[t], color='red',alpha=0.2))
                ax.add_patch(circ2)

        plt.plot(nominalX,nominalY,color='k',markersize=2,linewidth=3)

        plt.show()
        ax.savefig(OUTPUT_PATH+'/'+fname+"_safety_envelope"+'.pdf', format='pdf')
