import math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,110), ylim=(-50,150))

# change points to match drawing
B = geo.Point(0,43)
C = geo.Point(100,43)
A = geo.Point(40,80)

geo.outline_polygon(ax,[A,B,C],ec='r')
geo.fill_polygon(ax,[A,B,C])

Q,r = geo.get_circumcircle([A,B,C])

circle = plt.Circle((Q.x,Q.y),r, 
    facecolor='none',
    edgecolor='k')
ax.add_patch(circle)

D = geo.get_point_perp_on_line_for_point(
    A,[B,C])

# find correct point of tuple by eye
X = geo.get_intersection_line_segment_circle(
    [A,D],[Q,r])[1]
    
E = geo.get_point_perp_on_line_for_point(
    B,[A,C])
H = geo.get_intersection_for_two_lines([B,E],[A,X])

P = geo.get_intersection_line_segment_circle(
    [B,H],[Q,r])[1]

geo.draw_line_segments(ax,
    [[A,X],[A,H],[C,E],[B,E],[H,E]])

geo.label_points([('A',A,'NE',4),
                  ('B',B,'W',8),
                  ('C',C,'E',3),
                  ('D',D,'NE',2),
                  ('E',E,'W',8),
                  ('H',H,'W',9),
                  ('P',P,'W',7),
                  ('X',X,'S',11),
                    ])

geo.scatter_points(ax,[A,B,C,D,E,H,P,X])


# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/inscribed_prob.png'
plt.savefig(ofn, dpi=300)
