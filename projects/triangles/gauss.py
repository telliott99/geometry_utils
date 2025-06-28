import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-15,120), ylim=(-10,120))

Q = geo.Point(50,50)
r = 60

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

A,B = geo.get_horizontal_intercept_for_circle_point(
    [Q,r],geo.Point(10,20))
C = geo.get_point_on_circle_at_distance_for_point(
    [Q,r],80,A)[0]

geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])

Q,r = geo.get_circumcircle([A,B,C])

gD = geo.get_centroid_and_medians([A,B,C])
K = gD['K'];  L = gD['L'];  M = gD['M']

oD = geo.get_orthocenter_and_altitudes([K,L,M])
D = oD['D'];  E = oD['E'];  F = oD['F']

geo.outline_polygon(ax,[K,L,M],ec='b')
geo.fill_polygon(ax,[K,L,M],fc='b',alpha=0.2)

geo.outline_polygon(ax,[D,E,F],ec='k')
geo.fill_polygon(ax,[D,E,F],fc='k',alpha=0.4)

geo.scatter_points(ax, [A,B,C,D,E,F,K,L,M])
geo.scatter_points(ax, [Q],c='w')

'''

points = [
          ['A',A,'N',0],
          ['B',B,'N',0],
          ['C',C,'N',0],
         ]

geo.label_points(points)
'''

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/gauss.png'
plt.savefig(ofn, dpi=300)