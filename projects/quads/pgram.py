import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))


A = geo.Point(10,20)
B = geo.Point(60,20)

_,_,C,D = geo.get_pgram_for_angle_length_base(
    60,40,[A,B])

M = geo.get_midpoint([A,C]) 

geo.opg(ax,[A,B,C,D])

geo.opg(ax,[A,D,M])
geo.fpg(ax,[A,D,M])
geo.opg(ax,[B,C,M])
geo.fpg(ax,[B,C,M])

geo.opg(ax,[A,B,M],ec='b')
geo.fpg(ax,[A,B,M],fc='b',alpha=0.2)
geo.opg(ax,[C,D,M],ec='b')
geo.fpg(ax,[C,D,M],fc='b',alpha=0.2)


geo.savefig(plt)





