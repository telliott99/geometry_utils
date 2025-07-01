import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

ofn = '/Users/telliott/Desktop/example12.png'

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

# start proof 1

geo.draw_line_segment(ax,[M,B],ec='r')
geo.draw_line_segment(ax,[M,E],ec='r')

cL = [Q,r]
d = geo.get_length([M,B])

pL = geo.get_chord_for_point_on_circle_with_length(
    cL,M,d)
H = pL[1]

geo.draw_line_segment(ax,[M,pL[0]],ec='r')
geo.draw_line_segment(ax,[A,pL[0]],ec='r')
geo.draw_line_segment(ax,[A,M],ec='r',ls=':')

geo.scatter_points(ax,[H,M,A,B,D,E,G],s=8)

geo.write_labels([(A,'A',2,1),
                  (B,'B',-5,1),
                  (G,'G',1,0),
                  (D,'D',1,1),
                  (E,'E',1,1),
                  (H,'H',1,1),
                  (M,'M',-3,3) ])
    
dot1 = geo.mark_angle([M,A,H],d=10)
dot2 = geo.mark_angle([E,A,M],d=10)
geo.scatter_points(ax,[dot1,dot2],c='r')

plt.savefig(ofn, dpi=300)





