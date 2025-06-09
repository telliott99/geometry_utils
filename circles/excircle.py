import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,200), ylim=(-10,200))

pL = geo.get_standard_triangle()
A,B,C = pL
B = geo.nudge(B,'W',10)
C = geo.nudge(C,'NW',5)
C = geo.nudge(C,'N',10)

geo.fill_polygon(ax,[A,B,C])
geo.outline_polygon(ax,[A,B,C],ec='red')
geo.scatter_points(ax,[A,B,C])

# ----------------------------------------

rD1 = geo.get_incenter_and_bisectors([A,B,C])
I = rD1['I']
X,Y,Z = rD1['X'], rD1['Y'], rD1['Z']
r = geo.get_length([I,X])

circle = plt.Circle((I.x,I.y), r, 
    fc='none',
    ec='k')
ax.add_patch(circle)

# ----------------------------------------

tmpD = geo.get_point_by_fractional_length([A,B],2.0)
tmpE = geo.get_point_by_fractional_length([A,C],2.0)

geo.draw_line_segments(ax,[[C,tmpE],[B,tmpD]])

tmpF = geo.get_point_by_fractional_length([A,I],6.0)
geo.draw_line_segments(ax,[[A,tmpF]],ls=':')


# find excircle center
M = geo.bisect_angle_Euclid(B,[C,tmpD])
Ia = geo.get_intersection_for_two_lines(
    [A,I],[B,M])
geo.draw_line_segments(ax,[[B,Ia]],ls=':')

N = geo.bisect_angle_Euclid(C,[B,tmpE])
Ia2 = geo.get_intersection_for_two_lines(
    [A,I],[C,N])
geo.draw_line_segments(ax,[[C,Ia2]],ls=':')

#just to confirm
# print(Ia,Ia2)
#147.263,133.156 147.263,133.156


# find where feet of perpendiculars lie on extensions
D = geo.get_point_perp_on_line_for_point(Ia,[A,B])
E = geo.get_point_perp_on_line_for_point(Ia,[A,C])
F = geo.get_point_perp_on_line_for_point(Ia,[B,C])
r2 = geo.get_length([Ia,F])

'''
print(
    r2,
    geo.get_length([Ia,D]),
    geo.get_length([Ia,E]) )
'''

# 133.15586082714518 133.15586082714518 133.15586082714515
    
circle = plt.Circle((Ia.x,Ia.y), r2, 
    fc='none',
    ec='k')
ax.add_patch(circle)


geo.label_points([('A',A,'SW',10),
                  ('B',B,'S',8),
                  ('C',C,'W',8),
                  ('D',D,'S',8),
                  ('E',E,'W',8),
                  ('F',F,'SE',6),
                  ('X',X,'E',4),
                  ('Y',Y,'W',8),
                  ('Z',Z,'S',8),
                  ('I',I,'N',5),
                  ('Ia',Ia,'S',8),
                  ])

# ----------------------------------------

'''
geo.fill_polygon(ax,[I,Z,B],fc='r',alpha=0.5)
geo.fill_polygon(ax,[Ia,B,D],fc='b',alpha=0.5)
geo.outline_polygon(ax,[A,B,C],ec='red')
'''

geo.scatter_points(ax,[A,B,C,I,Ia,D,E,F,X,Y,Z])

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/excircle.png'
plt.savefig(ofn, dpi=300)





