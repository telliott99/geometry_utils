import sys,math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-30,120), ylim=(-50,100))

pL = geo.gtr()
pL = geo.scale_triangle(pL,f=0.8)
pL = geo.translate_points(pL,dx=10,dy=10)
A,B,C = pL

geo.opg(ax,[A,B,C])

D,E,F = geo.get_parallelograms_for_triangle(pL)
K = geo.get_point_by_fractional_length([B,C],0.5)

geo.opg(ax,[D,E,F],ec='k')
geo.fpg(ax,[A,B,C],fc='r',alpha=0.3)
geo.dlss(ax,[[A,D]],ec='k',ls=':')

geo.scp(ax,[A,B,C,K],c='k',s=6)
geo.scp(ax,[D,E,F],s=6)


geo.label_points(
    [['A',A,'SW',7],
     ['B',B,'SE',4],
     ['C',C,'N',2],
     ['D',D,'N',2],
     ['E',E,'N',2],
     ['F',F,'E',3],
     ['K',K,'SE',4],
     ])


geo.savefig(plt,ofn='pgrams.png')