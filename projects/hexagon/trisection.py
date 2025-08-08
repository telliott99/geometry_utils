import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

delta = 40
A = geo.Point(10,20)
B = geo.Point(A.x+delta,A.y)
C = geo.xcc([A,delta],[B,delta])[1]

D = geo.Point(C.x+delta,C.y)
E = geo.Point(B.x+delta,B.y)

geo.opg(ax,[A,C,D,E,B])
geo.fpg(ax,[A,B,C])
geo.fpg(ax,[D,B,E])
geo.dlss(ax,[[B,D],[B,C]],ec='r')

geo.dls(ax,[A,D],ec='k')

X = geo.xll([B,C],[A,D])
Y = geo.xll([E,X],[A,C])
geo.dls(ax,[E,Y],ec='b')

Z = geo.xll([E,Y],[B,D])
geo.fpg(ax,[B,X,Z],fc='b',alpha=0.2)
geo.scp(ax,[Z])

geo.savefig(plt)