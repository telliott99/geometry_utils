import geometry as geo
from geometry import np, plt

fig, ax = geo.init()

A = geo.Point(50,50)
r = 30

B = geo.Point(30,50)
C = geo.Point(45,60)

rL = geo.get_intersection_line_segment_circle(
    [B,C],(A,r))
P,R = rL

circle = plt.Circle(
    (A.x,A.y),r,fc='none',ec='k')
ax.add_patch(circle)

geo.draw_line_segments(ax,[[B,C]],ec='k')
geo.draw_line_segments(ax,[[P,B]],ec='r',ls=':')
geo.draw_line_segments(ax,[[C,R]],ec='r',ls=':')

geo.scp(ax,[P,B,C,R,A],s=6)

geo.savefig(plt)



