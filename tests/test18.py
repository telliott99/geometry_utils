import path

import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-100,200), ylim=(-100,200))

A = geo.Point(0,0)
B = geo.Point(20,80)
geo.draw_line_segments(ax,[[A,B]])
geo.scatter_points(ax,[A,B])

S,T = geo.get_perp_at_point_by_fractional_length(
    [A,B],f=1.2)
geo.draw_line_segments(ax,[[S,T]])
geo.scatter_points(ax,[S,T],c='b')
geo.draw_line_segments(ax,[[S,T]],ls=':',ec='b')

S,T = geo.get_perp_at_point_by_fractional_length(
    [A,B],f=0.2)
geo.draw_line_segments(ax,[[S,T]])
geo.scatter_points(ax,[S,T],c='r')
geo.draw_line_segments(ax,[[S,T]],ls=':',ec='r')

S,T = geo.get_perp_at_point_by_fractional_length(
    [A,B],f=0.5)
geo.draw_line_segments(ax,[[S,T]])
geo.scatter_points(ax,[S,T],c='g')
geo.draw_line_segments(ax,[[S,T]],ls=':',ec='g')

geo.scatter_points(ax,[A,B])


plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/example18.png'
plt.savefig(ofn, dpi=300)





