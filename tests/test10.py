import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

ofn = '/Users/telliott/Desktop/example10.png'

# an early draft for the broken chord stuff

fig, ax = geo.init()
ax.set(xlim=(0,120), ylim=(0,120))
fD = geo.get_broken_chord_layout(ax)

# ----------------------------------------

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']

geo.draw_line_segment(ax,[A,B])
geo.draw_line_segment(ax,[A,M])
geo.draw_line_segment(ax,[D,M])

circle = plt.Circle((Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

# ----------------------------------------

geo.draw_line_segment(ax,[M,B],ec='r')
geo.draw_line_segment(ax,[M,E],ec='r')

plt.savefig(ofn, dpi=300)





