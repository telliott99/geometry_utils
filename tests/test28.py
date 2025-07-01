import sys,math
import geometry as geo
from geometry import np, plt

fig, ax = geo.init()

A = geo.Point(20,20)
B = geo.Point(50,20)

rL = geo.get_parallelogram([A,B],45,aspect_ratio=0.6,phi=30)
A,B,C,D = rL
geo.opg(ax,rL)

geo.label_points(
    [['A',A,'NW',2],
     ['B',B,'NE',2],
     ['C',C,'S',3],
     ['D',D,'SW',5],
     ])

geo.scp(ax,[A,B,C,D],s=6)

geo.savefig(plt)



