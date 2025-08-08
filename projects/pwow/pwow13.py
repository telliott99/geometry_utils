import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,110), ylim=(-10,100))

phi = (5**0.5 + 1)/2

A = geo.Point(10,40)
B = geo.Point(90,40)
_,_,C,D = geo.get_rectangle_for_line([A,B],f=1/phi)

d = geo.get_length([A,D])/2
f = d/geo.get_length([A,B])
E = geo.gpf([A,B],f)

r1 = geo.get_length([D,E])
circle1 = plt.Circle(
    (E.x,E.y),r1,fc='none',ec='k')
ax.add_patch(circle1)

r2 = geo.get_length([A,B])
circle2 = plt.Circle(
    (A.x,A.y),r2,fc='none',ec='gray')
ax.add_patch(circle2)

circle3 = plt.Circle(
    (D.x,D.y),r2,fc='none',ec='gray')
ax.add_patch(circle3)

F = geo.xcc([D,r2],[A,r2])[1]

geo.dls(ax,[E,D],ec='r')
geo.opg(ax,[A,B,C,D])

geo.fpg(ax,[A,D,F])

geo.scp(ax,[E,F])

geo.savefig(plt)

