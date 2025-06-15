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

# returns a box
geo.mark_right_angle(D,[B,F],n=3)

geo.get_point_by_fractional_length([A,B],f)
geo.get_intersection_for_two_lines([A,B],[C,D])
geo.get_points_perp_on_line_for_point(A,pL)
geo.get_points_perp_at_point_by_fractional_length(pL,f=0.5)

get_intersection_line_segment_circle(pL,cL)
get_intersection_circle_circle(cL1,cL2)
get_tangent_points_on_circle_for_point(cL1,P)
mark_right_angle(A,pL,n=3)

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)
'''

pL = geo.get_standard_triangle()
A,B,C = pL



'''

points = [
          ['A',A,'N',0],
          ['B',B,'N',0],
          ['C',C,'N',0],
         ]

geo.label_points(points)
'''

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/problem.png'
plt.savefig(ofn, dpi=300)