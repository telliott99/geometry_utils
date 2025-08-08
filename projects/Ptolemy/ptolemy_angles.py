import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,110), ylim=(-30,100))


pL = geo.get_standard_triangle()
A,B,C = pL

Q,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

# go to circumcircle for ABC through A at slope m
D = geo.get_point_for_cyclic_quadrilateral(A,[B,C],m=0.4)

geo.outline_polygon(ax,[A,B,D,C])
geo.draw_line_segments(
    ax,[[A,D],[B,C]])

# eyeball it
F = geo.get_point_by_fractional_length(
    [A,D],0.2847)
#print(geo.get_angle(C,[B,D]))
#print(geo.get_angle(C,[A,F]))

geo.draw_line_segments(
    ax,[[C,F]])

aL = [[B,C,D],[A,C,F],[B,A,D]]
geo.mark_angles(ax,aL,d=15,c='r')

aL = [[A,B,C],[A,D,C]]
geo.mark_angles(ax,aL,d=10,c='b')

aL = [[F,C,B]]
#geo.mark_angles(ax,aL,d=15,c='orange')

aL = [[C,A,D],[C,B,D]]
geo.mark_angles(ax,aL,d=10,c='k')

def f():
    geo.fill_polygon(ax,[A,B,C])
    geo.fill_polygon(ax,[C,F,D],fc='b',alpha=0.15)

def g():
    X = geo.get_intersection_for_two_lines(
        [A,D],[B,C])
    geo.fill_polygon(ax,[A,F,C])
    geo.fill_polygon(ax,[C,B,D],fc='b',alpha=0.15)

#f()
g()

geo.scatter_points(ax,[A,B,C,D],s=8)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ptolemy_angles.png'
plt.savefig(ofn, dpi=300)