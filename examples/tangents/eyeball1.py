import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

# the eyeball theorem

fig, ax = geo.init()
ax.set(xlim=(-20,130), ylim=(10,90))

Q1 = geo.Point(20,50)
r1 = 25
circle1 = plt.Circle(
    (Q1.x,Q1.y),r1,fc='none',ec='k')
ax.add_patch(circle1)

Q2 = geo.Point(90,50)
r2 = 35
circle2 = plt.Circle(
    (Q2.x,Q2.y),r2,fc='none',ec='k')
ax.add_patch(circle2)

# S,T on Q1
[S,T] = geo.get_tangent_points_on_circle_for_point(
    [Q1,r1],Q2)

[U,V] = geo.get_tangent_points_on_circle_for_point(
    [Q2,r2],Q1)

geo.scatter_points(ax,[Q1,Q2,S,T,U,V])

geo.draw_line_segment(
    ax,[Q1,Q2],ls=':')

geo.draw_line_segments(
    ax,[[Q2,U],[Q2,V],[Q1,S],[Q1,T]],ls=':')

geo.draw_line_segments(
    ax,[[Q2,S],[Q2,T],[Q1,U],[Q1,V]],ec='r')

C = geo.get_intersection_line_segment_circle(
    [Q2,S],[Q2,r2])[0]
    
# why different order?
D = geo.get_intersection_line_segment_circle(
    [Q2,T],[Q2,r2])[1]
   
A = geo.get_intersection_line_segment_circle(
    [Q1,U],[Q1,r1])[1]
B = geo.get_intersection_line_segment_circle(
    [Q1,V],[Q1,r1])[1]

geo.scatter_points(ax,[A,B,C,D])

X = geo.get_point_by_fractional_length([C,D],0.5)
geo.scatter_points(ax,[A,B,C,D,X])

points = [
     ('A',A,'W',5),
     ('B',B,'NW',5),
     ('C',C,'E',3),
     ('D',D,'NE',3),
     ('S',S,'N',1),
     ('T',T,'S',4),
     ('U',U,'NW',2),
     ('V',V,'SW',6),
     ('O',Q1,'W',4),
     ('Q',Q2,'E',1),
     ('X',X,'NE',2) ]

geo.label_points(points)

geo.draw_line_segments(
    ax,[[A,B],[C,D]],ec='b',ls='-',lw=2)

geo.scatter_points(ax,[Q1,Q2,S,T,U,V,A,B,C,D,X])

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/eyeball1.png'
plt.savefig(ofn, dpi=300)