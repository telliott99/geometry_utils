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

geo.draw_chained_line_segments(ax,pL,ec='r')

geo.dlss(ax,[[Q,A],[Q,B],[Q,E]],ec='k')
#geo.opg(ax,[A,C,D])
#geo.fpg(ax,[A,C,D])

geo.opg(ax,[Q,C,D])
geo.fpg(ax,[Q,C,D],alpha=0.3)

t = (0,(2,4))

M = geo.get_midpoint([C,D])
N = geo.get_midpoint([D,E])
geo.dlss(ax,[[Q,M],[Q,N]],ls=t)

geo.scp(ax,[A,B,C,D,E,Q])

'''
Q,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)
'''

geo.savefig(plt)

