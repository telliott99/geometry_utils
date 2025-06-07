import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
[A,B,C] = geo.get_standard_triangle()
geo.fill_polygon(ax,[A,B,C])

geo.draw_line_segment(ax,[A,B,C],
    #fc='none',  # needed b/c we reset alpha next
    ec='red', 
    lw=2)

# ----------------------------------------

rD = geo.get_9point_circle([A,B,C])

P = rD['P']
Q = rD['Q']
R = rD['R']
N = rD['N']
    
geo.draw_line_segment(ax,(P,Q),ec='purple',lw=2)
geo.draw_line_segment(ax,(Q,R),ec='purple',lw=2)
geo.draw_line_segment(ax,(P,R),ec='purple',lw=2)

r = geo.get_length([N,P])

circle = plt.Circle((N.x,N.y), r, 
    facecolor='none',
    edgecolor='purple')
ax.add_patch(circle)

geo.scatter_points(ax,[P,Q,R,N],c='purple')

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

geo.draw_line_segment(ax,[X,Y],ec='g',lw=2)
geo.draw_line_segment(ax,[Y,Z],ec='g',lw=2)
geo.draw_line_segment(ax,[X,Z],ec='g',lw=2)

geo.scatter_points(ax,[X,Y,Z],c='g')

geo.scatter_points(ax,[A,B,C],c='black')

ofn = '/Users/telliott/Desktop/example4.png'
plt.savefig(ofn, dpi=300)





