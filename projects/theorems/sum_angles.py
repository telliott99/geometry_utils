import sys,math
import geometry as geo
from geometry import np, plt

fig, ax = geo.init()

A = geo.Point(10,40)
B = geo.Point(90,40)
Q = geo.get_point_by_fractional_length(
    [A,B],0.5)
r = geo.get_length([A,Q])

circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='gray',alpha=0.5)
ax.add_patch(circle)

# found a bug in this function today!
P = geo.get_point_at_angle_on_circle(
        135, [Q,r])
#R = geo.get_point_at_angle_on_circle(250, [Q,r])
 
R = geo.get_point_at_angle_on_circle(60, [Q,r])
       
geo.opg(ax,[A,B,P],ec='r')
geo.opg(ax,[A,B,R],ec='b')
geo.fpg(ax,[A,B,P],fc='r')
geo.fpg(ax,[A,B,R],fc='b')

geo.dls(ax,[P,R],ec='k',ls=(0,(2,4)))
geo.dls(ax,[A,B],ec='k')


geo.scp(ax,[A,B],c='r')
geo.scp(ax,[P,R])

geo.savefig(plt)
