import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(25,52)
B = geo.Point(85,52)
C = geo.Point(40,75)

geo.opg(ax,[A,B,C])

Q,r = geo.get_circumcircle([A,B,C])
cc = geo.get_circle(Q,r)
ax.add_patch(cc)

tmp = geo.Point(C.x,C.y+5)
F = geo.xll([C,tmp],[A,B])

P = geo.xlc([C,Q],[Q,r])[1]

geo.dlss(ax,[[C,P],[C,F]])
geo.dls(ax,[B,P],ls=':')

geo.scp(ax,[Q],s=4)

aL = [[B,A,C],[C,P,B]]
geo.mark_angles(ax,aL,d=5,c='r',s=15)

geo.savefig(plt)

