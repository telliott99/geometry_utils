import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,110), ylim=(-10,100))

A = geo.Point(10,40)
B = geo.Point(90,40)
Q = geo.get_midpoint([A,B])
r = geo.get_length([A,Q])

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

P = geo.get_point_at_angle_on_circle(
    135,[Q,r])

geo.opg(ax,[A,B,P])
box = geo.mark_right_angle(P,[A,B])
geo.opg(ax,box,ec='k')

C = geo.get_point_by_fractional_length(
    [B,P],0.45)
    
S,T = geo.xlc([Q,C],[Q,r])
geo.dls(ax,[S,T],ls=(0,(2,4)))

geo.fpg(ax,[Q,B,C])
geo.opg(ax,[Q,B,C])

geo.scp(ax,[Q,C])

geo.savefig(plt)

