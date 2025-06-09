import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,180), ylim=(-50,150))

'''
std functions
geo.outline_polygon(ax,[A,B,C])
geo.fill_polygon(ax,[A,B,C])
geo.draw_line_segments(ax,[[D,F],[C,F]])
rL = geo.mark_right_angle(D,[B,F],n=3)

geo.get_point_by_fractional_length([A,B],f)
geo.get_intersection_for_two_lines([A,B],[C,D])
geo.get_point_perp_on_line_for_point(A,pL)
geo.get_perp_at_point_by_fractional_length(pL,f=0.5)

get_intersection_line_segment_circle(pL,cL)
get_intersection_circle_circle(cL1,cL2)
get_tangent_points_on_circle_for_point(cL1,P)
mark_right_angle(A,pL,n=3)

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)
'''

pL = geo.get_standard_triangle()
A,B,C = pL

iD = geo.get_incenter_and_bisectors([A,B,C])
I,X,Y,Z = iD['I'],iD['X'],iD['Y'],iD['Z']
r = geo.get_length([I,X])

circle = plt.Circle(
    (I.x,I.y),r,fc='none',ec='k')
ax.add_patch(circle)

P,Q = geo.get_perp_at_point_by_fractional_length(
    [C,I],f=1.0)
M,N = geo.get_perp_at_point_by_fractional_length(
    [C,B],f=1.0)
    
L = geo.get_intersection_for_two_lines([P,Q],[M,N])
K = geo.get_intersection_for_two_lines([B,C],[I,L])

# relabel to be consistent with previous
D = X
E = Y
F = Z

geo.fill_polygon(ax,[A,I,F],fc='b',alpha=0.15)
geo.fill_polygon(ax,[D,I,K],fc='g',alpha=0.2)

geo.outline_polygon(ax,[A,I,F],ec='k')
geo.outline_polygon(ax,[D,I,K],ec='k')

geo.fill_polygon(ax,[C,K,L],fc='r',alpha=0.1)
geo.fill_polygon(ax,[B,K,L],fc='r',alpha=0.3)

#geo.fill_polygon(ax,[A,B,C])
geo.outline_polygon(ax,[A,B,C])

geo.draw_line_segments(ax,[[B,L],[C,L],[I,L]])
geo.draw_line_segments(ax,[[B,I],[C,I],[E,I]],ec='k',ls=':')

points = [
          ['A',A,'S',8],
          ['B',B,'S',8],
          ['C',C,'W',8],
          ['D',D,'NE',3],
          ['E',E,'W',8],
          ['F',F,'S',8],
          ['I',I,'N',4],
          ['K',K,'N',3],
          ['L',L,'NE',4],
         ]

Q = geo.get_point_by_fractional_length([C,L],0.5)
r2 = geo.get_length([C,Q])

circle2 = plt.Circle(
    (Q.x,Q.y),r2,fc='none',ec='b',ls=':',lw=1.5)
ax.add_patch(circle2)

geo.scatter_points(ax,[A,B,C,I,D,E,F,K,L,Q],s=10)
geo.label_points(points)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/heron.png'
plt.savefig(ofn, dpi=300)