import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-50,150), ylim=(-100,100))

pL = geo.get_standard_triangle(mode='equilateral')
A,B,C = pL
geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

Q,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

hoz = geo.Point(Q.x,Q.y-15)
rL = geo.get_chord_for_point_on_circle_with_length(
        [Q,r],B,40)
M = rL[1]

f = geo.get_length([A,M])/geo.get_length([M,B])
D = geo.get_point_by_fractional_length([M,B],f)

geo.draw_line_segment(ax,[C,M],ec='k')
geo.draw_line_segments(ax,[[A,M],[A,D],[M,D]],ec='b')
geo.fill_polygon(ax,[A,M,D],fc='b',alpha=0.05)

geo.scatter_points(ax,[A,B,C,D,M],s=6)


aL = [[A,C,B],[A,B,C],[B,M,A],[C,M,A],[A,D,B]]
geo.mark_angles(ax,aL,d=7,c='r',s=14)

geo.mark_angles(ax,[[C,A,M],[C,B,M],[B,A,D]],d=10,c='b',s=14)
#geo.mark_angles(ax,[[M,C,B],[M,A,B]],d=20,c='r',s=14)

points = [
          ['A',A,'SW',8],
          ['B',B,'SE',4],
          ['C',C,'N',4],
          ['D',D,'E',4],
          ['M',M,'E',4],
         ]

geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/Van_Schooten.png'
plt.savefig(ofn, dpi=300)