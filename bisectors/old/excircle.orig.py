import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-10,200), ylim=(-10,200))

pL = geo.get_standard_triangle()
A,B,C = pL
C = geo.nudge(C,'NW',5)

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

geo.scatter_points(ax,[X,Y,Z])

D = geo.get_point_by_fractional_length([A,C],2.0)
E = geo.get_point_by_fractional_length([A,B],2.0)
geo.draw_line_segments(ax,[[C,D],[B,E]])

P = geo.get_point_by_fractional_length([A,I],6.0)
geo.draw_line_segments(ax,[[A,P]],ls=':')

# ----------------------------------------

rD2 = geo.get_incenter_and_bisectors([C,B,D])
rD3 = geo.get_incenter_and_bisectors([B,C,E])

#Ia = geo.get_intersection_from_two_lines(
    #[C,rD2['X']],[B,rD3['X']])

long_bisector1 = geo.get_point_by_fractional_length(
    [C,rD2['X']],5.0)
long_bisector2 = geo.get_point_by_fractional_length(
    [B,rD3['X']],5.0)
#print(long_bisector1,long_bisector2)
Ia = geo.get_intersection_for_two_lines(
    [C,long_bisector1],[B,long_bisector2])

geo.label_points([('B',B,'NW',2),
                  ('C',C,'NW',2),
                  ('D',D,'NW',2),
                  ('E',E,'NW',2)])

geo.draw_line_segments(ax,[[B,Ia],[C,Ia]])

F = geo.get_point_perp_on_line_for_point(Ia,[A,B])
G = geo.get_point_perp_on_line_for_point(Ia,[A,C])
r2 = geo.get_length([Ia,F])
r3 = geo.get_length([Ia,G])
print(r2,r3)

circle = plt.Circle((Ia.x,Ia.y), r2, 
    fc='none',
    ec='k')
ax.add_patch(circle)

geo.label_points([('B',B,'NW',2),
                  ('C',C,'NW',2),
                  ('D',D,'NW',2),
                  ('E',E,'NW',2),
                  ('F',F,'NW',2),
                  ('G',G,'NW',2),
                  ('Ia',Ia,'NW',2),
                  ("rD2['X']",rD2['X'],'N',2),
                  ("rD3['X']",rD3['X'],'N',2),
                  ])

print(geo.get_angle(B,[Ia,E]), 'Ia,B,E]')
print(geo.get_angle(B,[C,Ia]), '[C,B,Ia]')

print(geo.get_angle(C,[D,Ia]), '[D,C,Ia]')
print(geo.get_angle(C,[Ia,B]), '[Ia,C,B]')

P = geo.get_intersection_for_two_lines(
    [A,Ia],[B,C])

print('P', P, 'X', X)
print(geo.get_all_angles([C,A,P]))
print(geo.get_all_angles([P,A,B]))
print(geo.get_all_angles([C,A,X]))
print(geo.get_all_angles([X,A,B]))

geo.scatter_points(ax,[D,E,Ia,rD2['X'],rD3['X']])

# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/excircle.png'
plt.savefig(ofn, dpi=300)





