import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
                   
# circle on center 3,3 with radius 3
r1 = 30
x1,y1 = (30,30)
Q1 = geo.Point(x1,y1)
c1 = [Q1,r1]

# circle on center 6,3 with radius 2
r2 = 30
x2,y2 = (60,70)
Q2 = geo.Point(x2,y2)
c2 = [Q2,r2]

circle1 = plt.Circle([Q1.x,Q1.y],r1,fc='none',ec='k')
circle2 = plt.Circle([Q2.x,Q2.y],r2,fc='none',ec='k')

ax.add_patch(circle1)
ax.add_patch(circle2)

# connect the centers
geo.draw_line_segment(ax,[Q1,Q2],ec='r')
geo.scatter_points(ax,[Q1,Q2])

# ------------------------------------------

# exercise new functions from geo

pL = geo.get_intersection_circle_circle(c1,c2)
geo.draw_line_segment(ax,pL,'r')
geo.scatter_points(ax,pL,c='red')

# ax needed b/c we construct circle in the callee
# not any more!

T1,T2 = geo.get_tangent_points_on_circle_for_point(c2,Q1)

geo.draw_line_segment(ax,[Q1,T1],ec='b')
geo.draw_line_segment(ax,[Q1,T2],ec='b')
geo.scatter_points(ax,[T1,T2],c='blue')

ofn = '/Users/telliott/Desktop/example6.png'
plt.savefig(ofn, dpi=300)





