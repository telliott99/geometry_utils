import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))




A = geo.Point(30,50)
B = geo.Point(60,50)
r = geo.get_length([A,B])

c1 = plt.Circle(
    (A.x,A.y),r,fc='none',ec='gray')
ax.add_patch(c1)

c2 = plt.Circle(
    (B.x,B.y),r,fc='none',ec='gray')
ax.add_patch(c2)

G = geo.get_midpoint([A,B])
tmp = geo.Point(A.x,A.y+geo.STD_LENGTH)
H = geo.xlc([A,tmp],[A,r])[1]

F = geo.xcc([A,r],[B,r])[1]

r3 = geo.get_length([G,H])
c3 = plt.Circle(
    (G.x,G.y),r3,fc='none',ec='magenta')
ax.add_patch(c3)

J = geo.xlc([A,B],[G,r3])[0]

r4 = geo.get_length([B,J])
c3 = plt.Circle(
    (B.x,B.y),r4,fc='none',ec='r')
ax.add_patch(c3)

geo.dls(ax,[A,B])
geo.dls(ax,[A,J],ls=':')

tmp = geo.get_point_by_fractional_length([A,H],1.4)
geo.dls(ax,[A,H],ls=':')

tmp = geo.get_point_by_fractional_length([G,F],2)
geo.dls(ax,[G,F],ls=':')

geo.dls(ax,[G,H],ec='magenta')

geo.scp(ax,[A,B,F,G,H,J])




geo.savefig(plt)

