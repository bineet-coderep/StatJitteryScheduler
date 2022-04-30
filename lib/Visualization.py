import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import random
from lib.RandomSampling import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.art3d as art3d
import seaborn as sns

class Viz2:

    def vizTrajs(allHitTraj,randTrajs,d_ub,th1=0,th2=1,fname="benchmark"):
        plt.figure()
        ax = plt.axes(projection='3d')
        #fig = plt.subplots()

        H=len(allHitTraj)

        ax.set_xlabel(r'$\mathbf{x_0}$',fontsize=12)
        ax.set_ylabel(r'$\mathbf{x_1}$',fontsize=12)
        ax.set_zlabel('time',fontsize=11,fontweight='bold')

        #ax.set_xlim(-25, 25)
        #ax.set_ylim(-30, 30)

        allHitX=[allHitTraj[t][th1][0] for t in range(H)]
        allHitY=[allHitTraj[t][th2][0] for t in range(H)]
        Z=list(range(H))
        #plt.plot(allHitX,allHitY,label="All Hit", color='g',markersize=2,linewidth=3)

        #allMissX=[allMissTraj[t][th1][0] for t in range(H)]
        #allMissY=[allMissTraj[t][th2][0] for t in range(H)]
        #plt.plot(allHitX,allHitY,label="All Miss", color='r',markersize=2,linewidth=3)

        for t in range(H):
            0;
            p = plt.Circle((allHitTraj[t][th1][0], allHitTraj[t][th2][0]), d_ub, facecolor='none', edgecolor='cyan',linewidth=0.4,alpha=0.5)
            ax.add_patch(p)
            art3d.pathpatch_2d_to_3d(p, z=t, zdir="z")




        #plt.plot(allMissX,allMissY,label="All Miss", color='r',markersize=2,linewidth=3)
        for traj in randTrajs:
            X=[traj[t][th1][0] for t in range(H)]
            Y=[traj[t][th2][0] for t in range(H)]
            #Z=list(range(H))
            ax.plot3D(X,Y,Z, color='k',markersize=1,linewidth=1,linestyle='--')

        plt.plot(allHitX,allHitY,Z,label="All Hit", color='g',markersize=2,linewidth=3)

        #plt.legend()
        #plt.show()
        #plt.savefig(OUTPUT_PATH+'/'+fname+"_safety_envelope"+'.pdf', format='pdf')

        #plt.legend()
        #plt.show()
        plt.savefig(OUTPUT_PATH+'/'+fname+"_safety_envelope"+'.pdf', format='pdf',bbox_inches='tight',pad_inches = 0,transparent = True)

    def vizTrajs2D(allHitTraj,randTrajs,d_ub,th1=0,th2=1,fname="benchmark"):
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
            plt.plot(X,Y, color='k',markersize=1,linewidth=1,linestyle='--')

        plt.plot(allHitX,allHitY,label="All Hit", color='g',markersize=2,linewidth=3)

        #plt.legend()
        #plt.show()
        plt.savefig(OUTPUT_PATH+'/'+fname+"_safety_envelope"+'.pdf', format='pdf')

    def vizTrajsVio(allHitTraj,randTrajs,randTrajsVio,vioT,d_ub,th1=0,th2=1,fname="benchmark"):
        plt.figure()
        ax = plt.axes(projection='3d')
        #fig = plt.subplots()

        H=len(allHitTraj)

        ax.set_xlabel(r'$\mathbf{x_0}$',fontsize=12)
        ax.set_ylabel(r'$\mathbf{x_1}$',fontsize=12)
        ax.set_zlabel('time',fontsize=11,fontweight='bold')

        #ax.set_xlim(-25, 25)
        #ax.set_ylim(-30, 30)

        allHitX=[allHitTraj[t][th1][0] for t in range(H)]
        allHitY=[allHitTraj[t][th2][0] for t in range(H)]
        Z=list(range(H))
        #plt.plot(allHitX,allHitY,label="All Hit", color='g',markersize=2,linewidth=3)

        #allMissX=[allMissTraj[t][th1][0] for t in range(H)]
        #allMissY=[allMissTraj[t][th2][0] for t in range(H)]
        #plt.plot(allHitX,allHitY,label="All Miss", color='r',markersize=2,linewidth=3)

        fg=False
        for t in range(H):
            if fg==False:
                p = plt.Circle((allHitTraj[t][th1][0], allHitTraj[t][th2][0]), d_ub, facecolor='none', edgecolor='cyan',linewidth=0.4,alpha=0.5,label="Safety envelope")
                fg=True
            else:
                p = plt.Circle((allHitTraj[t][th1][0], allHitTraj[t][th2][0]), d_ub, facecolor='none', edgecolor='cyan',linewidth=0.4,alpha=0.5)
            ax.add_patch(p)
            art3d.pathpatch_2d_to_3d(p, z=t, zdir="z")




        #plt.plot(allMissX,allMissY,label="All Miss", color='r',markersize=2,linewidth=3)
        fg=False
        for traj in randTrajs:
            X=[traj[t][th1][0] for t in range(H)]
            Y=[traj[t][th2][0] for t in range(H)]
            #Z=list(range(H))
            if fg==False:
                ax.plot3D(X,Y,Z, color='k',markersize=1,linewidth=1,linestyle='--',label="Random trajectories")
                fg=True
            else:
                ax.plot3D(X,Y,Z, color='k',markersize=1,linewidth=1,linestyle='--')

        k=0
        fg=False
        for traj in randTrajsVio:
            X=[traj[t][th1][0] for t in range(H)]
            Y=[traj[t][th2][0] for t in range(H)]
            if fg==False:
                plt.plot(X,Y,Z, color='r',markersize=1,linewidth=1.5,linestyle='--',label="Violating trajectories")
                p = plt.Circle((allHitTraj[vioT[k]][th1][0], allHitTraj[vioT[k]][th2][0]), d_ub, facecolor='none', edgecolor='r',linewidth=1,label="Violating enevelope")
                fg=True
            else:
                plt.plot(X,Y,Z, color='r',markersize=1,linewidth=1.5,linestyle='--')
                p = plt.Circle((allHitTraj[vioT[k]][th1][0], allHitTraj[vioT[k]][th2][0]), d_ub, facecolor='none', edgecolor='r',linewidth=1)
            ax.scatter(X[vioT[k]],Y[vioT[k]],vioT[k],marker='X',color='r',s=50)
            ax.scatter(allHitTraj[vioT[k]][th1][0], allHitTraj[vioT[k]][th2][0],vioT[k],marker='o',color='red',s=40)
            ax.add_patch(p)
            art3d.pathpatch_2d_to_3d(p, z=vioT[k], zdir="z")
            k=k+1

        plt.plot(allHitX,allHitY,Z, color='g',markersize=2,linewidth=3,label="Nominal trajectory")

        #plt.legend()
        #plt.show()
        #plt.savefig(OUTPUT_PATH+'/'+fname+"_safety_envelope"+'.pdf', format='pdf')

        plt.legend(loc='upper right')
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

    def vizVaryC2(listC,listD,listVar,listItNum,fname="benchmark"):

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

    def vizVaryC(mean_var_df,fname="benchmark"):
        '''
        Plots training information
        '''

        #print(mean_var_df)
        # loading dataset
        #data = sns.load_dataset("iris")
        #print(data)

        plt.ylabel('Deviation',fontsize=14,fontweight='bold')
        plt.xlabel(r'$\mathbf{c}$',fontsize=16)
        #plt.scatter(hList,diffList,alpha=0.1,color='cyan')
        #sns.lineplot(x="sepal_length", y="sepal_width", data=data)
        sns.lineplot(x="c", y="dev", data=mean_var_df)
        #plt.show()
        #plt.close()
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
