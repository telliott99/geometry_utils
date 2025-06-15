import sys,os,subprocess

path = '/Users/telliott/Library/CloudStorage/Dropbox/'
path += 'Github-Math/geometry_utils/'
    
L = os.listdir(path)
L = [f for f in L if os.path.isdir(f)]

L.sort()

for dir in L:
    try:
        result = subprocess.run(
            ['python3', 'all.py', dir])
        print(result.returncode, result.args[1].split('/')[-1])
    except OSError as e:
        print('error',fn,e)