import matplotlib.pyplot as plt
import numpy as np
import geometry as geo


fig, ax = geo.init()
                   
[A,B,C] = geo.get_standard_triangle("obtuse")
geo.outline_polygon(ax,[A,B,C],ec='lightsalmon')
geo.draw_line_segment(ax,[A,B,C])

# ----------------------------------------

rD = geo.get_incenter_and_bisectors([A,B,C])

P = rD['P']
Q = rD['Q']
R = rD['R']
I = rD['I']

# note: redefinition of X and Y!
X = rD['X']
Y = rD['Y']
Z = rD['Z']
    
geo.draw_line_segment(ax,(I,A),ec='r')
geo.draw_line_segment(ax,(I,B),ec='r')
geo.draw_line_segment(ax,(I,C),ec='r')

geo.draw_line_segment(ax,(I,X))
geo.draw_line_segment(ax,(I,Y))
geo.draw_line_segment(ax,(I,Z))

r = geo.get_length([I,X])

circle = plt.Circle((I.x,I.y), r, 
    fc='none',
    ec='purple')
ax.add_patch(circle)

geo.scatter_points(ax,[X,Y,Z,I])
geo.scatter_points(ax,[A,B,C])


ofn = '/Users/telliott/Desktop/example3.png'
plt.savefig(ofn, dpi=300)





