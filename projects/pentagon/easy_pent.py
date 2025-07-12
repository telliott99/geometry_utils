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

S = geo.xll([A,B],[C,D])
geo.fpg(ax,[B,C,S],fc='b',alpha=0.2)

geo.fpg(ax,[A,C,D])

geo.fpg(ax,[E,B,C],alpha=0.4)

geo.draw_chained_line_segments(ax,pL,ec='r')
geo.dls(ax,[A,D],ec='r')
geo.dlss(ax,[[A,C],[B,D],[B,E],[C,E]],
    ls=(0,(3,5)))


geo.opg(ax,[B,S,C],ec='b')

geo.scp(ax,[A,B,C,D,E,S])


geo.savefig(plt)

