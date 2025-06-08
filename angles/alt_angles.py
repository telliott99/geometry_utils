import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-30,100), ylim=(-10,100))

pL = geo.get_standard_triangle(mode='isosceles')
A,B,C = pL
C = geo.nudge(C,'S',15)

rD = geo.get_orthocenter_and_altitudes([A,B,C])
F = rD['F']


geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C],fc='r',alpha=0.12)

geo.draw_line_segment(ax,[C,F])

box = geo.mark_right_angle(F,[B,C],n=3)
geo.outline_polygon(ax,box,ec='k')

M = geo.get_point_by_fractional_length([F,C],1.2)
N = geo.get_point_by_fractional_length([B,C],1.2)

rL = geo.get_perp_at_point_by_fractional_length(
    [F,C],1.0)

geo.draw_line_segments(ax,[[C,M],[C,N]])
geo.draw_line_segment(ax,rL,ls=':',ec='gray')

geo.mark_angles(ax,
    [[A,B,C],[rL[0],C,N],[B,C,rL[1]]],c='r')

geo.mark_angles(ax,
    [[C,A,B],[rL[0],C,A]],c='b')

points = [
          ['A',A,'SW',5],
          ['B',B,'SE',2],
          ['C',C,'NE',3],
          ['F',F,'S',5],
          ['M',rL[0],'N',1],
          ['N',rL[1],'N',1],
         ]

geo.label_points(points)

geo.scatter_points(ax,rL,s=8)


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/alt_angles.png'
plt.savefig(ofn, dpi=300)