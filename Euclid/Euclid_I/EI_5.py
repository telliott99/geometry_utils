import geometry as geo
import matplotlib.pyplot as plt

fig, ax = geo.init()
ax.set(xlim=(-10,120), ylim=(0,100))

B = geo.Point(5,40)
C = geo.Point(35,40)
M = geo.get_point_by_fractional_length([B,C],0.5)
A = geo.Point(M.x,M.y+40)
D = geo.get_point_by_fractional_length([A,B],1.6)
E = geo.get_point_by_fractional_length([A,C],1.6)

P,Q,R,S,T = geo.translate_points([A,B,C,D,E],dx=60)

#----------------

#geo.opg(ax,[A,B,C])
#geo.opg(ax,[P,Q,R])

geo.dlss(ax,[[A,D],[A,E],[B,C],
             [P,S],[P,T],[Q,R]],ec='k')

#----------------

def panel1():
    geo.fpg(ax,[A,D,C])
    geo.opg(ax,[A,D,C])
    geo.fpg(ax,[P,Q,T],fc='b',alpha=0.2)
    geo.opg(ax,[P,Q,T],ec='b')
   
def panel2():
    geo.fpg(ax,[B,D,C])
    geo.opg(ax,[B,D,C])
    geo.fpg(ax,[Q,R,T],fc='b',alpha=0.2)
    geo.opg(ax,[Q,R,T],ec='b')

#panel1()
panel2()

geo.scp(ax,[A,B,C,D,E,P,Q,R,S,T])


geo.savefig(plt)