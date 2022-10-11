import os,sys
PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

from Parameters import *
import math
import time
import copy
import numpy as np

class System:

    def __init__(self,A,B,C,D,K):
        self.A=A # Dynamics
        self.B=B # Dynamics
        self.C=C # Dynamics
        self.D=D # Dynamics
        self.K=K # Control
