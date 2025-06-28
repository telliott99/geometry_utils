import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,400), ylim=(-30,150))

pL = geo.get_standard_triangle(mode='equilateral')
A,B,C = pL

# we want to draw 3 triangles with distinct sides
# can be done more succinctly, but this works

geo.fill_polygon(ax,[A,B,C],fc='salmon',alpha=0.2)
#geo.outline_polygon(ax,[A,B,C],ec='red',lw=2)
geo.draw_line_segment(ax,[A,C],ec='k',lw=2)
geo.draw_line_segment(ax,[A,B],ec='magenta',lw=2)
geo.draw_line_segment(ax,[B,C],ec='b',lw=2)


# middle one rotated 1/3
D,E,F = geo.translate_points([A,B,C],dx=125,dy=0)
Q,r = geo.get_circumcircle([D,E,F])
D,E,F = geo.rotate_points_around_center_by_angle(
    [D,E,F],Q,theta=120)
    
geo.fill_polygon(ax,[D,E,F],fc='salmon',alpha=0.2)
#geo.outline_polygon(ax,[D,E,F],ec='b')
geo.draw_line_segment(ax,[D,F],ec='k',lw=2)
geo.draw_line_segment(ax,[D,E],ec='magenta',lw=2)
geo.draw_line_segment(ax,[E,F],ec='b',lw=2)


# right one rotated 2/3
G,H,I = geo.translate_points([A,B,C],dx=250,dy=0)
Q,r = geo.get_circumcircle([G,H,I])
G,H,I = geo.rotate_points_around_center_by_angle(
    [G,H,I],Q,theta=240)

geo.fill_polygon(ax,[G,H,I],fc='salmon',alpha=0.2)
geo.draw_line_segment(ax,[G,I],ec='k',lw=2)
geo.draw_line_segment(ax,[G,H],ec='magenta',lw=2)
geo.draw_line_segment(ax,[H,I],ec='b',lw=2)

'''
geo.label_points([('A',A,'S',12),
                  ('B',B,'S',12),
                  ('C',C,'NW',5),
                  ('D',D,'S',12),
                  ('E',E,'NW',5),
                  ('F',F,'S',12),
                  ('G',G,'NW',5),
                  ('H',H,'S',12),
                  ('I',I,'S',12),
                   ])

geo.scatter_points(ax,[A,B,C,D,E,F,G,H,I])
'''
# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/equi_rotated.png'
plt.savefig(ofn, dpi=300)





