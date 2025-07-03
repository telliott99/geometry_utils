import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,150), ylim=(0,100))

A = geo.Point(20,20)
B = geo.Point(80,20)
s = geo.get_length([A,B])
C = geo.get_intersection_circle_circle(
    [A,s],[B,s])[1]

pL = [A,B,C]
geo.fpg(ax,pL)
geo.opg(ax,pL)


Q,r = geo.get_circumcircle(pL)
D,E,F = geo.rotate_points_around_center_by_angle(
            pL,Q,180)
            
geo.fpg(ax,[D,E,F])
geo.opg(ax,[D,E,F])

circle1 = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle1)

rho = geo.get_length([C,F])
circle2 = plt.Circle(
    (F.x,F.y),rho,fc='none',ec='k')
ax.add_patch(circle2)

P = geo.get_intersection_line_segment_circle(
    [A,B],[F,rho])[1]
geo.dls(ax,[A,P])

M = geo.get_intersection_for_two_lines(
    [A,B],[C,F])

geo.fpg(ax,[F,P,M],fc='b',alpha=0.2)
geo.opg(ax,[F,P,M],ec='b')


geo.scp(ax,[A,B,C,D,E,F,M,P,Q])

geo.savefig(plt)