import sys,path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-25,175), ylim=(0,100))

Q = geo.Point(40,50)
r = 30
circle1 = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle1)

S = geo.Point(20,10)
T = geo.get_tangent_points_on_circle_for_point(
        [Q,r],S)[1]
U = geo.get_point_by_fractional_length(
    [S,T],2.0)
V = geo.get_point_by_fractional_length(
    [S,T],0.8)

  
geo.draw_line_segments(ax,[[S,U],[Q,T]],ec='r')
geo.draw_line_segments(ax,[[Q,V]],ec='r',ls=':')
    
geo.scatter_points(ax,[Q,S,T,U,V])



T = geo.nudge(T,'E',2) 

points = [['Q',Q,'NE',4],
          ['S',S,'S',6],
          ['T',T,'S',6],
          ['U',U,'S',6],
          ['V',V,'S',6],
          ]

geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/tangent_basic.png'
plt.savefig(ofn, dpi=300)