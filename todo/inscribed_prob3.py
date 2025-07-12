import math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-40,140), ylim=(-50,140))

Q = geo.Point(20,60)
P = geo.Point(40,85)
Y = geo.Point(45,40)

O,r = geo.get_circumcircle([P,Q,Y])

circle = plt.Circle((O.x,O.y),r, 
    facecolor='none',
    edgecolor='k')
ax.add_patch(circle)

U,V = geo.get_perp_at_point_by_fractional_length(
    [O,P],f=1.0)
    
U,V = V,U

T = geo.get_point_by_fractional_length([P,U],4.0)
S = geo.get_point_by_fractional_length([T,P],2.0)

geo.draw_line_segments(ax,[[S,T]])

O2,r2 = geo.get_circumcircle([P,Q,T])
circle2 = plt.Circle((O2.x,O2.y),r2, 
    facecolor='none',
    edgecolor='k')
ax.add_patch(circle2)

R = geo.get_intersection_line_segment_circle(
    [P,Y],[O2,r2])[1]


Z = geo.get_intersection_line_segment_circle(
    [Q,T],[O,r])[1]

X = geo.get_intersection_for_two_lines(
    [P,Y],[Z,Q])
    

geo.draw_line_segments(ax,[[Z,Y],[P,R],[T,R]])

geo.mark_angles(ax,
    [[Q,P,R],[Q,Z,Y],[P,T,R]],c='r',d=8)

geo.draw_line_segments(ax,[[Q,Z]])

# ----------------------------------------

geo.scatter_points(ax,[P,Q,R,Y,S,T,X,Z],s=6)

'''
geo.label_points([('P',P,'NW',4),
                  ('Q',Q,'W',8),
                  ('Y',Y,'SE',7),
                  ('R',R,'SW',9),
                  ('Z',Z,'SE',7),
                  ('T',S,'W',7),
                  ('S',T,'NE',4),
                  ('X',X,'SW',12),
                    ])

'''


plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/inscribed_prob3.png'
plt.savefig(ofn, dpi=300)
