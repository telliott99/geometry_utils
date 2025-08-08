import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,150), ylim=(0,100))


pL = geo.gtr()
A,B,C = pL

geo.opg(ax,[A,B,C])

D = geo.gpf([A,C],0.7)
E = geo.gpf([B,C],0.4)
F = geo.xll([A,B],[D,E])

X = geo.get_perp_on_line_for_point([E,F],A)
Y = geo.get_perp_on_line_for_point([E,F],B)
Z = geo.get_perp_on_line_for_point([E,F],C)


geo.dls(ax,[B,F])

t = (0,(1,4))
geo.dls(ax,[A,X],ls=t)
geo.dls(ax,[B,Y],ls=t)
geo.dls(ax,[C,Z],ls=t)
geo.dls(ax,[Z,F],ec='b')

geo.scp(ax,[X,Y,Z])



geo.savefig(plt)

