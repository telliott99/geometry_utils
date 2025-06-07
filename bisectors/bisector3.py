import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,120), ylim=(-40,100))

A = geo.Point(10,40)
B = geo.Point(90,40)
C = geo.Point(25,80)

geo.fill_polygon(ax,[A,B,C])
geo.outline_polygon(ax,[A,B,C],ec='red')

Q,r = geo.get_circumcircle([A,B,C])

circle1 = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle1)

M = geo.bisect_angle_Euclid(C,[A,B])
D = geo.get_intersection_line_segment_circle(
        [C,M],[Q,r])[1]
        
geo.draw_line_segment(ax,[C,D],ec='r')
geo.draw_line_segments(ax,[[A,D],[B,D]])

geo.label_points([('A',A,'SW',8),
                  ('B',B,'SE',8),
                  ('C',C,'W',6),
                  ('D',D,'S',8),
                  ('M',M,'NE',3),
                  ])

geo.mark_angles(ax,
    [[A,C,D],[B,C,D],[B,A,D],[D,B,A]],c='k',d=8,s=9)

geo.scatter_points(ax,[A,B,C,D,M])


# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/bisector3.png'
plt.savefig(ofn, dpi=300)





