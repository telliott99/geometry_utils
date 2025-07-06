import sys,math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

Q = geo.Point(40,40)
r = 30
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)


# draw a line
U = geo.Point(25,20)
V = geo.Point(55,35)

A,B = geo.xlc([U,V],[Q,r])
M = geo.gpf([A,B],0.5)
C = geo.gpf([A,B],0.75)

geo.dlss(ax,[[A,B],[M,Q]])

geo.scp(ax,[Q,A,B,M])
geo.scp(ax,[C],c='r')

geo.dlss(ax,[[Q,C],[Q,B]],ec='r',ls=':')


geo.label_points(
    [['A',A,'SW',4],
     ['B',B,'NE',1],
     ['C',C,'S',3],
     ['M',M,'S',4],
     ['Q',Q,'W',4],
     ])



geo.savefig(plt,ofn='EII_35.png')