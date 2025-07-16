import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

pL = geo.gtr()
pL = geo.scale_triangle(pL,f=0.8)
pL = geo.translate_points(pL,dy=10)
A,B,C = pL

C = geo.nudge(C,'S',10)
pL = [A,B,C]

geo.opg(ax,pL)

Q,r = geo.get_circumcircle([A,B,C])
K = geo.get_midpoint([B,C])

geo.dlss(ax,[[C,Q],[Q,K]])

cc = plt.Circle(
        (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(cc)

oD = geo.get_orthocenter_and_altitudes(pL)
F = oD['F']
geo.dls(ax,[C,F])

geo.dlss(ax,[[B,Q],[C,Q],[Q,K]])

aL = [[C,A,B],[C,Q,K]]
geo.mark_angles(ax,aL,d=5,c='r',s=20)

box = geo.mark_right_angle(K,[Q,B])
geo.opg(ax,box,ec='k')

box = geo.mark_right_angle(F,[C,B])
geo.opg(ax,box,ec='k')


geo.savefig(plt)

