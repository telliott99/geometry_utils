import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,120), ylim=(-10,120))

pL = geo.get_standard_triangle()
A,B,C = pL
C = geo.nudge(C,'S',20)

geo.fill_polygon(ax,[A,B,C])
geo.outline_polygon(ax,[A,B,C],ec='red')

# draw a line parallel to AC but through D
# to meet bisector of A

M = geo.bisect_angle_Euclid(A,[B,C])
#print(M)

m = geo.get_slope_for_two_points([A,C])
tmp = geo.Point(B.x + 10,B.y + 10*m)

D = geo.get_intersection_for_two_lines([A,M],[B,C])
E = geo.get_intersection_for_two_lines([A,M],[B,tmp])

geo.draw_line_segments(ax,[[B,E],[A,E]],ls=':')

geo.label_points([('A',A,'SW',6),
                  ('B',B,'S',6),
                  ('C',C,'W',5),
                  ('D',D,'S',6),
                  ('E',E,'E',4),
                  ('M',M,'E',4),
                  ])

geo.scatter_points(ax,[A,B,C,D,E,M],s=4)

geo.mark_angles(ax,
    [[C,A,M],[M,A,B],[B,E,D]],c='r',d=8)
geo.mark_angles(ax,
    [[A,D,C],[E,D,B]],c='b',d=5)

# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/bisector1.png'
plt.savefig(ofn, dpi=300)





