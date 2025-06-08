import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,250), ylim=(-10,250))

pL = geo.get_standard_triangle()
A,B,C = pL

geo.fill_polygon(ax,[A,B,C],fc='salmon',alpha=0.2)
geo.outline_polygon(ax,[A,B,C],ec='r')

D = geo.get_point_by_fractional_length([A,B],2.0)
E = geo.get_point_by_fractional_length([A,C],2.0)
M = geo.bisect_angle_Euclid(A,[B,C])
F = geo.get_point_by_fractional_length([A,M],4.0)
geo.draw_line_segment(ax,[B,D],ls=':')
geo.draw_line_segment(ax,[C,E],ls=':')
geo.draw_line_segment(ax,[A,F],ls=':')

def draw_circle(ax,f,c='r'):
    Q = geo.get_point_by_fractional_length([A,M],f)
    S = geo.get_point_perp_on_line_for_point(Q,[A,B])
    T = geo.get_point_perp_on_line_for_point(Q,[A,C])
    geo.scatter_points(ax,[Q,S,T],c=c)
    r = geo.get_length([Q,S])
    circle = plt.Circle((Q.x,Q.y),r, 
        facecolor='none',
        edgecolor=c)
    ax.add_patch(circle)

draw_circle(ax,1.0,c='k')
draw_circle(ax,2.0,c='r')
draw_circle(ax,3.0,c='b')
draw_circle(ax,4.0,c='g')


geo.label_points([('A',A,'SW',10),
                  ('B',B,'SW',14),
                  ('C',C,'W',10),
                  ])

geo.scatter_points(ax,[A,B,C,F])

# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/example20.png'
plt.savefig(ofn, dpi=300)





