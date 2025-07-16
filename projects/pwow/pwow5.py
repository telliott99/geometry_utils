import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(20,20)
B = geo.Point(90,20)

S = geo.get_point_at_angle_on_circle(
    60,[A,10])
T = geo.get_point_at_angle_on_circle(
    120,[B,10])
C = geo.xll([A,S],[B,T])

geo.opg(ax,[A,B,C])
geo.fpg(ax,[A,B,C])

iD = geo.get_incenter_and_bisectors(
    [A,B,C])

I = iD['I']
Y = iD['Y']
r = geo.get_length([I,Y])
cl = geo.get_circle(I,r,fc='white',ec='k')
ax.add_patch(cl)

D = geo.get_point_by_fractional_length(
    [I,Y],2.0)

geo.opg(ax,[C,I,D],ec='b')





geo.savefig(plt)

