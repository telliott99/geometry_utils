import geometry as geo
import matplotlib.pyplot as plt

fig, ax = geo.init()
ax.set(xlim=(-50,110), ylim=(-10,100))

pL = geo.gtr()
A,B,C = pL

D = geo.get_point_for_cyclic_quadrilateral(
    A,[B,C],m=0.5)

Q,r = geo.get_circumcircle([A,B,C])
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='gray',alpha=0.6)
ax.add_patch(circle)

geo.opg(ax,[A,B,D,C])
geo.dlss(ax,[[A,D],[B,C]],ls=':')
geo.fpg(ax,[A,B,C])

aL = [[A,C,B],[A,D,B]]
geo.mark_angles(
    ax,aL,d=5,c='k',s=20)

aL = [[C,D,A],[A,B,C]]
geo.mark_angles(
    ax,aL,d=5,c='r',s=20)

points = [
     ('A',A,'SW',5),
     ('B',B,'SE',3),
     ('D',C,'NW',3),
     ('C',D,'N',3) ]

geo.label_points(points)


geo.savefig(plt)