import random
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-40,100), ylim=(-10,120))

n = 30
X = [random.randint(0,100) for i in range(n)]
Y = [random.randint(0,100) for i in range(n)]

pL = [geo.Point(x,y) for x,y in zip(X,Y)]
M = geo.Point(20,0)
N = geo.Point(50,80)

# testing mirror points
# it's quite slow, but I suspect the drawing code

qL = geo.mirror_points(pL,[M,N])

cL = ['r','g','b','purple','cyan',
      'magenta','steelblue','0.6']*n

geo.scatter_points(ax,pL)

for i,p in enumerate(pL):
    c = cL[i]
    geo.scatter_points(ax,[p,qL[i]],c=c)
    
geo.draw_line_segments(ax,[[M,N]],ec='purple',ls=':')

#-------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ex23.png'
plt.savefig(ofn, dpi=300)