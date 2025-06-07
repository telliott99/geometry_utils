import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()            
A,B,C = geo.get_standard_triangle(mode="isosceles")
geo.scatter_points(ax,[A,B,C],c='purple')

# circle on Q, with radius r
Q = geo.Point(30,55)
r = 25

circle = plt.Circle((Q.x,Q.y), r, 
    facecolor='none',
    edgecolor='purple')
ax.add_patch(circle)

# one line segment, AC, does cross so:
m,k = geo.get_slope_intercept_for_two_points([A,C])
pL = geo.get_intersection_slope_intercept_circle(m,k,[Q,r])

m2,k2 = geo.get_slope_intercept_for_two_points([B,C])
pL2 = geo.get_intersection_slope_intercept_circle(m2,k2,[Q,r])
#print(pL2)
# []

geo.draw_line_segment(ax,[pL[0],pL[1]])
geo.scatter_points(ax,pL,c='red')

ofn = '/Users/telliott/Desktop/example5.png'
plt.savefig(ofn, dpi=300)





