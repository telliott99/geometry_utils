import sys,os,subprocess
import numpy as np
import matplotlib.pyplot as plt

# python finds this in 
# /usr/local/lib/python3.10/site-packages
# which is really a sym link to geometry_utils/geometry.py
import geometry as geo

# we get the path to the project from geo
path = '/'.join(geo.get_path().split('/')[:-1])

# hard coded locations
# most are  /projects/proj_dir/script.py
# tests are /tests/test1.py
# run p3 tests/run.py from geo_utils directory

L = os.listdir(path + '/projects')
pathD = {}
for dir in L:
    if dir == '.DS_Store':
        continue
    pathD[dir] = path + '/projects/' + dir

#-------------------

if len(sys.argv) < 2:
    print('Usage: provide a target directory or ``all``')
    sys.exit()

t = sys.argv[1]

if not (t in pathD.keys() or t == 'all'):
    print('unrecognized option',t)
    sys.exit()

#-------------------

def run_test(path):
    try:
        result = subprocess.run(
            ['python3', path])
        print(result.returncode, result.args[1].split('/')[-1])
    except OSError as e:
        print('error',fn,e)
 
#-------------------

def do_one_directory(t):
    print('testing',t,':')
    dir_path = pathD[t]
    L = os.listdir(dir_path)
    L.sort()
    L = [fn for fn in L if fn.endswith('.py')]
    for fn in L:
        if fn == 'run.py':
            continue
        run_test(dir_path + '/' + fn)

if t in pathD.keys():
    do_one_directory(t)

else:
    assert t == 'all'
    for k in pathD.keys():
        do_one_directory(k)
    # not tests
    #do_one_directory(path + '/tests/')
    
