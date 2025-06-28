#import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

ofn = '/Users/telliott/Desktop/broken_chord4.png'

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
geo.draw_line_segment(ax,[B,M],ec='r')
geo.draw_line_segment(ax,[D,M])
geo.draw_line_segment(ax,[E,M],ec='r')
geo.draw_line_segment(ax,[G,B])

circle = plt.Circle(Q,r,fc='none',ec='k')
ax.add_patch(circle)

# ----------------------------------------

pL = geo.get_intersection_line_segment_circle([M,E],[Q,r])
# second one is M, or very close
# print(M,pL)
Z = pL[0]
geo.scatter_points(ax,[Z],s=8)

geo.draw_line_segment(ax,[M,Z],ec='r')
geo.draw_line_segment(ax,[A,Z],ec='r')
geo.draw_line_segment(ax,[G,Z],ec='r')

geo.write_labels([(A,'A',2,1),
                  (B,'B',-5,1),
                  (G,'G',-7,-5),
                  (D,'D',1,1),
                  (E,'E',2,1),
                  (Z,'Z',2,-5),
                  (M,'M',-3,3) ])

geo.scatter_points(ax,[M,A,B,E,D,G,Z],s=8)

# vertices taken CCW, the angle here is at vertex B
dot1 = geo.mark_angle([M,B,D],d=5)
dot2 = geo.mark_angle([D,E,M],d=5)
dot3 = geo.mark_angle([E,Z,A],d=5)
dot4 = geo.mark_angle([G,Z,E],d=5)
geo.scatter_points(ax,[dot1,dot2,dot3,dot4],c='b',s=20)

dot5 = geo.mark_angle([E,M,B],d=5)
dot6 = geo.mark_angle([Z,A,E],d=5)
geo.scatter_points(ax,[dot5,dot6],c='r',s=20)


plt.gca().set_axis_off()
plt.savefig(ofn, dpi=300)





