import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(-10,100))

n = 30
A = geo.Point(0,40)
B = geo.Point(n*2,40)

# use classic ratios to get right triangle
C = geo.get_intersection_circle_circle(
    [B,n*(math.sqrt(3))],[A,n])[1]
    
Q,r = geo.get_circumcircle([A,B,C])

#A,B,C = geo.rotate_points_around_center_by_angle(
    #[A,B,C],Q,theta=25)

geo.outline_polygon(ax,[A,B,C])

# drop the vertical
D = geo.get_point_perp_on_line_for_point(C,[A,B])

geo.draw_line_segments(ax,[[C,D],[C,Q]],ec='k')

aL = [[A,C,D],[A,B,C]]
geo.mark_angles(ax,aL,d=8,c='r',s=16)

points = [
          ['A',A,'SW',6],
          ['B',B,'SW',6],
          ['C',C,'NW',3],
          ['D',D,'SW',6],
          ['Q',Q,'S',4],
         ]

#geo.label_points(points)

geo.scatter_points(ax,[A,B,C,Q,D],s=5)

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/Pthm_similar.png'
plt.savefig(ofn, dpi=300)


