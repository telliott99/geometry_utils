import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

ofn = '/Users/telliott/Desktop/example11.png'

fig, ax = geo.init()
ax.set(xlim=(-20,100), ylim=(0,100))

Q = geo.Point(50,50)
r = 30
cL = [Q,r]
P = geo.Point(20,30)
d = 20

pL = geo.get_chord_for_point_on_circle_with_length(
    ax,cL,P,d)

circle = plt.Circle((Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

[A,B] = pL
geo.scatter_points(ax,[P,Q],c='k')
geo.scatter_points(ax,[A,B],c='r')

plt.savefig(ofn, dpi=300)

