import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(-10,100))

Q = geo.Point(50,50)
r = 30
circle1 = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle1)

A = geo.Point(20,Q.y)
B = geo.Point(80,Q.y)  
geo.draw_line_segment(ax,[A,B])

m = -1.5
k = geo.get_intercept_for_point_slope(Q,m)
C = geo.get_intersection_slope_intercept_circle(
    m,k,[Q,r])[1]
geo.draw_line_segments(ax,[[A,C],[B,C]],ec='r',ls=':')

D = geo.get_perp_on_line_for_point(
    [A,B],C)
geo.draw_line_segment(ax,[C,D],ec='r')

E = geo.Point(Q.x,Q.y+r)
geo.draw_line_segment(ax,[Q,E],ec='r')

M = geo.get_point_by_fractional_length([C,D],0.5)
N = geo.get_point_by_fractional_length([Q,E],0.2)

geo.scatter_points(ax,[A,B,C,D,E,Q])

points = [
          ['Q',Q,'SW',6],
          #['P',A,'W',4],
          #['R',B,'E',2],
          ['h',M,'E',1],
          ['r',N,'E',1]
         ]

geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/geometric_mean.png'
plt.savefig(ofn, dpi=300)