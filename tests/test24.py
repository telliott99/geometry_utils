import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,200), ylim=(0,100))

pL = geo.get_standard_triangle()
A,B,C = pL

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

D,E,F = geo.scale_triangle(pL,f=0.25)
D,E,F = geo.translate_points([D,E,F],dx=60,dy=0)

geo.outline_polygon(ax,[D,E,F],ec='b')
geo.fill_polygon(ax,[D,E,F],fc='b',alpha=0.15)


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/test24.png'
plt.savefig(ofn, dpi=300)