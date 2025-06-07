import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import broken_chord as bc

fig,ax,fD = bc.setup()

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']

# we remove E to rename it as Z

# ----

d = geo.get_length([G,B])
Z = geo.Point(A.x-d,A.y)

geo.write_labels([(Z,'Z',1,1) ])

                  
geo.draw_line_segment(ax,[M,E],ec='r')
geo.draw_line_segment(ax,[M,B],ec='r')
geo.draw_line_segment(ax,[A,M],ec='r')
geo.draw_line_segment(ax,[G,M],ec='r')
geo.draw_line_segment(ax,[B,G],ec='r')
geo.draw_line_segment(ax,[M,Z],ec='r')

geo.scatter_points(ax,[M,A,B,E,D,G],s=8)

# vertices taken CCW, the angle here is at vertex B
dot1 = geo.mark_angle([D,A,M],d=10)
dot2 = geo.mark_angle([B,G,M],d=10)
geo.scatter_points(ax,[dot1,dot2],c='b',s=20)

# ----

# rescatter to make them clean
geo.scatter_points(ax,[M,A,B,E,D,G],s=8)

plt.gca().set_axis_off()

ofn = '/Users/telliott/Desktop/broken_chord3.png'
plt.savefig(ofn, dpi=300)





