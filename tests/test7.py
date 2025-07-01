import matplotlib.pyplot as plt
import math, random
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,110), ylim=(-20,110))

N = 50
X = [random.randint(0,100) for i in range(N)]
Y = [random.randint(0,100) for i in range(N)]
pL1 = [geo.Point(x,y) for x,y in zip(X,Y)]

Q = geo.Point(40,40)
pL2 = geo.rotate_points_around_center_by_angle(
    pL1,Q,4)
   
pL3 = geo.rotate_points_around_center_by_angle(
    pL2,Q,4)

pL4 = geo.rotate_points_around_center_by_angle(
    pL3,Q,4)
    
geo.scatter_points(ax,pL1,c='r')
geo.scatter_points(ax,pL2,c='b')
geo.scatter_points(ax,pL3,c='magenta')
geo.scatter_points(ax,pL4,c='g')

geo.scatter_points(ax,[Q],c='k',s=20)

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ex7.png'
plt.savefig(ofn, dpi=300)
