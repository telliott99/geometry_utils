import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(20,20)
B = geo.Point(80,20)
C = geo.xcc([A,60],[B,60])[1]

X = geo.gpf([B,C],0.6)
theta = geo.get_angle_for_point_on_center(X,A)

phi = 60-theta
tmp = geo.get_point_at_angle_on_circle(
    180-phi,[B,10])
    
Y = geo.xll([A,C],[B,tmp])
P = geo.xll([A,X],[B,Y])

print(geo.get_angle(P,[A,B]))
# 120.00000000000004


geo.fpg(ax,[A,X,C])
geo.fpg(ax,[A,B,Y],fc='b',alpha=0.2)

geo.opg(ax,[A,B,C])


geo.dlss(ax,[[A,X],[B,Y]])

Q,r = geo.gcc([X,Y,P])
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)


geo.scp(ax,[A,B,C,X,Y,P])


geo.savefig(plt)