import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(-50,100))

pL = geo.get_standard_triangle()
A,B,C = pL
C = geo.nudge(C,'S',20)

geo.fill_polygon(ax,[A,B,C])
geo.outline_polygon(ax,[A,B,C])

O,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle(
    (O.x,O.y),r,fc='none',ec='k')
ax.add_patch(circle)

oD = geo.get_orthocenter_and_altitudes([A,B,C])

D = oD['D']
E = oD['E']
F = oD['F']
H = oD['H']

X = geo.get_intersection_line_segment_circle(
    [C,F],[O,r])[1]

Y = geo.get_intersection_line_segment_circle(
    [A,D],[O,r])[1]

geo.draw_line_segments(
    ax,[[A,D],[B,E],[C,X],[A,Y]])
geo.draw_line_segments(
    ax,[[A,X],[B,X]],ls=':')


box = geo.mark_right_angle(D,[A,C])
geo.outline_polygon(ax,box,ec='k')
box = geo.mark_right_angle(E,[A,B])
geo.outline_polygon(ax,box,ec='k')
box = geo.mark_right_angle(F,[C,B])
geo.outline_polygon(ax,box,ec='k')


aL = [[H,A,F],[B,C,X],[B,A,X]]
geo.mark_angles(ax,aL,d=5,c='r',s=20)

geo.scatter_points(ax,[A,B,C,H,X],s=6)

points = [
          ['A',A,'SW',6],
          ['B',B,'S',5],
          ['C',C,'NW',5],
          ['D',D,'NW',4],
          #['E',E,'W',5],
          ['F',F,'S',6],
          ['H',H,'E',5],
          ['X',X,'SW',7],
         ]

geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/extended_altitude.png'
plt.savefig(ofn, dpi=300)