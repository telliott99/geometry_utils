import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-30,100), ylim=(0,100))

A = geo.Point(20,40)
B = geo.Point(80,40)

Q = geo.get_midpoint([A,B])
r = geo.get_length([A,Q])

circle = geo.get_circle(Q,r)
ax.add_patch(circle)

C = geo.get_point_at_angle_on_circle(50, [Q,r])

geo.fill_sector(ax,Q,r,B,C,fc='r',alpha=0.2)
geo.fpg(ax,[Q,B,C],alpha=0.4)
geo.dlss(ax,[[A,B],[B,C],[Q,C]],ec='r')
geo.dls(ax,[A,C],ls=(0,(2,4)))

geo.scp(ax,[A,B,C,Q],s=5)


geo.savefig(plt)

