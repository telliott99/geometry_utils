import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(20,20)
B = geo.Point(80,20)
C = geo.xcc([A,60],[B,60])[1]

geo.opg(ax,[A,B,C])
geo.fpg(ax,[A,B,C],alpha=0.3)

iD = geo.get_incenter_and_bisectors([A,B,C])
I = iD['I']
X = iD['X']
r = geo.get_length([I,X])

circle = plt.Circle(
    (I.x,I.y),r,fc='white',ec='k')
ax.add_patch(circle)

geo.dlss(ax,[[I,C],[I,X]])

geo.scp(ax,[A,B,C])

geo.savefig(plt)