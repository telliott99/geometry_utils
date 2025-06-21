import sys,math
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

# contrary to best practice
# import *all* the symbols from the library
from geometry import *

fig, ax = geo.init()
ax.set(xlim=(-20,120), ylim=(-30,100))

'''
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)


gtr =  get_standard_triangle
sp =  scatter_points
lss =  draw_line_segments
fpg =  fill_polygon
opg =  outline_polygon
gpf =  get_point_by_fractional_length
gcc =  get_circumcircle
goa =  get_orthocenter_and_altitudes
gcm =  get_centroid_and_medians
gib =  get_incenter_and_bisectors
xll = get_intersection_for_two_lines
xlc = get_intersection_line_segment_circle
xcc = get_intersection_circle_circle
ba =  bisect_angle_Euclid
rp =  rotate_points_around_center_by_angle
tp =  translate_points
sct =  scale_triangle
ma =  mark_angle
mra = mark_right_angle
rl  = get_rectangle_for_line

'''

#----------

pL = gtr()
A,B,C = pL
opg(ax,pL)
fpg(ax,pL)

O,_ = gcc(pL)

K = gpf([A,B],0.5)
L = gpf([B,C],0.5)
M = gpf([C,A],0.5)
pL2 = [K,L,M]

N,r = gcc(pL2)
ax.add_patch(plt.Circle(
    (N.x,N.y),r,fc='none',ec='k'))
opg(ax,pL2,ec='b',lw=1.5)
    
oD = goa(pL)
D,E,F = oD['D'],oD['E'],oD['F']

pL3 = rp([K,L,M],N,180)
opg(ax,pL3,ec='g',lw=1.5)

lss(ax,[[A,D],[B,E],[C,F]],ec='g',ls=':')

sp(ax,[A,B,C,D,E,F,K,L,M,N])
sp(ax,[K,L,M],c='b')
sp(ax,[D,E,F],c='g')
sp(ax,pL3,c='g')



#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ninepoint_rev.png'
plt.savefig(ofn, dpi=300)