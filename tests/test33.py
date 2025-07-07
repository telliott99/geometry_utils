import geometry as geo
import matplotlib.pyplot as plt

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(30,50)
B = geo.Point(70,50)

C = geo.get_point_at_angle_length_for_point(
    75,40,A)

D,E,F = geo.get_three_parallelograms_for_triangle([A,B,C])
geo.scp(ax,[D,E,F])

geo.opg(ax,[B,C,D],ec='g',lw=1.5)
geo.opg(ax,[A,C,F],ec='r',lw=1.5)
geo.opg(ax,[A,B,E],ec='b',lw=1.5)

geo.savefig(plt)
