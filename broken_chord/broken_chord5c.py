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

# just like 5b except we fool with point B
tmp = geo.rotate_points_around_center_by_angle(
    [B],Q,math.radians(37))
#print(B,tmp)
B = tmp[0]

# must also recalculate D and E
D = geo.get_perp_on_line_for_point([A,B],M)
E = geo.get_point_by_fractional_length([B,D],2.0)

# -----

geo.draw_line_segments(ax,[[A,B],[D,M],[G,B]])

circle = plt.Circle((Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

geo.draw_line_segment(ax,[M,B],ec='r')
geo.draw_line_segment(ax,[M,E],ec='r')

#geo.draw_multiple_line_segments(ax,[[[M,B],[M,E]]],ec='r')

geo.scatter_points(ax,[M,A,G,B,D,E],s=8)

pL = geo.get_intersection_line_segment_circle([M,E],[Q,r])
# second one is M, or very close
# print(M,pL)
Z = pL[1]
geo.scatter_points(ax,[Z],s=8)

geo.draw_line_segments(ax,[[M,Z],[A,Z],[G,Z],[A,M]],ec='r')

geo.write_labels([(A,'A',2,-4),
                  (B,'B',-6,1),
                  (G,'G',-6,-6),
                  (D,'D',3,0),
                  (E,'E',3,-1),
                  #(Z,'Z',-7,1),
                  (M,'M',-3,3) ])

aL = [[M,B,D],[A,E,G],[M,Z,A],[G,A,M],[B,E,M]]
geo.mark_angles(ax,aL,c='b',d=4)

aL = [[E,M,B],[A,M,G],[A,B,G]]
geo.mark_angles(ax,aL,d=8,c='r')

geo.scatter_points(ax,[M,A,G,B,D,E],s=8)

ofn = '/Users/telliott/Desktop/broken_chord5c.png'
plt.gca().set_axis_off()
plt.savefig(ofn, dpi=300)

