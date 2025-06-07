import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
[A,B,C] = geo.get_standard_triangle()
geo.fill_polygon(ax,[A,B,C])

geo.outline_polygon(ax,[A,B,C],ec='k')

# ----------------------------------------

rD = geo.get_9point_circle([A,B,C])

P = rD['P']
Q = rD['Q']
R = rD['R']
N = rD['N']
    
geo.draw_line_segments(ax,[[P,Q],[Q,R],[P,R]],ec='r')

r = geo.get_length([N,P])

circle = plt.Circle((N.x,N.y), r, 
    facecolor='none',
    edgecolor='r')
ax.add_patch(circle)

# ----------------------------------------

# we want to rotate the points P,Q,R about center N
# since it's 180 deg, we do not solve the general problem
# get dx,dy from point P to N
# add twice that to P to reflect P' in N

dx,dy = geo.get_deltas([P,N])
X = geo.Point(P.x+2*dx,P.y+2*dy)
dx,dy = geo.get_deltas([Q,N])
Y = geo.Point(Q.x+2*dx,Q.y+2*dy)
dx,dy = geo.get_deltas([R,N])
Z = geo.Point(R.x+2*dx,R.y+2*dy)

geo.draw_line_segments(ax,[[X,Y],[Y,Z],[X,Z]],ec='m')

# let's include the altitudes
oD = geo.get_orthocenter_and_altitudes([A,B,C])

D = oD['D']
E = oD['E']
F = oD['F']

geo.draw_line_segments(
    ax,[[A,D],[B,E],[C,F]],ec='b',ls=':')


geo.scatter_points(ax,[P,R,N],c='r')
geo.scatter_points(ax,[Q],c='r')
geo.scatter_points(ax,[X,Y,Z],c='m')
geo.scatter_points(ax,[D,E,F],c='b')
geo.scatter_points(ax,[A,B,C],c='black')

points = [
          ['A',A,'SW',6],
          ['B',B,'S',4],
          ['C',C,'NE',2],
         ]

geo.label_points(points)


plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ninepoint.png'
plt.savefig(ofn, dpi=300)





