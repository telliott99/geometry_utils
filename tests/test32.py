import geometry as geo
import matplotlib.pyplot as plt

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(30,10)
B = geo.Point(60,10)

_,_,C,D = geo.get_pgram_for_angle_length_base(70,15,[A,B])
geo.opg(ax,[A,B,C,D])

theta = 40

tmp = geo.get_point_at_angle_length_for_point(theta,10,D)
E = geo.xll([A,B],[D,tmp])
F = geo.xll([B,C],[D,tmp])

G = geo.get_pgram_point_for_point_diagonal(B,[E,F])
geo.opg(ax,[E,B,F,G],ec='k')

# fill in the rest

H = geo.xll([A,D],[F,G])
I = geo.xll([C,D],[E,G])
geo.dlss(ax,[[D,H],[D,I]])
geo.dls(ax,[E,F],ec='b')


geo.savefig(plt)
