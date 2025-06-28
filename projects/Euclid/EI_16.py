import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(-10,100))

pL = geo.get_standard_triangle()
A,B,C = pL

A,B,C = geo.scale_triangle([A,B,C],0.6)

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

P = geo.get_point_parallel_to_line_for_point(
    [A,C],B)
d = geo.get_length([A,C])
f = d/(geo.get_length([B,P]))
D = geo.get_point_by_fractional_length(
    [B,P],f)

E = geo.get_intersection_for_two_lines(
    [B,C],[A,D])

geo.fill_polygon(ax,[A,B,D],fc='b',alpha=0.15)

geo.draw_line_segments(
    ax,[[A,D],[B,D]],ec='b')
    
S = geo.get_point_by_fractional_length(
    [C,B],1.3)
T = geo.get_point_by_fractional_length(
    [A,B],1.4)

geo.draw_line_segments(
    ax,[[B,S],[B,T]],ec='k')


geo.scatter_points(ax,[A,B,C,D,E,S,T])

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/EI_18.png'
plt.savefig(ofn, dpi=300)