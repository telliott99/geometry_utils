import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

ofn = '/Users/telliott/Desktop/example2.png'

fig, ax = geo.init()
# expand for circumcircle
ax.set(xlim=(-25, 110), ylim=(-25, 110))

# ----------------------------------------

# an ordered list of points
[A,B,C] = geo.get_standard_triangle()

geo.fill_polygon(ax,[A,B,C])
geo.outline_polygon(ax,[A,B,C])
geo.scatter_points(ax,[A,B,C])

# ----------------------------------------

rD = geo.get_orthocenter_and_altitudes([A,B,C])

D = rD['D']
E = rD['E']
F = rD['F']
H = rD['H']
    
geo.draw_line_segment(ax,[A,D])
geo.draw_line_segment(ax,[B,E])
geo.draw_line_segment(ax,[C,F])

geo.scatter_points(ax,[D,E,F],c='r')

# ----------------------------------------

rD = geo.get_centroid_and_medians([A,B,C])

K = rD['K']
L = rD['L']
M = rD['M']
G = rD['G']


geo.draw_line_segment(ax,(A,K))
geo.draw_line_segment(ax,(B,L))
geo.draw_line_segment(ax,(C,M))

geo.scatter_points(ax,[K,L,M,G],c='b')


# ----------------------------------------

# this works, just kind of busy
# see test_geo3.py

'''

rD = geo.get_incenter_and_bisectors([A,B,C])

P = rD['P']
Q = rD['Q']
R = rD['R']
I = rD['I']

# rD also has perps X,Y,Z

geo.draw_line_segment(ax,(A,P))
geo.draw_line_segment(ax,(B,Q))
geo.draw_line_segment(ax,(C,R))

geo.scatter_points(ax,[P,Q,R,I],c='k')

'''

# ----------------------------------------

Q,r = geo.get_circumcircle([A,B,C])
geo.scatter_points(ax,[Q],c='purple')

circle = plt.Circle((Q.x,Q.y),r, 
    facecolor='none',
    edgecolor='purple')
ax.add_patch(circle)

# to go over circle
geo.scatter_points(ax,[A,B,C])

plt.savefig(ofn, dpi=300)





