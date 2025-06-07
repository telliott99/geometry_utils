import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

ofn = '/Users/telliott/Desktop/broken_chord2.png'

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
                  
d = geo.get_length([A,D])
Z = [D[0]-d,D[1]]

geo.write_labels([(A,'A',2,1),
                  (B,'B',-5,1),
                  (G,'G',1,0),
                  (D,'D',1,1),
                  (Z,'Z',-5,1),
                  (M,'M',-3,3) ])

geo.draw_line_segment(ax,[M,B],ec='r')
geo.draw_line_segment(ax,[Z,B],ec='r')
geo.draw_line_segment(ax,[A,M],ec='r')
geo.draw_line_segment(ax,[M,Z],ec='r')
geo.draw_line_segment(ax,[G,Z],ec='r',ls=':')
geo.draw_line_segment(ax,[G,M],ec='r',ls=':')
geo.draw_line_segment(ax,[B,G],ec='r',ls=':')

#geo.scatter_points(ax,[M,A,B,E,D,G],s=8)
geo.scatter_points(ax,[M,A,B,D,G],s=8)

# vertices taken CCW, the angle here is at vertex B
dot1 = geo.mark_angle([M,Z,D],d=10)
dot2 = geo.mark_angle([D,A,M],d=10)
dot3 = geo.mark_angle([B,G,M],d=10)
geo.scatter_points(ax,[dot1,dot2,dot3],c='b',s=20)

'''
dot3 = geo.mark_angle([M,B,D],d=5)
dot4 = geo.mark_angle([D,E,M],d=5)
geo.scatter_points(ax,[dot3,dot4],c='b',s=20)

dot5 = geo.mark_angle([A,M,E],d=10)
dot6 = geo.mark_angle([H,M,A],d=10)
geo.scatter_points(ax,[dot5,dot6],c='purple',s=20)

'''

plt.gca().set_axis_off()
plt.savefig(ofn, dpi=300)





