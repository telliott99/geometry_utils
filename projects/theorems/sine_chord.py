import geometry as geo
import matplotlib.pyplot as plt

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

Q = geo.Point(50,50)
r = 40

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='gray',alpha=0.75)
ax.add_patch(circle)

A = geo.Point(Q.x-r,Q.y)
B = geo.Point(Q.x+r,Q.y)

C = geo.get_point_on_circle_at_distance_for_point(
    [Q,r],25,B)[0]
D = geo.xlc([C,geo.Point(C.x,C.y-5)],[Q,r])[1]
M = geo.gpf([C,D],0.5)


geo.fpg(ax,[A,M,C],alpha=0.1)
geo.dlss(ax,[[A,Q],[A,C]],ec='r')

geo.opg(ax,[Q,M,C])
geo.fpg(ax,[Q,M,C],fc='r',alpha=0.75)

geo.dls(ax,[A,B])
geo.dlss(ax,[[C,D],[A,D]],ls=(2,(3,6)))


geo.scp(ax,[A,B,Q,C,D,M])


geo.savefig(plt)