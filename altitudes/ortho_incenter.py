import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,120), ylim=(-40,120))

A,B,C = geo.get_standard_triangle()

geo.outline_polygon(ax,[A,B,C],ec='b')
geo.fill_polygon(ax,[A,B,C],fc='b',alpha=0.07)

oD = geo.get_orthocenter_and_altitudes([A,B,C])
D = oD['D'];  E = oD['E'];  F = oD['F']
H = oD['H']

geo.outline_polygon(ax,[D,E,F])
geo.fill_polygon(ax,[D,E,F])

geo.outline_polygon(ax,[D,E,F])
geo.fill_polygon(ax,[D,E,F])


geo.draw_line_segments(
    ax,[[A,D],[B,E],[C,F]],lw=0.5)

geo.scatter_points(ax, [A,B,C,D,E,F])
geo.scatter_points(ax, [H])


diameter = [B,H]
Q = geo.get_point_by_fractional_length(diameter,0.5)
r = geo.get_length([B,Q])

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k',lw=2,ls=':')
ax.add_patch(circle)


aL = [[A,B,E],[F,D,A],[F,C,E],[A,D,E]]
geo.mark_angles(ax,aL,d=20,c='k')


diameter = [C,H]
O = geo.get_point_by_fractional_length(diameter,0.5)
r2 = geo.get_length([C,O])

circle = plt.Circle(
    (O.x,O.y),r2,fc='none',ec='k',lw=2,ls=':')
ax.add_patch(circle)


points = [
          ['A',A,'W',5],
          ['B',B,'E',2],
          ['C',C,'N',2],
          ['D',D,'N',2],
          ['E',E,'W',6],
          ['F',F,'SW',8],
         ]

geo.label_points(points,s=16)

geo.scatter_points(ax,[A,B,C,D,E,F])
geo.scatter_points(ax,[H],c='r',s=20)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ortho_incenter.png'
plt.savefig(ofn, dpi=300)