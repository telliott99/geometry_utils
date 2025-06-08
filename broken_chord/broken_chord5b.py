import sys, random
import math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,120), ylim=(0,120))

fD = geo.get_broken_chord_alternate_layout(ax)

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']

geo.draw_line_segment(ax,[A,B])
geo.draw_line_segment(ax,[D,M])
geo.draw_line_segment(ax,[G,B])

circle = plt.Circle((Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

geo.draw_line_segment(ax,[M,B],ec='r')
geo.draw_line_segment(ax,[M,E],ec='r')

geo.scatter_points(ax,[M,A,G,B,D,E],s=8)

pL = geo.get_intersection_line_segment_circle([M,E],[Q,r])
# second one is M, or very close
# print(M,pL)
Z = pL[1]
geo.scatter_points(ax,[Z],s=8)

geo.draw_line_segment(ax,[M,Z],ec='r')
geo.draw_line_segment(ax,[A,Z],ec='r')
geo.draw_line_segment(ax,[G,Z],ec='r')
geo.draw_line_segment(ax,[A,M],ec='r')

geo.write_labels([(A,'A',2,-4),
                  (B,'B',-5,1),
                  (G,'G',-6,-6),
                  (D,'D',3,-3),
                  (E,'E',3,-1),
                  (Z,'Z',-7,1),
                  (M,'M',-3,3) ])

dot1 = geo.mark_angle([M,B,D],d=5)
dot2 = geo.mark_angle([A,E,Z],d=5)
dot3 = geo.mark_angle([M,Z,A],d=5)
geo.scatter_points(ax,[dot1,dot2,dot3],c='b',s=20)

dot4 = geo.mark_angle([Z,A,E],d=8)
dot5 = geo.mark_angle([E,M,B],d=8)
dot6 = geo.mark_angle([Z,G,B],d=8)
dot7 = geo.mark_angle([A,B,G],d=8)
geo.scatter_points(ax,[dot4,dot5,dot6,dot7],c='r',s=20)


ofn = '/Users/telliott/Desktop/broken_chord5b.png'
plt.gca().set_axis_off()
plt.savefig(ofn, dpi=300)

