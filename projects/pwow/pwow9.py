import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(25,25)
B = geo.Point(75,25)
dx,dy = 10,40
C = geo.Point(A.x-dx,A.y+dy)
D = geo.Point(B.x+dx,C.y)

Q,r = geo.get_circumcircle([A,B,C])
cc = geo.get_circle(Q,r)
ax.add_patch(cc)

geo.opg(ax,[A,B,D,C])
geo.dlss(ax,[[A,D],[B,C]],ec='r',ls=(0,(2,5)))

tmp = geo.Point(B.x,B.y+dy)
H = geo.xll([C,D],[B,tmp])
geo.dls(ax,[B,H],ec='b')

box = geo.mark_right_angle(H,[D,B])
geo.opg(ax,box,ec='b')


geo.savefig(plt)

