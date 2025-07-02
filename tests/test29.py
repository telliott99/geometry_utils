import sys,math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,110), ylim=(-10,100))


A = geo.Point(50,5)
B = geo.Point(50,55)
Q = geo.get_point_by_fractional_length(
    [A,B],0.5)

s = geo.get_length([A,B])
r = s/2

C = geo.Point(B.x+s,B.y)
D = geo.Point(A.x+s,A.y)
E = geo.Point(B.x-s,B.y)
F = geo.Point(A.x-s,A.y)

geo.opg(ax,[A,B,C,D])
geo.fpg(ax,[A,B,C,D],fc='k',alpha=1.0)

geo.opg(ax,[A,B,E,F])
geo.fpg(ax,[A,B,E,F],fc='k',alpha=0.1)

circle = plt.Circle(
    (Q.x,Q.y),r,fc='w',ec='r',alpha=1.0)
ax.add_patch(circle)

geo.dls(ax,[D,E],ec='r',lw=1,ls=':')

geo.scp(ax,[A,B,C,D,E,F,Q],c='r',s=6)

X = geo.get_intersection_line_segment_circle(
    [D,E],[Q,r])[1]
geo.scp(ax,[X],c='k',s=15)


geo.savefig(plt)