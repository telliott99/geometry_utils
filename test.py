import sys,os,subprocess
import numpy as np
import matplotlib.pyplot as plt

# python finds this in 
# /usr/local/lib/python3.10/site-packages
# which is really a sym link to geometry_utils/geometry.py
import geometry as geo


# script must run from project directory
# in order for path to be correct
path = geo.get_path()

if len(sys.argv) < 2:
    print('Usage: provide a target directory or ``all``')
    sys.exit()

t = sys.argv[1]

#-------------------

def run_test(path):
    try:
        result = subprocess.run(
            ['python3', 'test_dir.py', path])
        print(result.returncode, result.args[1].split('/')[-1])
    except OSError as e:
        print('error',fn,e)
 
#-------------------

L = os.listdir(path + '/projects')
L = [f for f in L if os.path.isdir(path + '/projects/' + f)]

if t == 'tests':
    run_test(path + '/tests/')
    
elif t != 'all':
   run_test(path + '/projects/' + t)

else:
    for t in L:
        run_test(path + '/projects/' + t)
    run_test(path + '/tests/')
