import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
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


        ax.set_xlabel(r'$\mathbf{x_0}$',fontsize=12)
        ax.set_ylabel(r'$\mathbf{x_1}$',fontsize=12)
        ax.set_zlabel('time',fontsize=11,fontweight='bold')

        #ax.set_xlim(-25, 25)
        #ax.set_ylim(-30, 30)
        #ax.set_zlim(0, 160)

        nVert=len(allHitTraj)
        H=len(allHitTraj[0])

        Zlist=list(range(H))

        for randTraj in randTrajs:
            for t in range(H):
                #fillX=[]
                #fillY=[]
                polyArray=np.zeros((nVert,2))
                for v in range(nVert):
                    polyArray[v][0]=randTraj[v][t][th1]
                    polyArray[v][1]=randTraj[v][t][th2]
                #polyArray[nVert][0]=allHitTraj[0][t][th1]
                #polyArray[nVert][1]=allHitTraj[0][t][th2]
                #polyArray=np.random.rand(nVert ,2)
                #print(polyArray)
                pPoly=plt.Polygon(polyArray,fc='g', closed=True,fill=True,alpha=0.3)
                ax.add_patch(pPoly)
                art3d.pathpatch_2d_to_3d(pPoly, z=t, zdir="z")


            for v in range(nVert):
                Xlist=[]
                Ylist=[]
                for t in range(H):
                    Xlist.append(randTraj[v][t][th1])
                    Ylist.append(randTraj[v][t][th2])
                ax.plot3D(Xlist,Ylist,Zlist, color='g',markersize=1,linewidth=0.1,linestyle='--',alpha=0.3)

        for t in range(H):
            #fillX=[]
            #fillY=[]
            polyArray=np.zeros((nVert,2))
            for v in range(nVert):
                polyArray[v][0]=allHitTraj[v][t][th1]
                polyArray[v][1]=allHitTraj[v][t][th2]
            #poly2Array[nVert][0]=allHitTraj[0][t][th1]
            #polyArray[nVert][1]=allHitTraj[0][t][th2]
            #polyArray=np.random.rand(nVert ,2)
            #print(polyArray)
            pPoly=plt.Polygon(polyArray,fc='k',closed=True,fill=True,alpha=0.6)
            ax.add_patch(pPoly)
            art3d.pathpatch_2d_to_3d(pPoly, z=t, zdir="z")

        for v in range(nVert):
            Xlist=[]
            Ylist=[]
            for t in range(H):
                Xlist.append(allHitTraj[v][t][th1])
                Ylist.append(allHitTraj[v][t][th2])
            ax.plot3D(Xlist,Ylist,Zlist, color='k',markersize=1,linewidth=0.1,linestyle='-',alpha=0.6)



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

        nVert=len(allHitTraj)
        H=len(allHitTraj[0])

        Zlist=list(range(H))

        for randTraj in randTrajs:
            for t in range(H):
                #fillX=[]
                #fillY=[]
                polyArray=np.zeros((nVert,2))
                for v in range(nVert):
                    polyArray[v][0]=randTraj[v][t][th1]
                    polyArray[v][1]=randTraj[v][t][th2]
                #polyArray[nVert][0]=allHitTraj[0][t][th1]
                #polyArray[nVert][1]=allHitTraj[0][t][th2]
                #polyArray=np.random.rand(nVert ,2)
                #print(polyArray)
                pPoly=plt.Polygon(polyArray,fc='g', closed=True,fill=True,alpha=0.3)
                ax.add_patch(pPoly)
                art3d.pathpatch_2d_to_3d(pPoly, z=t, zdir="z")


            for v in range(nVert):
                Xlist=[]
                Ylist=[]
                for t in range(H):
                    Xlist.append(randTraj[v][t][th1])
                    Ylist.append(randTraj[v][t][th2])
                ax.plot3D(Xlist,Ylist,Zlist, color='g',markersize=1,linewidth=0.1,linestyle='--',alpha=0.3)

        for t in range(H):
            #fillX=[]
            #fillY=[]
            polyArray=np.zeros((nVert,2))
            for v in range(nVert):
                polyArray[v][0]=allHitTraj[v][t][th1]
                polyArray[v][1]=allHitTraj[v][t][th2]
            #poly2Array[nVert][0]=allHitTraj[0][t][th1]
            #polyArray[nVert][1]=allHitTraj[0][t][th2]
            #polyArray=np.random.rand(nVert ,2)
            #print(polyArray)
            pPoly=plt.Polygon(polyArray,fc='k',closed=True,fill=True,alpha=0.6)
            ax.add_patch(pPoly)
            art3d.pathpatch_2d_to_3d(pPoly, z=t, zdir="z")

        for v in range(nVert):
            Xlist=[]
            Ylist=[]
            for t in range(H):
                Xlist.append(allHitTraj[v][t][th1])
                Ylist.append(allHitTraj[v][t][th2])
            ax.plot3D(Xlist,Ylist,Zlist, color='k',markersize=1,linewidth=0.1,linestyle='-',alpha=0.6)
        #plt.legend()
        #plt.show()
        #plt.savefig(OUTPUT_PATH+'/'+fname+"_safety_envelope"+'.pdf', format='pdf')
        for randTraj in randTrajsVio:
            for t in range(H):
                #fillX=[]
                #fillY=[]
                polyArray=np.zeros((nVert,2))
                for v in range(nVert):
                    polyArray[v][0]=randTraj[v][t][th1]
                    polyArray[v][1]=randTraj[v][t][th2]
                #polyArray[nVert][0]=allHitTraj[0][t][th1]
                #polyArray[nVert][1]=allHitTraj[0][t][th2]
                #polyArray=np.random.rand(nVert ,2)
                #print(polyArray)
                pPoly=plt.Polygon(polyArray,fc='r', closed=True,fill=True,alpha=0.6)
                ax.add_patch(pPoly)
                art3d.pathpatch_2d_to_3d(pPoly, z=t, zdir="z")


            for v in range(nVert):
                Xlist=[]
                Ylist=[]
                for t in range(H):
                    Xlist.append(randTraj[v][t][th1])
                    Ylist.append(randTraj[v][t][th2])
                ax.plot3D(Xlist,Ylist,Zlist, color='r',markersize=1,linewidth=0.5,linestyle='--',alpha=0.6)
        #plt.legend(loc='upper right')
        #plt.show()
        plt.savefig(OUTPUT_PATH+'/'+fname+"_safety_envelope_vio"+'.pdf', format='pdf')

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
