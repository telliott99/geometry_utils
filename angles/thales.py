import sys,math,path
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,150), ylim=(0,100))

O = geo.Point(30,50)
r = 30
circle1 = plt.Circle(
    (O.x,O.y),r,fc='none',ec='k')
ax.add_patch(circle1)

P = geo.Point(0,O.y)
Q = geo.Point(60,O.y)  
geo.draw_line_segment(ax,[P,Q])

R = geo.rotate_points_around_center_by_angle(
    [Q],O,50)[0]

geo.fill_polygon(ax,[P,Q,R])
geo.outline_polygon(ax,[P,Q,R],ec='r')

O2,A,B,C = geo.translate_points([O,P,Q,R],dx=85)

circle2 = plt.Circle(
    (O2.x,O2.y),r,fc='none',ec='k')
ax.add_patch(circle2)

geo.fill_polygon(ax,[A,B,C])
geo.outline_polygon(ax,[A,B,C],ec='r')

aL = [[A,B,C],[B,C,O2]]
geo.mark_angles(ax,aL,c='k')

aL = [[O2,C,A],[C,A,B]]
geo.mark_angles(ax,aL,c='r',d=10)

geo.draw_line_segment(ax,[O2,C],ec='r',ls=':')

geo.scatter_points(ax,[O,P,Q,R,O2,A,B,C],s=6)

points = [
          ['O',O,'SW',6],
          ['O',O2,'SW',6],

          ['P',P,'W',4],
          ['Q',Q,'E',2],
          ['R',R,'E',2],

          ['P',A,'W',4],
          ['Q',B,'E',2],
          ['R',C,'E',2],
         ]

geo.label_points(points)


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/thales.png'
plt.savefig(ofn, dpi=300)