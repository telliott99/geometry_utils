import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-150,200), ylim=(-150,200))

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

pL = geo.get_standard_triangle()
A,B,C = pL
geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

iD = geo.get_incenter_and_bisectors([A,B,C])
I = iD['I']

a = geo.get_length([B,C])
b = geo.get_length([A,C])
c = geo.get_length([A,B])
s = (a+b+c)/2

circle1 = plt.Circle((I.x,I.y),s, 
    facecolor='none',
    edgecolor='k')
ax.add_patch(circle1)

r = geo.get_length([I,iD['X']])
circle2 = plt.Circle((I.x,I.y),r, 
    facecolor='none',
    edgecolor='k')
ax.add_patch(circle2)

rL = geo.get_intersection_line_segment_circle(
    [A,B],[I,s])
geo.draw_line_segment(ax,rL,ec='r')

rL = geo.get_intersection_line_segment_circle(
    [B,C],[I,s])
geo.draw_line_segment(ax,rL,ec='r')

rL = geo.get_intersection_line_segment_circle(
    [A,C],[I,s])
geo.draw_line_segment(ax,rL,ec='r')

Y = iD['Y']
geo.draw_line_segment(ax,[I,rL[1]],ec='r',ls=':')
geo.draw_line_segment(ax,[I,Y],ec='r',ls=':')

box = geo.mark_right_angle(Y,[C,I],n=8)
geo.outline_polygon(ax,box,ec='k')

geo.scatter_points(ax,[A,B,C,I,rL[1]],s=10)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/problem.png'
plt.savefig(ofn, dpi=300)