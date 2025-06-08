import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import broken_chord as bc

fig,ax,fD = bc.setup()

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']


# "erasing" E
geo.scatter_points(ax,[E],c='white',s=12)
geo.draw_line_segment(ax,[B,A])

# ----------------------------------------

d = geo.get_length([B,D])
Z = geo.Point(A.x-d,A.y)
tmp = geo.Point(Z.x,Z.y+10)
pL = geo.get_intersection_line_segment_circle([Z,tmp],[Q,r])
H = pL[0]

geo.draw_line_segment(ax,[M,H],ec='r')
geo.draw_line_segment(ax,[H,Z],ec='r')
geo.draw_line_segment(ax,[B,M],ec='r')
geo.draw_line_segment(ax,[H,A],ec='r')

geo.write_labels([(Z,'Z',2,1),
                  (H,'H',-3,3) ])

aL = [[Z,A,H],[M,B,D]]
geo.mark_angles(ax,aL,c='r')

# ----

# rescatter to make them clean
geo.scatter_points(ax,[M,A,B,D,G,Z,H],s=8)

plt.gca().set_axis_off()

ofn = '/Users/telliott/Desktop/broken_chord6.png'
plt.savefig(ofn, dpi=300)





