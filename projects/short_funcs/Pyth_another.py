import sys,math
import matplotlib.pyplot as plt
import numpy as np

# contrary to best practice
# import *all* the symbols from the library
import geometry as geo
from geometry import *

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

'''
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)
'''

'''
gtr =  get_standard_triangle
scp =  scatter_points
dls =  draw_line_segment
dlss = draw_line_segments
fpg =  fill_polygon
opg =  outline_polygon
gpf =  get_point_by_fractional_length
gpp =  get_perp_at_point_by_fractional_length
gcc =  get_circumcircle
goa =  get_orthocenter_and_altitudes
gcm =  get_centroid_and_medians
gib =  get_incenter_and_bisectors
xll =  get_intersection_for_two_lines
xlc =  get_intersection_line_segment_circle
xcc =  get_intersection_circle_circle
bae =  bisect_angle_Euclid
rpa =  rotate_points_around_center_by_angle
mvp =   translate_points
sct =  scale_triangle
mka =   mark_angle
mra =  mark_right_angle
grl  =  get_rectangle_for_line
'''

A,B = geo.Point(10,40), geo.Point(60,40)
Q = gpf([A,B],0.5)
r = geo.get_length([A,Q])
ax.add_patch(plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k'))


C = get_point_on_circle_at_distance_for_point([Q,r],25,B)[0]
fpg(ax,[A,B,C])
opg(ax,[A,B,C])

#lss(ax,[[A,B]],ec='r')

D = gpf([B,C],0.5)
S,T = xlc([D,Q],[Q,r])
dls(ax,[S,T],ec='b',ls=':',lw=1.5)

rL = gpp([S,Q],1.0)
U,V = xlc(rL,[Q,r])
dls(ax,[U,V],ec='b',ls=':',lw=1.5)

P = xll([S,T],[B,C])
#sp(ax,[P])
R = xll([U,V],[A,C])
#scp(ax,[R])


#sp(ax,[A,B,C,Q])
scp(ax,[A,B])

box = mra(R,[A,Q])
opg(ax,box,ec='k')
box = mra(C,[A,B])
opg(ax,box,ec='k')
box = mra(Q,[R,S])
opg(ax,box,ec='k')

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/Pyth_another.png'
plt.savefig(ofn, dpi=300)