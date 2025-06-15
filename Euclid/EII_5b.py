import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(-0.7,100))


Q = geo.Point(50,0)
r = 40

# google shows how to independently set alpha for fc and ec
from matplotlib import colors
facecolor = colors.to_rgba('r',0.1)

circle = plt.Circle(
    (Q.x,Q.y),r,fc=facecolor,ec='k')
ax.add_patch(circle)

pL = geo.get_horizontal_intercept_for_circle_point(
    [Q,r],Q)
A,B = pL
geo.draw_line_segment(ax,[A,B])

C = geo.Point(Q.x,Q.y+r)
geo.draw_line_segment(ax,[Q,C])

D = geo.get_point_by_fractional_length(
    [Q,B],0.8)

# compute the length of the vertical SD
hoz = geo.get_length([Q,D])
print(hoz)

d = math.sqrt(r**2 - hoz**2)
S = geo.Point(D.x,Q.y+d)
geo.draw_line_segment(ax,[D,S])

R = geo.Point(Q.x,S.y)
geo.draw_line_segment(ax,[R,S])

geo.fill_polygon(ax,[Q,R,S,D],fc='b',alpha=0.2)

geo.scatter_points(ax,[A,B,C,Q,D,R,S],s=8)


points = [
          ['A',A,'W',4],
          ['B',B,'E',1],
          ['C',C,'N',1],
          ['D',D,'S',4],
          ['R',R,'W',4],
          ['S',S,'E',1],
          ['Q',Q,'SW',5],
         ]

geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/EII_5.png'
plt.savefig(ofn, dpi=300)