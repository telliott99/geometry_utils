import geometry as geo
import matplotlib.pyplot as plt

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(-20,100))

A = geo.Point(10,30)
B = geo.Point(80,25)
C = geo.Point(25,80)

Q,r = geo.get_circumcircle([A,B,C])

K = geo.get_perp_on_line_for_point([A,B],Q)

bD = geo.get_incenter_and_bisectors([A,B,C])
I = bD['I']

M = geo.xlc([C,I],[Q,r])[1]

#-----

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='gray',alpha=0.5)
ax.add_patch(circle)

rho = geo.get_length([I,bD['Z']])
circle2 = plt.Circle(
    (I.x,I.y),rho,fc='none',ec='k',ls=':')
ax.add_patch(circle2)

geo.opg(ax,[A,B,C])

geo.dlss(ax,[[C,M],[Q,M],[B,M]])

box = geo.mark_right_angle(K,[Q,B])
geo.opg(ax,box,ec='k')

aL = [[I,C,A],[B,C,I],[A,B,M]]
geo.mark_angles(ax,aL,d=10,c='b',s=20)

geo.dls(ax,[I,B],ec='r')


geo.scp(ax,[A,B,C,I,Q,M])


geo.savefig(plt)
