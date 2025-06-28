import sys,math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

pL = geo.get_standard_triangle()
A,B,C = list(pL)
geo.outline_polygon(ax,pL)
geo.fill_polygon(ax,pL)

oD = geo.get_orthocenter_and_altitudes(pL)
D,E,F,H = oD['D'],oD['E'],oD['F'],oD['H']
geo.draw_line_segments(ax,[[A,D],[C,F]],ec='b',ls=':')

box = geo.mark_right_angle(D,[A,C])
geo.outline_polygon(ax,box,ec='k')
box = geo.mark_right_angle(F,[B,C])
geo.outline_polygon(ax,box,ec='k')

geo.fill_polygon(ax,[A,F,H],fc='b',alpha=0.15)
geo.fill_polygon(ax,[C,D,H],fc='b',alpha=0.15)

geo.label_points(
    [['A',A,'W',4],
     ['B',B,'E',1],
     ['C',C,'N',1],
     ['D',D,'E',1],
     ['F',F,'S',4],
     ['H',H,'SE',2],
     ])
    
aL = [[D,A,B],[D,C,F]]
geo.mark_angles(ax,aL,d=6,c='k')

#----------

geo.scatter_points(ax,[A,B,C,H],s=3)

geo.savefig(plt)


