import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-50,100), ylim=(-10,100))

pL = geo.get_standard_triangle(mode='obtuse')
A,B,C = pL
B = geo.nudge(B,'W',25)
A = geo.nudge(A,'N',15)
D = geo.Point(80,60)

K = geo.get_point_by_fractional_length([A,B],0.5)
L = geo.get_point_by_fractional_length([B,D],0.5)
M = geo.get_point_by_fractional_length([C,D],0.5)
N = geo.get_point_by_fractional_length([A,C],0.5)

geo.outline_polygon(ax,[A,B,D,C],ec='k')
geo.fill_polygon(ax,[A,B,D,C])
geo.outline_polygon(ax,[K,L,M,N])
geo.fill_polygon(ax,[K,L,M,N])

geo.draw_line_segment(ax,[A,D],ec='b')
geo.draw_line_segment(ax,[B,C],ec='g')

geo.scatter_points(ax,[A,B,C,D,K,L,M,N],s=8)


points = [
          ['A',A,'SW',6],
          ['B',B,'N',2],
          ['C',C,'E',1],
          ['D',D,'N',2],
          ['K',K,'SW',6],
          ['L',L,'N',2],
          ['M',M,'E',1],
          ['N',N,'SW',6],
        ]

geo.label_points(points)


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/varignon.png'
plt.savefig(ofn, dpi=300)