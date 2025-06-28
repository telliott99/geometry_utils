import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,140), ylim=(-20,100))


pL = geo.get_standard_triangle()
A,B,C = pL
A,B,C = geo.scale_triangle([A,B,C],0.7)
C = geo.nudge(C,'S',15)


Q,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
#ax.add_patch(circle)

# go to circumcircle for ABC through A at slope m
D = geo.get_point_for_cyclic_quadrilateral(A,[B,C],m=0.45)

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])


a = geo.get_length([A,B])
b = geo.get_length([B,D])
c = geo.get_length([D,C])
d = geo.get_length([A,C])

x = geo.get_length([A,D])
y = geo.get_length([B,C])

# draw the two triangles next to each other

f = (a+b)/a
K = geo.get_point_by_fractional_length([A,B],f)
L,M = geo.get_intersection_circle_circle(
    [B,y],[K,c])

def panel_c():
    geo.outline_polygon(ax,[B,K,M],ec='b')
    geo.fill_polygon(ax,[B,K,M],fc='b',alpha=0.15)
    geo.scatter_points(ax,[A,B,C,K,M],s=8)

#panel_c()
#geo.scatter_points(ax,[A,B,C,K,M],s=8)

f = geo.get_length([A,C])/geo.get_length([K,M])

S = geo.get_point_by_fractional_length([B,K],f)
T = geo.get_point_by_fractional_length([B,M],f)

def panel_d():
    geo.outline_polygon(ax,[B,S,T],ec='b')
    geo.fill_polygon(ax,[B,S,T],fc='b',alpha=0.15)

#geo.scatter_points(ax,[A,B,C,S,T],s=8)
geo.draw_line_segments(ax,[[C,geo.Point(T.x,C.y)]],ls=':')
panel_d()
geo.scatter_points(ax,[A,B,C,S,T],s=8)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ptolemy.png'
plt.savefig(ofn, dpi=300)