'''
Parameters required for the code
'''
import os,sys

'''
Please add the following line in ~/.bashrc
export SCHDLR_ROOT_DIR = <YOUR PROJECT ROOT>
'''

PROJECT_ROOT = os.environ['SCHDLR_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

LIB_PATH=PROJECT_ROOT+'/'+'lib/'
SRC_PATH=PROJECT_ROOT+'/'+'src/'
OUTPUT_PATH=PROJECT_ROOT+'/'+'output/'
PICKLE_PATH=PROJECT_ROOT+'/'+'pickles/'
DATA_PATH=PROJECT_ROOT+'/'+'data/'


BOUNDED_TREE_STEP=5

PICKLE_FLAG=True

VIZ_PER_COVERAGE=100 # Percentage of reachable sets covered
