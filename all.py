import sys,os,subprocess
import path

if len(sys.argv) > 1:
    directory = sys.argv[1] + '/'
else:
    directory = 'tests/'

print('testing %s' % directory)
p = path.p + directory
    
L = os.listdir(p)
L = [f for f in L if f.endswith('.py')]

try:
    L.remove('path.py')
except:
    pass

# lexicographical sort:
# 1 10 11 .. 2 21 .. 3 4

L.sort()

for fn in L:
    try:
        result = subprocess.run(
            ['python3',p+fn])
        print(result.returncode, result.args[1].split('/')[-1])
    except Error as e:
        print('error',fn,e)