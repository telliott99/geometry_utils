import matplotlib.pyplot as plt
import math, random
import numpy as np
import geometry as geo

ofn = '/Users/telliott/Desktop/example8.png'
fig, ax = geo.init()
ax.set(xlim=(-25, 140), ylim=(-25, 150))
    
# starting from a center point Q
# normalize points to Q
# rotate by theta
# add Q back again

theta = 90

A,B,C = geo.get_standard_triangle(mode="obtuse")
[Q,r] = geo.get_circumcircle([A,B,C])

circle = plt.Circle((Q.x,Q.y), r, 
    facecolor='none',
    edgecolor='purple')
ax.add_patch(circle)

# angle in radians
[D,E,F] = geo.rotate_points_around_center_by_angle(
        [A,B,C],Q,theta)
        
[X,Y,Z] = geo.rotate_points_around_center_by_angle(
        [A,B,C],Q,180)

geo.fill_polygon(ax,[A,B,C],alpha=0.35)
geo.outline_polygon(ax,[A,B,C])
geo.scatter_points(ax,[A,B,C],c='red')

geo.fill_polygon(ax,[D,E,F],fc='b',alpha=0.1)
geo.outline_polygon(ax,[D,E,F])
geo.scatter_points(ax,[D,E,F],c='b')

geo.fill_polygon(ax,[X,Y,Z],fc='k',alpha=0.1)
geo.outline_polygon(ax,[X,Y,Z])
geo.scatter_points(ax,[X,Y,Z],c='k')

geo.scatter_points(ax,[Q],'purple')

plt.savefig(ofn, dpi=300)