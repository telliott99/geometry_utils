import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,120), ylim=(-40,100))

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
'''

pL = geo.get_standard_triangle(mode='equilateral')
A,B,C = pL

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

Q,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle((Q.x,Q.y), r, 
    fc='none',
    ec='lightgray')
ax.add_patch(circle)

D = geo.get_point_by_fractional_length([C,Q],2)
M = geo.get_intersection_for_two_lines([A,B],[C,D])


geo.draw_line_segments(ax,[[A,Q],[B,Q]],ec='0.2')
geo.draw_line_segments(ax,[[C,D]],ec='k')
geo.draw_line_segments(ax,[[A,D],[B,D]],ec='m')

geo.scatter_points(ax,[A,B,C,Q,D,M])


points = [
          ['A',A,'SW',8],
          ['B',B,'SE',5],
          ['C',C,'NE',2],
          ['D',D,'S',7],
          ['M',geo.nudge(M,'N',1),'W',8],
          ['Q',Q,'E',2],
         ]

geo.label_points(points)


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/equilateral.png'
plt.savefig(ofn, dpi=300)