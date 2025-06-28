import sys,math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(9,100))

A = geo.Point(10,10)
B = geo.Point(90,10)

Q = geo.get_point_by_fractional_length(
    [A,B],0.5)
r = geo.get_length([A,Q])

# problem with different alpha for fc and ec
# didn't work yet here
t = colors.to_rgba('b',alpha=0.2)

circle = plt.Circle(
    (Q.x,Q.y),r,fc='r',ec='r',alpha=0.4)
ax.add_patch(circle)

rL = geo.get_rectangle_for_line([A,B])
print(rL)
C,D = rL[2:]

geo.outline_polygon(ax,rL)

T = geo.get_tangent_points_on_circle_for_point(
    [Q,r],D)[0]

geo.scatter_points(ax,rL)

E = geo.get_intersection_for_two_lines(
    [D,T],[B,C])
geo.draw_line_segment(ax,[D,E])

geo.fill_polygon(ax,[C,D,E],fc='gray',alpha=0.5)


geo.scatter_points(ax,[E,T])

points = [
          ['A',A,'S',5],
          ['B',B,'S',5],
          ['C',C,'N',2],
          ['D',D,'N',2],
          ['T',T,'N',3],
          ['E',E,'E',1],
         ]

geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/problem.png'
plt.savefig(ofn, dpi=300)