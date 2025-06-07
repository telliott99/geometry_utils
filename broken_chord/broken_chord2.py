import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import broken_chord as bc

ofn = '/Users/telliott/Desktop/broken_chord2.png'

fig,ax,fD = bc.setup()

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']

geo.write_labels([(E,'E',1,1) ])
geo.draw_line_segment(ax,[M,E],ec='r')

# ----------------------------------------

ax.set(xlim=(-60,120), ylim=(0,120))

d = geo.get_length([A,D])
Z = geo.Point(D.x-d,D.y)

geo.write_labels([(Z,'Z',-5,1) ])

geo.draw_line_segment(ax,[M,B],ec='r')
geo.draw_line_segment(ax,[Z,B],ec='r')
geo.draw_line_segment(ax,[A,M],ec='r')
geo.draw_line_segment(ax,[M,Z],ec='r')
geo.draw_line_segment(ax,[G,Z],ec='r')
geo.draw_line_segment(ax,[G,M],ec='r')
geo.draw_line_segment(ax,[B,G],ec='r')

#geo.scatter_points(ax,[M,A,B,E,D,G],s=8)
geo.scatter_points(ax,[M,A,B,D,G],s=8)

# vertices taken CCW, the angle here is at vertex B
dot1 = geo.mark_angle([M,Z,D],d=12)
dot2 = geo.mark_angle([D,A,M],d=12)
dot3 = geo.mark_angle([B,G,M],d=12)
geo.scatter_points(ax,[dot1,dot2,dot3],c='b',s=20)

# ----

# rescatter to make them clean
geo.scatter_points(ax,[M,A,B,E,D,G,Z],s=8)

plt.gca().set_axis_off()
plt.savefig(ofn, dpi=300)





