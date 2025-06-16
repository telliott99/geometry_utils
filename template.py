import sys,math
import matplotlib.pyplot as plt
import numpy as np

# contrary to best practice
# import *all* the symbols from the library
# import geometry as geo
from geometry import *

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

'''
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)
'''

tr =  get_standard_triangle
sc =  scatter_points
ls =  draw_line_segments
fp =  fill_polygon
op =  outline_polygon
pf =  get_point_by_fractional_length
cc =  get_circumcircle
oa =  get_orthocenter_and_altitudes
cm =  get_centroid_and_medians
ib =  get_incenter_and_bisectors
xll = get_intersection_for_two_lines
xlc = geo.get_intersection_line_segment_circle(pL,cL)
xcc = geo.get_intersection_circle_circle(cL1,cL2)
ba =  bisect_angle_Euclid(A,pL)
rp =  rotate_points_around_center_by_angle(pL,Q,theta)
tp =  translate_points(pL,dx=0,dy=0)
st =  scale_triangle(pL,f=1.0)
ma =  mark_angle(pL,d=5)
mra = mark_right_angle(A,pL,n=3)
rl  = get_rectangle_for_line








#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/problem.png'
plt.savefig(ofn, dpi=300)