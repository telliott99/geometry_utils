import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-30,120), ylim=(-30,120))

pL = geo.get_cyclic_quadrilateral()
A,B,K,C = pL

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

Q,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

aD = geo.get_orthocenter_and_altitudes([A,B,C])
D = aD['D']
    
geo.draw_line_segments(ax,[[A,K],[B,K],[C,K]])

# find the vertical from D to another side
M = geo.get_point_perp_on_line_for_point(D,[A,B])
N = geo.get_intersection_for_two_lines(
    [D,M],[C,K])
    
geo.draw_line_segments(ax,[[A,D],[M,N]])

geo.fill_polygon(ax,[D,N,K],fc='b',alpha=0.1)

geo.scatter_points(ax,[A,B,C,K,N])



points = [
          ['A',A,'W',6],
          ['B',B,'E',2],
          ['C',C,'NW',3],
          ['D',D,'W',8],
          ['M',M,'NE',2],
          ['N',N,'N',2],
          ['K',K,'E',3],
         ]

geo.label_points(points)

box = geo.mark_right_angle(D,[A,C])
geo.outline_polygon(ax,box,ec='k')

box = geo.mark_right_angle(M,[A,N])
geo.outline_polygon(ax,box,ec='k')


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/brahmagupta.png'
plt.savefig(ofn, dpi=300)