import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-40,100), ylim=(-30,150))

n = 30
A = geo.Point(0,40)
B = geo.Point(n*2,40)
C = geo.get_intersection_circle_circle(
    [B,n*(math.sqrt(3))],[A,n])[0]

geo.outline_polygon(ax,[A,B,C])
print(geo.get_angle(C,[A,B]))

sqL = geo.get_rectangle([A,B])
M = geo.get_point_by_fractional_length([A,B],0.5)
rL1 = geo.rotate_points_around_center_by_angle(sqL,M,180)
# by eye
D,E = rL1[2:]
geo.outline_polygon(ax,[A,B,E,D],ec='k')

rL2 = geo.get_rectangle([A,C])
G,F = rL2[2:] 
geo.outline_polygon(ax,[A,F,G,C],ec='b')

rL3 = geo.get_rectangle([B,C])
I,H = rL3[2:] 
geo.outline_polygon(ax,[B,C,I,H],ec='r')

points = [
          ['A',A,'SW',8],
          ['B',B,'SE',4],
          ['C',C,'NW',5],
          ['D',D,'SW',8],
          ['E',E,'S',5],
          ['F',F,'SW',9],
          ['G',G,'NW',4],
         ]

geo.label_points(points)
geo.scatter_points(ax,[A,B,C,D,E,F,G,H,I],s=6)

Z = geo.get_perp_on_line_for_point([D,E],C)
X = geo.get_intersection_for_two_lines([A,B],[C,Z])

def fig1(ax):
    geo.draw_line_segment(ax,[C,Z],ls=':')
    geo.fill_polygon(ax,[A,D,Z,X],fc='gray',alpha=0.3)
    geo.fill_polygon(ax,[A,C,G,F],fc='b',alpha=0.2)
    points = [
              ['X',X,'NE',3],
              ['Z',Z,'S',6],
             ]
    geo.label_points(points)
    geo.scatter_points(ax,[X,Z],s=6)

fig1(ax)

def fig2(ax):
    geo.draw_line_segment(ax,[B,F],ec='b',ls=':')
    geo.draw_line_segment(ax,[C,D],ec='gray',ls=':')
    geo.fill_polygon(ax,[A,C,D],fc='gray',alpha=0.3)
    geo.fill_polygon(ax,[F,A,B],fc='b',alpha=0.2)

#fig2(ax)



plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/Pthm.png'
plt.savefig(ofn, dpi=300)


