import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,110), ylim=(-30,100))

pL = geo.get_standard_triangle()
A,B,C = pL
C = geo.nudge(C,'E',46)

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

Q,r = geo.get_circumcircle([A,B,C])

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

M = geo.bisect_angle_Euclid(A,[B,C])
D = geo.get_intersection_line_segment_circle(
    [A,M],[Q,r])[1]

geo.draw_line_segments(ax,[[A,D],[B,D],[C,D]])

aL = [[C,A,D],[D,A,B]]
geo.mark_angles(ax,aL,d=14,c='m')



points = [
          ['A',A,'W',6],
          ['B',B,'E',3],
          ['C',C,'N',1],
          ['D',D,'E',2],
         ]

geo.label_points(points)

geo.scatter_points(ax,[A,B,C,D],s=6)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/cq_SSA.png'
plt.savefig(ofn, dpi=300)