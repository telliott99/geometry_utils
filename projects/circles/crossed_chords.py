import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,100), ylim=(-20,100))

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
B = geo.Point(60,50)
C = geo.Point(25,70)

Q,r = geo.get_circumcircle([A,B,C])

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

#need a point on the circle for second chord
D = geo.get_intersection_line_segment_circle(
    [C,geo.Point(C.x+10,C.y-40)],[Q,r])[1]

X = geo.get_intersection_for_two_lines([A,B],[C,D])

geo.outline_polygon(ax,[A,C,X])
geo.fill_polygon(ax,[A,C,X])

geo.outline_polygon(ax,[B,D,X],ec='b')
geo.fill_polygon(ax,[B,D,X],fc='b',alpha=0.2)



points = [
          ['A',A,'SW',6],
          ['B',B,'SE',2],
          ['C',C,'NE',2],
          ['D',D,'S',5],
          ['X',X,'N',4],
          ]

geo.label_points(points)
geo.scatter_points(ax,[A,B,C,D,X],s=10)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/crossed_chords.png'
plt.savefig(ofn, dpi=300)