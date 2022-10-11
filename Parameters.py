'''
Parameters required for the code
'''
import os,sys

'''
Please add the following line in ~/.bashrc
export STAT_SCHDLR_ROOT_DIR = <YOUR PROJECT ROOT>
'''

PROJECT_ROOT = os.environ['STAT_SCHDLR_V2_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

LIB_PATH=PROJECT_ROOT+'/'+'lib/'
SRC_PATH=PROJECT_ROOT+'/'+'src/'
OUTPUT_PATH=PROJECT_ROOT+'/'+'output/'
PICKLE_PATH=PROJECT_ROOT+'/'+'pickles/'
DATA_PATH=PROJECT_ROOT+'/'+'data/'


PICKLE_FLAG=False
RAND_SAMP_MET="RGA"

R=500
#EPSILON=0.0001
EPSILON=0.001
EPOCH=20
