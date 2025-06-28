import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import broken_chord as bc

fig,ax,fD = bc.setup()
ax.set(xlim=(-50,120), ylim=(0,120))

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']


# "erasing" E
geo.scatter_points(ax,[E],c='white',s=12)
geo.draw_line_segment(ax,[B,A])

# ----------------------------------------

Z = geo.get_perp_on_line_for_point(
    [G,B],M)

geo.draw_line_segments(ax,[[M,Z],[M,B],[B,Z]],ec='r')

geo.label_points([('Z',Z,'NW',2)])

aL = [[Z,B,M],[M,B,D]]
geo.mark_angles(ax,aL,c='r',d=6)

geo.draw_line_segments(ax,[[M,A],[M,G]],ec='r',ls=':')

geo.fill_polygon(ax,[G,M,Z])

geo.scatter_points(ax,[Z])
 
# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/broken_chord8.png'
plt.savefig(ofn, dpi=300)





