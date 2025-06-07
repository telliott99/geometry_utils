import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,300), ylim=(-10,150))

pL = geo.get_standard_triangle()
A,B,C = pL
C = geo.nudge(C,'N',20)

geo.fill_polygon(ax,[A,B,C],fc='salmon',alpha=0.2)
#geo.outline_polygon(ax,[A,B,C],ec='red',lw=2)
geo.draw_line_segment(ax,[A,C],ec='k',lw=2)
geo.draw_line_segment(ax,[A,B],ec='magenta',lw=2)
geo.draw_line_segment(ax,[B,C],ec='b',lw=2)


D,E,F = geo.translate_points([A,B,C],dx=80,dy=40)
Q,r = geo.get_circumcircle([D,E,F])

D,E,F = geo.rotate_points_around_center_by_angle(
    [D,E,F],Q,theta=165)
geo.fill_polygon(ax,[D,E,F],fc='salmon',alpha=0.2)
#geo.outline_polygon(ax,[D,E,F],ec='b')
geo.draw_line_segment(ax,[D,F],ec='k',lw=2)
geo.draw_line_segment(ax,[D,E],ec='magenta',lw=2)
geo.draw_line_segment(ax,[E,F],ec='b',lw=2)

K,L,M = geo.mirror_points([A,B,C])
K,L,M = geo.translate_points([K,L,M],dx=270,dy=0)

geo.fill_polygon(ax,[K,L,M],fc='salmon',alpha=0.2)
#geo.outline_polygon(ax,[K,L,M],ec='g')
geo.draw_line_segment(ax,[K,M],ec='k',lw=2)
geo.draw_line_segment(ax,[K,L],ec='magenta',lw=2)
geo.draw_line_segment(ax,[L,M],ec='b',lw=2)

geo.label_points([('A',A,'SW',10),
                  ('B',B,'S',8),
                  ('C',C,'NW',5),
                  ('D',D,'SE',6),
                  ('E',E,'W',8),
                  ('F',F,'S',8),
                  ('K',K,'S',8),
                  ('L',L,'SW',10),
                  ('M',M,'N',4),
                   ])

geo.scatter_points(ax,[A,B,C,D,E,F,K,L,M])

# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/example19.png'
plt.savefig(ofn, dpi=300)





