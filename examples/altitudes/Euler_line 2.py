import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(-10,100))

pL = geo.get_standard_triangle()
A,B,C = pL
C = geo.nudge(C,'S',20)

geo.fill_polygon(ax,[A,B,C])
geo.outline_polygon(ax,[A,B,C])

oD = geo.get_orthocenter_and_altitudes([A,B,C])
O,r = geo.get_circumcircle([A,B,C])
mD = geo.get_centroid_and_medians([A,B,C])

D = oD['D']
F = oD['F']
H = oD['H']

G = mD['G']
K = mD['K']
M = mD['M']

geo.draw_line_segments(
    ax,[[A,D],[A,K],[C,F],[C,M],[O,K],[O,M]],ls=':')

geo.draw_line_segments(
    ax,[[O,H]])

geo.fill_polygon(ax,[C,H,G],'b',alpha=0.15)
geo.fill_polygon(ax,[M,O,G],'b',alpha=0.15)

geo.fill_polygon(ax,[A,B,C])

geo.scatter_points(ax,[A,B,C,D,F,H,G,K,M,O],s=6)

points = [
          ['A',A,'SW',5],
          ['B',B,'S',4],
          ['C',C,'N',2],
          ['D',D,'N',2],
          ['F',F,'S',4],
          ['H',H,'E',2],
          ['G',G,'N',3],
          ['K',K,'E',2],
          ['M',M,'S',4],
          ['O',O,'SE',3],
         ]

geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/Euler_line.png'
plt.savefig(ofn, dpi=300)