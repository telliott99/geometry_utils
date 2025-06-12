import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,110), ylim=(0,100))

y = 10
r = 40
Q = geo.Point(50,y+r)
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

E = geo.Point(0,y)
F = geo.Point(100,y)
geo.draw_line_segment(ax,[E,F])

B = geo.Point(50,y)
A = geo.Point(50,y+r*2)

D = geo.get_point_on_circle_at_distance_for_point(
    [Q,r],30,A)[1]

C = geo.get_point_on_circle_at_distance_for_point(
    [Q,r],40,D)[1]

geo.draw_line_segments(ax,[[A,B],[E,F]])

geo.fill_polygon(ax,[A,B,D])
geo.outline_polygon(ax,[A,B,D],ec='r')
geo.fill_polygon(ax,[D,B,C],fc='b',alpha=0.2)
geo.outline_polygon(ax,[C,B,D],ec='b')


geo.scatter_points(ax,[A,B,C,D,E,F])

points = [
          ['A',A,'N',2],
          ['B',B,'S',5],
          ['C',C,'E',2],
          ['D',D,'N',2],
          ['E',E,'S',5],
          ['F',F,'S',5],
         ]

geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/EIII_32.png'
plt.savefig(ofn, dpi=300)