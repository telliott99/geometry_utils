import math
import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,120), ylim=(-10,100))

pL = geo.get_standard_triangle()
A,B,C = pL
B = geo.nudge(B,'E',20)

geo.fill_polygon(ax,[A,B,C],fc='salmon',alpha=0.2)
geo.outline_polygon(ax,[A,B,C],ec='r')

f = 0.6
d = geo.get_length([A,B])*f
D = geo.Point(C.x+d,C.y)
E = geo.get_point_by_fractional_length([C,B],f)

G = geo.get_point_perp_on_line_for_point(A,[C,E])
H = geo.get_point_perp_on_line_for_point(D,[C,E])

geo.draw_line_segments(
    ax,[[C,D],[D,E],[A,G],[D,H]],ls=':')

geo.label_points([('A',A,'SW',5),
                  ('B',B,'S',5),
                  ('C',C,'W',5),
                  ('D',D,'E',2),
                  ('E',E,'E',2),
                  ('G',G,'NW',4),
                  ('H',H,'NW',4),
                  ])

geo.mark_angles(ax,
    [[A,B,C],[G,C,D]],c='r',d=8)
geo.mark_angles(ax,
    [[C,A,G],[E,D,H]],c='b',d=8)
geo.mark_angles(ax,
    [[A,C,B],[C,E,D]],c='g',d=6)
geo.mark_angles(ax,
    [[C,D,H],[B,A,G]],c='magenta',d=6)
  
pL = geo.mark_right_angle(G,[A,C])
geo.outline_polygon(ax,pL,ec='k')

pL = geo.mark_right_angle(H,[D,E])
geo.outline_polygon(ax,pL,ec='k')

#geo.scatter_points(ax,pL,c='purple')

geo.scatter_points(ax,[A,B,C,D,E],s=4)

# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/similar_dissect.png'
plt.savefig(ofn, dpi=300)

