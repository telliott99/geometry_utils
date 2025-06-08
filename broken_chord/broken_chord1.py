import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import broken_chord as bc

ofn = '/Users/telliott/Desktop/broken_chord1.png'

fig,ax,fD = bc.setup()

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']

geo.write_labels([(E,'E',1,1) ])
geo.draw_line_segment(ax,[M,B],ec='r')
geo.draw_line_segment(ax,[M,E],ec='r')

# ----

d = geo.get_length([M,B])
pL = geo.get_chord_for_point_on_circle_with_length(ax,[Q,r],M,d)
H = pL[1]
geo.write_labels([(H,'H',1,1) ])

geo.draw_line_segments(
    ax,[[M,H],[A,H],[A,M]],ec='r')

# vertices taken CCW, the angle here is at vertex B
geo.mark_angles(ax,[[M,A,H],[E,A,M]],d=12,c='r',s=20)
geo.mark_angles(ax,[[M,B,D],[D,E,M]],d=5,c='b',s=20)
geo.mark_angles(ax,[[A,M,E],[H,M,A]],d=10,c='g',s=20)

# rescatter to make them clean
geo.scatter_points(ax,[M,A,B,E,D,G,H],s=8)

plt.gca().set_axis_off()
plt.savefig(ofn, dpi=300)





