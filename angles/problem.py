import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-30,100), ylim=(-10,100))

pL = geo.get_standard_triangle(mode='isosceles')
A,B,C = pL
C = geo.nudge(C,'S',30)

f = 0.25
D = geo.get_point_by_fractional_length([A,B],f)

rL = geo.get_perp_at_point_by_fractional_length([A,B],f)
F = geo.get_intersection_for_two_lines([B,C],rL)
E = geo.get_intersection_for_two_lines([A,C],[D,F])

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C],fc='r',alpha=0.12)

geo.draw_line_segments(ax,[[D,F],[C,F]])

rL = geo.mark_right_angle(D,[B,F],n=3)
geo.outline_polygon(ax,rL,ec='k')

geo.scatter_points(ax,[A,B,C,E,F],s=8)

points = [
          ['B',A,'SW',6],
          ['C',B,'SE',2],
          ['A',C,'NE',2],
          ['D',D,'S',5],
          ['E',E,'W',4],
          ['F',F,'W',4],
         ]

geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/problem.png'
plt.savefig(ofn, dpi=300)