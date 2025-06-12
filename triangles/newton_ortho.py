import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(-10,100))


pL = geo.get_standard_triangle()
A,B,C = pL

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

oD = geo.get_orthocenter_and_altitudes([A,B,C])
D = oD['D']
F = oD['F']

geo.draw_line_segments(ax,[[A,D],[C,F]])

aL = [[B,C,F],[D,A,B]]
geo.mark_angles(ax,aL,d=5,c='m',s=20)

box = geo.mark_right_angle(D,[A,C])
geo.outline_polygon(ax,box,ec='k')
box = geo.mark_right_angle(F,[B,C ])
geo.outline_polygon(ax,box,ec='k')


points = [
          ['A',A,'SW',5],
          ['B',B,'SE',2],
          ['C',C,'N',1],
          ['D',D,'E',1],
          ['F',F,'S',4],
         ]

geo.label_points(points)

geo.scatter_points(ax,[A,B,C],s=6)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/newton_ortho.png'
plt.savefig(ofn, dpi=300)