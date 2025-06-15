import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,140), ylim=(-20,100))
lw=1.4


pL = geo.get_standard_triangle()
A,B,C = pL
A,B,C = geo.scale_triangle([A,B,C],0.7)
C = geo.nudge(C,'S',15)


Q,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

# go to circumcircle for ABC through A at slope m
D = geo.get_point_for_cyclic_quadrilateral(A,[B,C],m=0.45)

def panel_a():
    geo.draw_line_segments(ax,[[A,B],[C,D]],ec='r',lw=lw)
    geo.draw_line_segments(ax,[[A,C],[B,D]],ec='cyan',lw=lw)
    geo.draw_line_segments(ax,[[A,D],[B,C]],ec='m',lw=lw)
    geo.scatter_points(ax,[D],s=8)
    
    
#panel_a()

def panel_b():
    geo.draw_line_segments(ax,[[A,B],[A,C],[B,C]],ec='r')
    geo.draw_line_segments(ax,[[D,B],[D,C]],ec='b')
    geo.fill_polygon(ax,[A,B,C])
    geo.fill_polygon(ax,[D,B,C],fc='b',alpha=0.15)
    geo.scatter_points(ax,[D],s=8)

panel_b()



geo.scatter_points(ax,[A,B,C,D],s=8)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ptolemy.png'
plt.savefig(ofn, dpi=300)