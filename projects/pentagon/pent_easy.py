import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(10,10)
B = geo.Point(90,10)
Q = geo.get_midpoint([A,B])
r = geo.get_length([A,Q])
tmp = geo.Point(Q.x,Q.y+5)
C = geo.xlc([Q,tmp],[Q,r])[1]

circle = geo.get_circle(Q,r)
ax.add_patch(circle)
geo.dlss(ax,[[A,B],[Q,C]])

D = geo.gpf([Q,C],0.5)

tmp = geo.bisect_angle_Euclid(D,[Q,B])
E = geo.xll([Q,B],[D,tmp])

geo.dls(ax,[D,B],ec='r')
geo.fpg(ax,[Q,D,E])
geo.opg(ax,[Q,D,E])

tmp = geo.Point(E.x,E.y+5)
F = geo.xlc([E,tmp],[Q,r])[0]
geo.dls(ax,[E,F],ls=(0,(2,4)))

geo.scp(ax,[Q,A,B,C,D,E,F])
geo.savefig(plt)

