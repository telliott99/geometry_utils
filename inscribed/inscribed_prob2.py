import math
import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,120), ylim=(-40,120))

pL = geo.get_standard_triangle()
[A,B,C] = pL
C = geo.nudge(C,'NE',5)

geo.outline_polygon(ax,[A,B,C],ec='r')
geo.fill_polygon(ax,[A,B,C])

Q,r = geo.get_circumcircle([A,B,C])

circle = plt.Circle((Q.x,Q.y),r, 
    facecolor='none',
    edgecolor='k')
ax.add_patch(circle)

#--------------------

D = geo.get_point_perp_on_line_for_point(C,[A,B])
geo.draw_line_segment(ax,[C,D])

X = geo.bisect_angle_Euclid(C,[A,B])
geo.draw_line_segment(ax,[C,X])

geo.draw_line_segments(ax,[[Q,B],[Q,C]],ls=':')
    
geo.label_points([('A',A,'SW',8),
                  ('B',B,'SE',4),
                  ('C',C,'N',4),
                  ('D',D,'NE',3),
                  ('X',X,'NE',3),
                  ('O',Q,'E',2),
                    ])

# extra

#E = geo.get_intersection_line_segment_circle([C,D],[Q,r])[1]
#Y = geo.get_intersection_line_segment_circle([C,X],[Q,r])[1]
#F = geo.get_intersection_line_segment_circle([C,Q],[Q,r])[1]

#geo.draw_line_segments(ax,[[C,E],[C,Y],[C,F],[E,F]])

#geo.scatter_points(ax,[E,Y,F])

'''
geo.label_points([('E',E,'S',8),
                  ('Y',Y,'S',8),
                  ('F',F,'S',8),
                     ])
'''
# ----------------------------------------

geo.scatter_points(ax,[A,B,C,D,X,Q])

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/inscribed_prob2.png'
plt.savefig(ofn, dpi=300)
