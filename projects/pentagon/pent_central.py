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

geo.dlss(ax,[[Q,C],[Q,D]],ec='k')
geo.opg(ax,[A,C,D])
geo.fpg(ax,[A,C,D])

geo.opg(ax,[Q,C,D])
geo.fpg(ax,[Q,C,D],alpha=0.3)

geo.scp(ax,[A,B,C,D,E,Q])


geo.savefig(plt)

