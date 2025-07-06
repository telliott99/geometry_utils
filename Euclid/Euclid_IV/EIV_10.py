import sys,math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

# draw the circle on center Q
# with arbitrary radius QA

A = geo.Point(5,5)
B = geo.Point(60,60)
r = geo.get_length([A,B])

circle = plt.Circle(
    (A.x,A.y),r,fc='none',ec='k')
ax.add_patch(circle)

# QA/QB = phi
phi = (5**0.5 + 1)/2
C = geo.get_point_by_fractional_length(
    [A,B],1/phi)
    
d = geo.get_length([A,C])

# first point is correct, but not what should have been first
D = geo.get_point_on_circle_at_distance_for_point(
    [A,r],d,B)[0]

geo.fpg(ax,[B,C,D])
geo.opg(ax,[B,C,D])
geo.dlss(ax,[[A,C],[A,D]])

Q,rho = geo.get_circumcircle([A,C,D])

circle2 = plt.Circle(
    (Q.x,Q.y),rho,fc='none',ec='k',ls=':')
ax.add_patch(circle2)



geo.scp(ax,[A,B,C,D],c='k',s=6)


geo.savefig(plt,ofn='EIV_10.png')