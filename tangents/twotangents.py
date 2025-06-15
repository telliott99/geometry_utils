# problem with lines tangent to two circles
# either crossing between
# or originating from a point outside the smaller one

import sys
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(0,100))

Q = geo.Point(50,50)
r = 30
circle1 = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle1)

# let points be on horizontal for convenience
P = geo.Point(0,50)
X = geo.Point(90,50)

# order of return changed
A,D = geo.get_tangent_points_on_circle_for_point([Q,r],P)
S,T = geo.get_tangent_points_on_circle_for_point([Q,r],X)

K = geo.get_intersection_for_two_lines([P,A],[X,S])
N = geo.get_intersection_for_two_lines([P,D],[X,T])


geo.draw_line_segments(ax,
    [[P,K],[P,N],[X,K],[X,N]],ec='r')

geo.draw_line_segment(ax,[P,X],ls=':')

geo.scatter_points(ax,[Q,P,X,A,D,S,T,K,N])


points = [['Q',Q,'N',2],
          ['P',P,'NW',2],
          ['X',X,'N',2],
          ['A',A,'NW',2],
          ['D',D,'SW',6],
          ['S',S,'N',2],
          ['T',T,'SE',2],
          ['K',K,'NW',2],
          ['N',N,'S',4]]
          
geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/twotangents.png'
plt.savefig(ofn, dpi=300)