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
'''
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

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/problem.png'
plt.savefig(ofn, dpi=300)