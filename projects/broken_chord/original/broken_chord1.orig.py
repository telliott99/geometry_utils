import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

ofn = '/Users/telliott/Desktop/broken_chord1.png'

fig, ax = geo.init()
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
geo.draw_line_segment(ax,[G,B])

circle = plt.Circle(Q,r,fc='none',ec='k')
ax.add_patch(circle)

# ----------------------------------------

geo.draw_line_segment(ax,[M,B],ec='r')
#geo.draw_line_segment(ax,[M,D],ec='r')
geo.draw_line_segment(ax,[M,E],ec='r')

d = geo.get_length([M,B])

pL = geo.get_chord_for_circle_from_point_with_length(ax,[Q,r],M,d)
H = pL[0]

#print(d - geo.get_length([H,M]))
#print(d - geo.get_length([B,M]))

geo.draw_line_segment(ax,[M,pL[0]],ec='r')
geo.draw_line_segment(ax,[A,pL[0]],ec='r')
geo.draw_line_segment(ax,[A,M],ec='r',ls=':')

geo.scatter_points(ax,[M,A,B,E,D,G],s=8)

geo.write_labels([(A,'A',2,1),
                  (B,'B',-5,1),
                  (G,'G',1,0),
                  (D,'D',1,1),
                  (E,'E',1,1),
                  (H,'H',1,1),
                  (M,'M',-3,3) ])

# vertices taken CCW, the angle here is at vertex B
dot1 = geo.mark_angle([M,A,H],d=10)
dot2 = geo.mark_angle([E,A,M],d=10)
geo.scatter_points(ax,[dot1,dot2],c='r',s=20)

dot3 = geo.mark_angle([M,B,D],d=5)
dot4 = geo.mark_angle([D,E,M],d=5)
geo.scatter_points(ax,[dot3,dot4],c='b',s=20)

dot5 = geo.mark_angle([A,M,E],d=10)
dot6 = geo.mark_angle([H,M,A],d=10)
geo.scatter_points(ax,[dot5,dot6],c='purple',s=20)

plt.gca().set_axis_off()
plt.savefig(ofn, dpi=300)





