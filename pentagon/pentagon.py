import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))


O = geo.Point(50,50)
r = 40

pD = geo.get_pentagon(O,r)
pL = pD['vertices']

rL = geo.rotate_points_around_center_by_angle(pL,O,-90)
A,B,C,D,E = rL

geo.draw_line_segments(ax,[[A,B],[B,C],[C,D],[D,E],[A,E]])

P = geo.get_intersection_for_two_lines([A,C],[B,D])
Q = geo.get_intersection_for_two_lines([B,D],[C,E])
R = geo.get_intersection_for_two_lines([C,E],[A,D])
S = geo.get_intersection_for_two_lines([A,C],[B,E])
T = geo.get_intersection_for_two_lines([A,D],[B,E])

geo.draw_line_segments(ax,[[A,C],[A,D],[B,D],[B,E],[C,E]])


geo.fill_polygon(ax,[A,C,D],fc='r',alpha=0.2)
geo.fill_polygon(ax,[E,R,A],fc='b',alpha=0.2)
geo.fill_polygon(ax,[B,S,P],fc='g',alpha=0.2)

geo.scatter_points(ax,[A,B,C,D,E,P,Q,R,S,T],s=6)




points = [
          ['A',A,'N',1],
          ['B',B,'W',4],
          ['C',C,'W',5],
          ['D',D,'E',2],
          ['E',E,'E',2],
         ]

geo.label_points(points)


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/pentagon.png'
plt.savefig(ofn, dpi=300)