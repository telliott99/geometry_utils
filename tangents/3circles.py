 # problem with lines tangent to two circles
# either crossing between
# or originating from a point outside the smaller one

import sys,path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-30,120), ylim=(-20,100))

# we first fix Q1,Q2
# for convenience let them be horizontal
# the distance between centers must be r1 + r2

Q1 = geo.Point(10,30)
r1 = 40
circle1 = plt.Circle(
    (Q1.x,Q1.y),r1,fc='none',ec='k')
ax.add_patch(circle1)

Q2 = geo.Point(80,30)
r2 = 30
circle1 = plt.Circle(
    (Q2.x,Q2.y),r2,fc='none',ec='k')
ax.add_patch(circle1)

# Q3 is the intersection of two circles
# on centers Q1 and Q2
# with radii r1+r3 and r2+r3
r3 = 20

# pick the point lying above the Q1-Q2 center
pL = geo.get_intersection_circle_circle(
    [Q1,r1+r3],[Q2,r2+r3])
Q3 = pL[0]

circle3 = plt.Circle(
    (Q3.x,Q3.y),r3,fc='none',ec='k')
ax.add_patch(circle3)

geo.draw_line_segments(ax,
    [[Q1,Q2],[Q1,Q3],[Q2,Q3]],ec='r',ls=':')
    
#----------
    
# specialty function to construct line
def f(cL,O,d):
    Q,r = cL
    T = geo.get_intersection_line_segment_circle(
        [O,Q],[Q,r])[0]
        
    m = geo.get_perp_slope([O,Q])
    # this needes adjustment if slope is vertical!
    # for now
    if m > 100:  m = 100
    dx = d
    dy = d * m     
    U = geo.Point(T.x+dx, T.y+dy)
    V = geo.Point(T.x-dx, T.y-dy)
    return [T,U,V]

pL1 = f([Q1,r1],Q3,30)
pL2 = f([Q1,r1],Q2,30)
pL3 = f([Q3,r3],Q2,50)

geo.draw_line_segments(
    ax,[pL1[1:], pL2[1:], pL3[1:]],ec='b',ls=':')

geo.scatter_points(ax,[Q1,Q2,Q3])
geo.scatter_points(ax,[pL1[0],pL2[0],pL3[0]])

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/3circles.png'
plt.savefig(ofn, dpi=300)