import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(-50,100))

pL = geo.get_standard_triangle()
A,B,C = pL
geo.draw_line_segment(ax,[A,B])


theta=60

tmp = geo.get_point_at_angle_on_circle(
    theta,[A,10])

rL = geo.get_perp_at_point_by_fractional_length(
    [A,B],0.5)
    
X = geo.xll([A,tmp],rL)
M = geo.get_midpoint([A,B])

geo.fill_polygon(ax,[A,B,X])
geo.outline_polygon(ax,[A,B,X])

geo.dls(ax,[X,M])

#----------

theta = 45
r = 20

U = geo.get_point_at_angle_on_circle(
    theta,[A,r])
    
Y = geo.get_point_at_angle_on_circle(
    theta+90,[B,r])

K = geo.get_intersection_for_two_lines(
    [A,U],[B,Y])

geo.draw_line_segments(
    ax,[[A,K],[B,K]],ls=':')

geo.scatter_points(ax,[K,U,Y])


#----------

geo.savefig(plt)