import path
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

d = geo.get_length([M,A])
circle = plt.Circle(
    (M.x,M.y),d,fc='none',ec='k')
ax.add_patch(circle)

Z = geo.get_point_by_fractional_length([A,D],2.0)
geo.draw_line_segments(ax,
    [[B,Z],[Z,G],[M,G],[M,A]],ec='r')
     
geo.label_points([('Z',Z,'NE',2)])

aL = [[B,G,M],[B,A,M],[M,Z,D]]
geo.mark_angles(ax,aL,c='r',d=10)

geo.draw_line_segments(ax,
    [[M,Z]],ec='r',ls=':')

aL = [[A,M,G],[A,B,G]]
geo.mark_angles(ax,aL,c='b',d=5)


geo.scatter_points(ax,[Z,M,G])

# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/broken_chord7.png'
plt.savefig(ofn, dpi=300)





