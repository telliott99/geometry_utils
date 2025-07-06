import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,200), ylim=(-10,100))

pL = geo.get_standard_triangle(mode='right')
A,B,C = pL

# it would be easier to just start with isosceles
# but this is a new function

Q,r = geo.get_circumcircle(pL)

# reflect in hoz across vertical line through Q
qL = geo.mirror_points(pL,[Q])
D,E,F = qL

d = D.x-E.x
rL = geo.translate_points(pL,dx=d,dy=0)

geo.outline_polygon(ax,rL,ec='k')
geo.outline_polygon(ax,qL,ec='r')

geo.fill_polygon(ax,qL)
geo.fill_polygon(ax,rL,fc='b',alpha=0.2)

geo.scatter_points(ax,[A,B,E,F,rL[1]],s=6)
points = [
          ['A',A,'S',6],
          ['B',B,'S',6],
          ['C',F,'NW',5],
          ['D',rL[1],'S',6],
         ]

geo.label_points(points)


geo.savefig(plt)


