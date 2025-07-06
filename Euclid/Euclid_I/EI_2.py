import geometry as geo
from geometry import np, plt

fig, ax = geo.init()

A = geo.Point(10,5)
B = geo.Point(30,30)
C = geo.Point(45,35)
A,B,C = geo.translate_points([A,B,C],dx=0,dy=20)

geo.draw_line_segments(ax,[[B,C]],ec='k')

r = geo.get_length([A,B])
D,_ = geo.get_intersection_circle_circle(
    [A,r],[B,r])

geo.fpg(ax,[A,B,D])

U = geo.get_point_by_fractional_length(
    [D,B],2.0)
V = geo.get_point_by_fractional_length(
    [D,A],2.0)
geo.dlss(ax,[[D,U],[D,V]],ls=':')


r1 = geo.get_length([B,C])
c1 = plt.Circle(
    (B.x,B.y),r1,fc='none',ec='gray',alpha=0.4)
ax.add_patch(c1)

E = geo.get_intersection_line_segment_circle(
    [B,D],[B,r1])[0]

r2 = geo.get_length([D,E])
c2 = plt.Circle(
    (D.x,D.y),r2,fc='none',ec='k',alpha=1.0,ls=':')
ax.add_patch(c2)

F = geo.get_intersection_line_segment_circle(
    [A,D],[D,r2])[0]

geo.opg(ax,[A,B,D])

geo.dls(ax,[A,F])

geo.scp(ax,[A,B,C,D,E,F],s=6)

geo.savefig(plt)



