import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,120), ylim=(-10,100))

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

A = geo.Point(30,40)
B = geo.Point(70,40)
r = geo.get_length([A,B])

c1 = plt.Circle(
    (A.x,A.y),r,fc='none',ec='gray')
ax.add_patch(c1)

c2 = plt.Circle(
    (B.x,B.y),r,fc='none',ec='gray')
ax.add_patch(c2)

# returns wrong order right now
D,C = geo.get_intersection_circle_circle(
    [A,r],[B,r])
    
geo.draw_line_segments(
    ax,[[A,B],[C,D]])

geo.fill_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,D],fc='b',alpha=0.2)

geo.outline_polygon(ax,[A,B,C],ec='r')
geo.outline_polygon(ax,[A,B,D],ec='b')

X = geo.get_intersection_for_two_lines(
    [A,B],[C,D])
    
box = geo.mark_right_angle(X,[C,B],n=3)
geo.outline_polygon(ax,box,ec='b')

geo.scatter_points(ax,[A,B,C,D],s=8)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/problem.png'
plt.savefig(ofn, dpi=300)