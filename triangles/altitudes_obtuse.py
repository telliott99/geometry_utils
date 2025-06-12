import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(-60,100))

pL = geo.get_standard_triangle(mode='obtuse')

# to be consistent with other plots
A,B,C = pL

geo.outline_polygon(ax,[A,B,C])


oD = geo.get_orthocenter_and_altitudes([A,B,C])
D = oD['D']
E = oD['E']
F = oD['F']

H = geo.get_intersection_for_two_lines([A,D],[B,E])
geo.draw_line_segments(
    ax,[[A,D],[A,E],[A,F],[A,H],[B,H],[C,H]],ls=':')



points = [
          ['A',geo.nudge(A,'N',2),'W',8],
          ['B',B,'W',6],
          ['C',C,'N',2],
          ['D',D,'E',2],
          ['E',E,'W',6],
          ['F',F,'S',6],
          ['H',H,'W',7],
         ]

geo.label_points(points)


geo.scatter_points(ax,[A,B,C,D,E,F,H],s=6)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/altitudes_obtuse.png'
plt.savefig(ofn, dpi=300)