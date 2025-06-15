import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(-50,100))

pL = geo.get_standard_triangle()
A,B,C = pL

theta=60

D,E = geo.get_points_at_angle_to_line(
    theta,[A,B])

geo.draw_line_segment(ax,[A,B])
geo.scatter_points(ax,[A,B,D])

'''
> p3 test25.py
59.99988223535874
60.000042971840834
> 
'''

X = geo.get_point_by_fractional_length(
    [A,B],0.5)

geo.fill_polygon(ax,[A,X,D])
geo.outline_polygon(ax,[A,X,D])

#----------

theta = 45
r = 55
U,V = geo.get_point_with_base_angle_length(
    [A,B],theta,r)
    
Y,Z =  geo.get_point_with_base_angle_length(
    [B,A],theta,r)

K = geo.get_intersection_for_two_lines(
    [A,U],[B,Y])

geo.draw_line_segments(
    ax,[[A,K],[B,K]],ls=':')

geo.scatter_points(ax,[U,Y,K])

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ex25.png'
plt.savefig(ofn, dpi=300)