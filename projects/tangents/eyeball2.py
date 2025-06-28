# problem with lines tangent to two circles
# either crossing between
# or originating from a point outside the smaller one

import sys
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-25,175), ylim=(0,100))

Q1 = geo.Point(35,50)
r1 = 15
circle1 = plt.Circle(
    (Q1.x,Q1.y),r1,fc='none',ec='k')
ax.add_patch(circle1)

Q2 = geo.Point(120,50)
r2 = 40
circle2 = plt.Circle(
    (Q2.x,Q2.y),r2,fc='none',ec='k')
ax.add_patch(circle2)

'''
x/r1 = (x+d)/r2
x/(x+d) = r1/r2
1 + d/x = r2/r1
d/x = r2/r1-1
'''

# center line is horizontal
d = Q2.x - Q1.x

tmp = r2/r1 - 1
# x1 is the distance P lies away from Q1 to left
x1 = d/tmp
P = geo.Point(Q1.x-x1, Q1.y)
B,C = geo.get_tangent_points_on_circle_for_point([Q2,r2],P)
A,D = geo.get_tangent_points_on_circle_for_point([Q1,r1],P)

geo.draw_line_segment(ax,[P,B],ec='r')
geo.draw_line_segment(ax,[P,C],ec='r')

#----

tmp = r2/r1 + 1
# x2 is the distance X lies away from Q1 to right
x2 = d/tmp
X = geo.Point(Q1.x+x2,Q1.y)

# S,T on Q1
[S,T] = geo.get_tangent_points_on_circle_for_point([Q1,r1],X)
[U,V] = geo.get_tangent_points_on_circle_for_point([Q2,r2],X)

#----

points = [['P',P,'N',2],
          ['X',X,'N',4],
          ['A',A,'N',2],
          ['B',B,'N',2],
          ['C',C,'NE',1],
          ['D',D,'N',2],
          ['S',S,'N',1],
          ['T',T,'SE',3],
          ['U',U,'S',6],
          ['V',V,'N',1]]
          
#geo.label_points(points)

geo.label_points(
    [['P',P,'N',2],['O',Q1,'N',2],['Q',Q2,'N',2]])
geo.draw_line_segment(ax,[P,Q2],ls=':')
          
I1 = geo.get_intersection_for_two_lines([S,V],[A,B])
I2 = geo.get_intersection_for_two_lines([S,V],[C,D])
I3 = geo.get_intersection_for_two_lines([T,U],[A,B])
I4 = geo.get_intersection_for_two_lines([T,U],[C,D])

geo.draw_line_segment(ax,[I1,I2],ec='b')
geo.draw_line_segment(ax,[I3,I4],ec='b')

geo.scatter_points(ax,[P,A,B,C,D])
geo.scatter_points(ax,[X,S,T,U,V],c='r')
geo.scatter_points(ax,[I1,I2,I3,I4],c='b')
geo.scatter_points(ax,[Q1,Q2])


points = [['K',I1,'N',2],
          ['M',I2,'NE',1],
          ['L',I3,'N',3],
          ['N',I4,'S',6]]
          
#geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/eyeball2.png'
plt.savefig(ofn, dpi=300)