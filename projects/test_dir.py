import sys,os,subprocess
import geometry as geo

# we receive the path to the target directory from sys.argv
path = sys.argv[1]

name = path.split('/')[-1]
print('testing %s' % name)

L = os.listdir(path)
L = [f for f in L if f.endswith('.py')]

# lexicographical sort:
# 1 10 11 .. 2 21 .. 3 4

L.sort()

for fn in L:
    try:
        result = subprocess.run(
            ['python3.10',path + '/' + fn])
        print(result.returncode, result.args[1].split('/')[-1])
    except OSError as e:
        print('error',fn,e)