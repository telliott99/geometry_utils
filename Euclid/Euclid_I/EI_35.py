import geometry as geo
import matplotlib.pyplot as plt

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(10,10)
B = geo.Point(35,10)


A,B,C,D = geo.get_parallelogram_for_line(
        [A,B],135,aspect_ratio=1.5)

tmp,_ = geo.get_points_at_angle_to_line(
    115,[A,B])
E = geo.xll([C,D],[A,tmp])
M = geo.get_point_by_fractional_length([A,E],0.5)
F = geo.get_point_by_fractional_length([B,M],2.0)

geo.opg(ax,[A,B,C,D])
geo.opg(ax,[A,B,E,F],ec='b')

geo.fpg(ax,[A,B,C,D])
geo.fpg(ax,[A,B,E,F],fc='b',alpha=0.2)

geo.dls(ax,[E,D],ec='k')

geo.savefig(plt)