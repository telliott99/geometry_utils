import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import broken_chord as bc

# note proof 4 re-uses a diagram
# hence there is no bc4.png

fig,ax,fD = bc.setup()

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']

geo.write_labels([(E,'E',1,1) ])
geo.draw_line_segment(ax,[M,E],ec='r')

# ----------------------------------------

pL = geo.get_intersection_line_segment_circle([M,E],[Q,r])
# second one is M, or very close
# print(M,pL)
Z = pL[0]
geo.scatter_points(ax,[Z],s=8)

geo.draw_line_segment(ax,[M,Z],ec='r')
geo.draw_line_segment(ax,[A,Z],ec='r')
geo.draw_line_segment(ax,[G,Z],ec='r')

geo.write_labels([(Z,'Z',2,-5) ])

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

# ----

# rescatter to make them clean
geo.scatter_points(ax,[M,A,B,E,D,G,Z],s=8)

plt.gca().set_axis_off()

ofn = '/Users/telliott/Desktop/broken_chord5.png'
plt.savefig(ofn, dpi=300)





