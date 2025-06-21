import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))


pL = geo.get_standard_triangle()
A,B,C = pL

A,B,C = geo.scale_triangle([A,B,C],0.6)

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

d = geo.get_length([A,C])
f = d/(geo.get_length([B,C]))

D = geo.get_point_by_fractional_length(
    [C,B],f)

geo.fill_polygon(ax,[A,B,D],fc='b',alpha=0.15)

geo.draw_line_segment(ax,[A,D],ec='b')


'''
points = [
          ['A',A,'W',6],
          ['B',B,'E',3],
          ['C',C,'N',2],
         ]

geo.label_points(points)
'''

geo.scatter_points(ax,[A,B,C,D])

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/EI_18.png'
plt.savefig(ofn, dpi=300)