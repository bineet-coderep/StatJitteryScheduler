import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import math

class JFB:

    def __init__(self,B=1000,c=0.99):
        self.B=B
        self.c=c
        self.K=self.getNumberOfSamples()
        self.err=self.getErr()

    def getNumberOfSamples(self):
        K=math.ceil((-math.log10(self.B+1)/math.log10(self.c)))
        return K

    def getErr(self):
        err=(self.c/(self.c+((1-self.c)*self.B)))
        return err

    def printReport(self):
        print(">> STATUS: Jeffries Bayes Factor Details . . .")
        print("\t* Number of Samples (K): ",self.K)
        print("\t* Type I Error: ",self.err)
        print("\t* c: ",self.c)
        print("\t* B: ",self.B)
        print(">> End of report")


if False:
    JFB().printReport()
