import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

delta = 50
A = geo.Point(10,20)
B = geo.Point(A.x+delta,A.y)
D = geo.xcc([A,delta],[B,delta])[1]


C = geo.get_diagonal_for_point_diagonal(
        A,[B,D])

geo.opg(ax,[A,B,C,C])
geo.fpg(ax,[A,B,C],alpha=0.3)
geo.dlss(ax,[[A,D],[B,D],[C,D]])


geo.savefig(plt)