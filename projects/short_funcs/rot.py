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

#----------

# p3 test26a.py 32

arg = sys.argv[1]
n = int(arg)
n+=1

pL = gtr()
scp(ax,pL,s=6)
if not n > 32:
    opg(ax,pL,lw=2)

Q,r = gcc(pL)
ax.add_patch(plt.Circle((Q.x,Q.y),r,fc='none',ec='k'))

for i in range(1,n):
    theta = 5*i
    rL = rpa(pL,Q,theta)
    opg(ax,rL,ec='b')


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/rot_' + arg + '.png'
plt.savefig(ofn, dpi=300)