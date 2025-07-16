import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

Q = geo.Point(40,40)
r = 30
cl = geo.get_circle(Q,r,fc='none',ec='k')
ax.add_patch(cl)

tmp = geo.Point(Q.x+5,Q.y)
A,B = geo.xlc([Q,tmp],[Q,r])
geo.dls(ax,[A,B])

C,D = geo.get_point_on_circle_at_distance_for_point(
    [Q,r],25,B)
E = geo.xll([A,B],[C,D])


geo.opg(ax,[A,C,E])
geo.fpg(ax,[A,C,E])

geo.opg(ax,[Q,C,E])
geo.fpg(ax,[Q,C,E])

geo.opg(ax,[B,C,E],ec='b')
#geo.fpg(ax,[B,C,E])



geo.savefig(plt)

