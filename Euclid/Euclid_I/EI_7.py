import geometry as geo
import matplotlib.pyplot as plt

fig, ax = geo.init()
ax.set(xlim=(-5,150), ylim=(0,100))

A = geo.Point(0,20)
B = geo.Point(50,20)
C = geo.Point(10,60)
D = geo.Point(30,70)

geo.opg(ax,[A,B,C],ec='k')
geo.opg(ax,[A,B,D])
geo.fpg(ax,[A,B,D])

geo.dls(ax,[C,D])

geo.scp(ax,[A,B,C,D])

P,Q,R,_ = geo.translate_points([A,B,C,D],dx=70)
S = geo.Point(P.x+2,D.y+10)
R = geo.nudge(R,'S',10)
R = geo.nudge(R,'E',5)

geo.opg(ax,[P,Q,R],ec='k')
geo.opg(ax,[P,Q,S])
geo.fpg(ax,[P,Q,S])

geo.dls(ax,[R,S])

U = geo.get_point_by_fractional_length([P,R],2.0)
V = geo.get_point_by_fractional_length([P,S],1.4)

geo.dlss(ax,[[R,U]],ls=(0,(3,6)))
geo.dlss(ax,[[S,V]],ls=(0,(3,5)))

geo.scp(ax,[P,Q,R,S,U,V])

#geo.write_one_label(S,'S')

geo.savefig(plt)