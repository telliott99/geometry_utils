import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-50,150), ylim=(-30,150))

pL = geo.get_standard_triangle()
A,B,C = pL
B = geo.nudge(B,'N',14)
C = geo.nudge(C,'N',30)

# finds intercept for line through A with slope m
D = geo.get_point_for_cyclic_quadrilateral(
    A,[B,C],m=0.5)

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

Q,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

L = geo.get_point_by_fractional_length(
    [A,B],1.4)
    
print(geo.get_angle(B,[C,D]))
print(geo.get_angle(B,[D,L]))

geo.draw_line_segments(ax,[[B,D],[B,L]])
geo.draw_line_segments(ax,[[A,D],[C,D]],ec='b')

geo.scatter_points(ax,[A,B,C,D,L])


points = [
          ['A',A,'SW',8],
          ['B',B,'S',7],
          ['C',C,'NW',4],
          ['D',D,'E',4],
          ['E',L,'S',7]
         ]

geo.label_points(points)


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/cq_problem.png'
plt.savefig(ofn, dpi=300)