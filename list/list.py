p = '/Users/telliott/Library/CloudStorage/Dropbox/'
p += 'Github-Math/geometry_utils/'
fn = 'geometry.py'

with open(p+fn) as fh:
    data = fh.read()
    
i = -1
L = list()
limit = 100
rL = list()

while True:
    i = data.find('def ',i+1)
    j = data.find(':',i+1)
    rL.append(data[i:j])
    #print('i',i)
    if i == -1:
        break
    i = j

for e in rL:
    print(e)