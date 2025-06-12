import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-100,150), ylim=(-100,100))

pL = geo.get_standard_triangle()
A,B,C = pL

D = geo.get_point_by_fractional_length([C,A],1.5)
E = geo.get_point_by_fractional_length([C,B],1.5)

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C],fc='r')

geo.draw_line_segments(ax,[[A,D],[B,E],[D,E]],ec='b')
geo.fill_polygon(ax,[A,D,E,B],fc='b')


a = geo.get_point_by_fractional_length([A,C],0.5)
b = geo.get_point_by_fractional_length([B,C],0.5)
c = geo.get_point_by_fractional_length([A,B],0.5)
d = geo.get_point_by_fractional_length([A,D],0.5)
e = geo.get_point_by_fractional_length([B,E],0.5)
f = geo.get_point_by_fractional_length([D,E],0.5)

points = [
          ['a',a,'N',0],
          ['b',b,'N',0],
          ['c',c,'N',0],
          ['d',d,'N',0],
          ['e',e,'N',0],
          ["c+c'",f,'N',0],
          ]

#geo.label_points(points)


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/similarity.png'
plt.savefig(ofn, dpi=300)