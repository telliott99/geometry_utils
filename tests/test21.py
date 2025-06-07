import math
import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-100,100), ylim=(-100,100))

pL = geo.get_standard_triangle(mode='right')
A,B,C = pL
theta = geo.get_angle(A,[B,C])
# print(theta)

pL = geo.translate_points([A,B,C],dx=20,dy=0)
pL = geo.rotate_points_around_center_by_angle(
    pL,geo.Point(0,0),35)
    
A,B,C = pL

geo.outline_polygon(ax,[A,B,C],ec='r')
geo.scatter_points(ax,[A,B,C],s=4)
pL = geo.mark_right_angle(A,[B,C])
#print(pL)

geo.outline_polygon(ax,pL,ec='k')


# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/example21.png'
plt.savefig(ofn, dpi=300)
