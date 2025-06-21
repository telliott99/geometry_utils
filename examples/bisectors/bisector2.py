import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-180,120), ylim=(-10,120))

pL = geo.get_standard_triangle()
A,B,C = pL
C = geo.nudge(C,'S',20)

geo.fill_polygon(ax,[A,B,C])
geo.outline_polygon(ax,[A,B,C],ec='red')

# draw a line parallel to AC but through D
# to meet bisector of A

D = geo.get_point_by_fractional_length([A,C],2.0)
M = geo.bisect_angle_Euclid(C,[B,D])

m = geo.get_slope_for_two_points([C,M])
tmp = geo.Point(A.x + 10,A.y + 10*m)
E = geo.get_intersection_for_two_lines([A,tmp],[B,C])

geo.draw_line_segment(ax,[C,D])
geo.draw_line_segments(ax,[[A,E],[C,M],[C,D]],ls=':')

F = geo.get_intersection_for_two_lines([A,B],[M,C])
geo.draw_line_segments(ax,[[A,F],[M,F]],ls=':')

geo.label_points([('A',A,'S',8),
                  ('B',B,'S',8),
                  ('C',C,'W',8),
                  ('D',D,'W',8),
                  ('E',E,'E',2),
                  ('F',F,'SW',10),
                  ('M',M,'E',4),
                  ])

geo.mark_angles(ax,
    [[D,C,M],[M,C,B],[C,A,E],[A,E,C]],c='r',d=8)

geo.scatter_points(ax,[A,B,C,D,E,F,M],s=4)


# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/bisector2.png'
plt.savefig(ofn, dpi=300)





