import sys,os,subprocess


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

path += '/projects/'

#-------------------

def run_test(directory):
    try:
        result = subprocess.run(
            ['python3.10', 'projects/test_dir.py', directory])
        print(result.returncode, result.args[1].split('/')[-1])
    except OSError as e:
        print('error',fn,e)
 
#-------------------

L = os.listdir(path)
L = [f for f in L if os.path.isdir(path + '/' + f)]
L.sort()

for directory in L:
    if t == 'all' or directory.startswith(t):
        run_test('projects/' + directory)

    

