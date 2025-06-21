import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

ofn = '/Users/telliott/Desktop/broken_chord3.png'

fig, ax = geo.init()
fig, ax = geo.init()
ax.set(xlim=(-60,120), ylim=(0,120))
fD = geo.get_broken_chord_layout(ax)

# ----------------------------------------

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']

geo.draw_line_segment(ax,[A,B])
geo.draw_line_segment(ax,[A,M])
geo.draw_line_segment(ax,[D,M])
geo.draw_line_segment(ax,[G,B])

circle = plt.Circle(Q,r,fc='none',ec='k')
ax.add_patch(circle)

# ----------------------------------------



d = geo.get_length([G,B])
Z = [A[0] - d,A[1]]
                  
geo.write_labels([(A,'A',2,1),
                  (B,'B',-5,1),
                  (G,'G',1,0),
                  (D,'D',1,1),
                  (Z,'Z',2,1),
                  (M,'M',-3,3) ])

geo.draw_line_segment(ax,[M,B],ec='r')
geo.draw_line_segment(ax,[A,M],ec='r')
geo.draw_line_segment(ax,[G,M],ec='r',ls=':')
geo.draw_line_segment(ax,[B,G],ec='r',ls=':')
geo.draw_line_segment(ax,[M,Z],ec='r',ls=':')

geo.scatter_points(ax,[M,A,B,E,D,G],s=8)

# vertices taken CCW, the angle here is at vertex B
dot1 = geo.mark_angle([D,A,M],d=10)
dot2 = geo.mark_angle([B,G,M],d=10)
geo.scatter_points(ax,[dot1,dot2],c='b',s=20)


plt.gca().set_axis_off()
plt.savefig(ofn, dpi=300)





