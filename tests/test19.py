import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,300), ylim=(-30,180))

pL = geo.get_standard_triangle()
A,B,C = pL
C = geo.nudge(C,'N',20)

# we want to draw 3 triangles with distinct sides
# can be done more succinctly, but this works

geo.fill_polygon(ax,[A,B,C],fc='salmon',alpha=0.2)
#geo.outline_polygon(ax,[A,B,C],ec='red',lw=2)
geo.draw_line_segment(ax,[A,C],ec='k',lw=2)
geo.draw_line_segment(ax,[A,B],ec='magenta',lw=2)
geo.draw_line_segment(ax,[B,C],ec='b',lw=2)

# middle one rotated
D,E,F = geo.translate_points([A,B,C],dx=80,dy=40)
Q,r = geo.get_circumcircle([D,E,F])
D,E,F = geo.rotate_points_around_center_by_angle(
    [D,E,F],Q,theta=165)
    
geo.fill_polygon(ax,[D,E,F],fc='salmon',alpha=0.2)
#geo.outline_polygon(ax,[D,E,F],ec='b')
geo.draw_line_segment(ax,[D,F],ec='k',lw=2)
geo.draw_line_segment(ax,[D,E],ec='magenta',lw=2)
geo.draw_line_segment(ax,[E,F],ec='b',lw=2)

# and a mirror image, also rotated a bit
G,H,I = geo.mirror_points(
    [A,B,C],[geo.Point(130,B.y)])
Q,r = geo.get_circumcircle([G,H,I])
G,H,I = geo.rotate_points_around_center_by_angle(
    [G,H,I],Q,theta=25)

geo.fill_polygon(ax,[G,H,I],fc='salmon',alpha=0.2)
#geo.outline_polygon(ax,[K,L,M],ec='g')
geo.draw_line_segment(ax,[G,I],ec='k',lw=2)
geo.draw_line_segment(ax,[G,H],ec='magenta',lw=2)
geo.draw_line_segment(ax,[H,I],ec='b',lw=2)

geo.label_points([('A',A,'SW',10),
                  ('B',B,'S',8),
                  ('C',C,'NW',5),
                  ('D',D,'SE',6),
                  ('E',E,'W',8),
                  ('F',F,'S',8),
                  ('G',G,'S',8),
                  ('H',H,'W',9),
                  ('I',I,'N',4),
                   ])

geo.scatter_points(ax,[A,B,C,D,E,F,G,H,I])

# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ex19.png'
plt.savefig(ofn, dpi=300)





