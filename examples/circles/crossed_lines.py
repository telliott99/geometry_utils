import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

'''
std functions
geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])
geo.draw_line_segments(ax,[[D,F],[C,F]])
rL = geo.mark_right_angle(D,[B,F],n=3)

geo.get_point_by_fractional_length([A,B],f)
geo.get_intersection_for_two_lines([A,B],[C,D])
geo.get_point_perp_on_line_for_point(A,pL)
geo.get_perp_at_point_by_fractional_length(pL,f=0.5)

get_intersection_line_segment_circle(pL,cL)
get_intersection_circle_circle(cL1,cL2)
get_tangent_points_on_circle_for_point(cL1,P)
mark_right_angle(A,pL,n=3)

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)
'''

A = geo.Point(10,10)
B = geo.Point(10,60)
C = geo.Point(50,20)
D = geo.Point(50,70)

geo.draw_line_segments(ax,[[A,B],[C,D]])
geo.draw_line_segments(ax,[[A,D],[B,C]],ec='r')
X = geo.get_intersection_for_two_lines([A,D],[B,C])

points = [
          ['A',A,'SW',4],
          ['B',D,'NE',1],
          ['C',B,'N',1],
          ['D',C,'NE',1],
          ['X',X,'S',6],
          ]

geo.label_points(points)

geo.mark_angles(ax,[[A,B,X],[B,C,D]],d=5,c='r',s=20)
geo.mark_angles(ax,[[B,A,X],[C,D,X]],d=7,c='b',s=20)

geo.scatter_points(ax,[A,B,C,D,X],s=5)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/crossed_lines.png'
plt.savefig(ofn, dpi=300)