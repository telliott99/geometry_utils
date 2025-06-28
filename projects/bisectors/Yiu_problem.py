import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))


A = geo.Point(10,10)
B = geo.Point(50,10)
C = geo.get_point_by_fractional_length([A,B],2.0)

# default is square
rect =  geo.get_rectangle_for_line([A,B])

E,D = rect[2:]
F = geo.Point(C.x,D.y)

geo.draw_line_segments(
    ax,[[A,C],[D,F],[A,D],[B,E],[D,E],[C,F],[C,D]])

geo.fill_polygon(ax,[A,C,D])

M = geo.bisect_angle_Euclid(D,[A,C])
P = geo.get_intersection_for_two_lines(
    [A,B],[D,M])
geo.draw_line_segment(
    ax,[D,P],ec='r')
aL = [[P,D,A],[C,D,P]]

geo.mark_angles(ax,aL,c='m',d=8,s=20)

points = [
          ['A',A,'S',4],
          ['B',B,'S',4],
          ['C',C,'S',4],
          ['D',D,'N',2],
          ['E',E,'N',2],
          ['F',F,'N',2],
          ['P',P,'S',4],
         ]

geo.label_points(points)

geo.scatter_points(ax,[A,B,C,D,E,F,P],s=6)


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/Yiu_problem.png'
plt.savefig(ofn, dpi=300)