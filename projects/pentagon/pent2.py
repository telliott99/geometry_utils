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

pL = pL + [A,B]
for i in range(5):
    geo.dls(ax,[pL[i],pL[i+2]])
    
geo.opg(ax,[A,C,D])
geo.fpg(ax,[A,C,D])

#geo.scp(ax,[A,B,C,D,E])

aL = [[B,A,C],[A,B,E],[A,E,B],[D,A,E],
      [E,C,D],[B,D,C]]
geo.mark_angles(ax,aL,d=10,c='r',s=20)

aL = [[C,A,D],[A,C,E],[A,D,B]]
geo.mark_angles(ax,aL,d=10,c='k',s=20)


geo.savefig(plt)

