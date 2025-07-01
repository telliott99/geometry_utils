import sys,math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

Q = geo.Point(40,40)
r = 30
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

A = geo.get_point_at_angle_on_circle(
    0,[Q,r])
B = geo.get_point_at_angle_on_circle(
    30,[Q,r])
C = geo.get_point_at_angle_on_circle(
    60,[Q,r])
    
geo.scp(ax,[A,Q])
geo.scp(ax,[B],c='r')
geo.scp(ax,[C],c='b')


geo.savefig(plt,ofn='ex27.png')