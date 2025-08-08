import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

pL = geo.gtr()
A,B,C = pL
geo.opg(ax,pL)

P = geo.Point(44,38)


D = geo.xll([B,C],[A,P])
E = geo.xll([A,C],[B,P])
F = geo.xll([A,B],[C,P])
geo.dlss(ax,[[A,D],[B,E],[C,F]])

geo.savefig(plt)

