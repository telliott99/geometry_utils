import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,110), ylim=(-10,100))

A = geo.Point(10,40)
B = geo.Point(90,40)
_,_,C,D = geo.get_rectangle_for_line([A,B],f=4/7)

P = geo.gpf([D,C],3/7)
Q = geo.gpf([B,C],1/4)

geo.opg(ax,[A,B,C,D])

geo.fpg(ax,[A,D,P])
geo.opg(ax,[A,D,P])

geo.fpg(ax,[P,Q,C])
geo.opg(ax,[P,Q,C])

geo.fpg(ax,[A,B,Q],fc='b',alpha=0.2)
geo.opg(ax,[A,B,Q],ec='b')

geo.savefig(plt)

