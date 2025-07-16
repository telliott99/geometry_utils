import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(0,100))


O = geo.Point(20,40)
r1 = 20
c1 = geo.get_circle(O,r1)
ax.add_patch(c1)

Q = geo.Point(55,40)
r2 = 30
c2 = geo.get_circle(Q,r2)
ax.add_patch(c2)

P = geo.get_point_at_angle_on_circle(
    170,[O,r1])
    
A,B = geo.xcc([O,r1],[Q,r2])
    
S = geo.xlc([P,A],[Q,r2])[1]
T = geo.xlc([P,B],[Q,r2])[1]

R = geo.get_point_at_angle_on_circle(
    195,[O,r1])

U = geo.xlc([R,A],[Q,r2])[1]
V = geo.xlc([R,B],[Q,r2])[1]

geo.dlss(ax,[[P,S],[P,T]])
geo.dlss(ax,[[R,U],[R,V]],ls=(0,(2,3)))

geo.dls(ax,[S,T],ec='r')
geo.dls(ax,[U,V],ec='b')

    
geo.scp(ax,[P,A,B,R,S,T,U,V])

geo.savefig(plt)

