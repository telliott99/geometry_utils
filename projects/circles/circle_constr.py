import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-30,100), ylim=(0,100))

Q = geo.Point(50,50)
r = 40

circle = geo.get_circle(Q,r)
circle.set_edgecolor('k')
ax.add_patch(circle)

A = geo.get_point_at_angle_on_circle(210, [Q,r])
B = geo.get_point_at_angle_on_circle(  0, [Q,r])
C = geo.get_point_at_angle_on_circle(125, [Q,r])


K = geo.get_midpoint([A,B])
L = geo.get_midpoint([A,C])
M = geo.get_midpoint([B,C])

geo.opg(ax,[A,B,C])

geo.fpg(ax,[Q,A,C],fc='r',alpha=0.4)
geo.fpg(ax,[Q,B,C],fc='b',alpha=0.2)
geo.fpg(ax,[Q,A,B],fc='g',alpha=0.2)

box = geo.mra(K,[B,Q])
geo.opg(ax,box,ec='k')

box = geo.mra(L,[A,Q])
geo.opg(ax,box,ec='k')

box = geo.mra(M,[C,Q])
geo.opg(ax,box,ec='k')

tmp = geo.get_point_by_fractional_length(
    [K,Q],1.5)
geo.dls(ax,[K,tmp],ls=(0,(2,4)))

tmp = geo.get_point_by_fractional_length(
    [L,Q],1.5)
geo.dls(ax,[L,tmp],ls=(0,(2,4)))

tmp = geo.get_point_by_fractional_length(
    [M,Q],1.5)
geo.dls(ax,[M,tmp],ls=(0,(2,4)))


geo.scp(ax,[A,B,C,Q],s=5)


geo.savefig(plt)

