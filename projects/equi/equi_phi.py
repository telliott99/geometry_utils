import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(20,20)
B = geo.Point(80,20)
C = geo.xcc([A,60],[B,60])[1]

geo.opg(ax,[A,B,C])

Q,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

M = geo.get_midpoint([A,C])
N = geo.get_midpoint([B,C])
U,V = geo.xlc([M,N],[Q,r])
geo.dls(ax,[U,V])

geo.fpg(ax,[C,U,N])
geo.opg(ax,[C,U,N])

geo.fpg(ax,[N,V,B],fc='b',alpha=0.2)
geo.opg(ax,[N,V,B],ec='b')


geo.scp(ax,[A,B,C])

geo.savefig(plt)