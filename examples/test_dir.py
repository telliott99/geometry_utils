import sys,os,subprocess

path = '/Users/telliott/Library/CloudStorage/Dropbox/'
path += 'Github-Math/geometry_utils/examples/'

if len(sys.argv) > 1:
    directory = sys.argv[1] + '/'
else:
    directory = 'tests/'

print('testing %s' % directory)
path += directory
    
L = os.listdir(path)
L = [f for f in L if f.endswith('.py')]

# lexicographical sort:
# 1 10 11 .. 2 21 .. 3 4

L.sort()

for fn in L:
    if fn == 'geometry.py':
        continue
    try:
        result = subprocess.run(
            ['python3',path+fn])
        print(result.returncode, result.args[1].split('/')[-1])
    except OSError as e:
        print('error',fn,e)