import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-30,100), ylim=(0,100))


Q = geo.Point(60,50)
r = 35

pL = []
for i in range(1,6):
     theta = i*72 + 18
     P = geo.get_point_at_angle_on_circle(
         theta,[Q,r])
     pL.append(P)
A,B,C,D,E = pL

geo.opg(ax,pL)

geo.dlss(ax,[[A,C],[A,D],[B,D],[B,E],[C,E]],ec='k')
geo.fpg(ax,[A,C,D],alpha=0.2)

S = geo.xll([B,D],[C,E])
T = geo.xll([A,D],[C,E])
U = geo.xll([A,D],[B,E])
V = geo.xll([A,C],[B,E])
W = geo.xll([A,C],[B,D])

geo.fpg(ax,[B,V,W],fc='g',alpha=0.2)
geo.fpg(ax,[A,T,E],fc='b',alpha=0.2)

Q,r = geo.gcc([A,B,C])
circle = geo.get_circle(Q,r)
ax.add_patch(circle)

geo.scp(ax,[A,B,C,D,E],s=5)


geo.savefig(plt)

