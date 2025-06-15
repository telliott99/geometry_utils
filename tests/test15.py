import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

# todo:  move this function to the library
# from the proof for Pythagorean theorem
# based on broken chord

# do this smarter!!

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

Q = geo.Point(50,50)
A = geo.Point(20,60)
r = geo.get_length([A,Q])
B = geo.get_point_reflected_on_diameter(A,[Q,r])

# CCW first
pL = geo.get_point_on_circle_at_distance_for_point(
    [Q,r],40,B)
C = pL[0]
    
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)

def mirror_triangle_in_circle(pL):
    A,B,C = pL
    tmp = geo.Point(A.x+10,A.y)
    # since A *is* on circle, it will be [0]
    D = geo.get_intersection_line_segment_circle(  
        [A,tmp],[Q,r])[1]
    E = geo.get_point_reflected_on_diameter(
        D,[Q,r])
    tmp = geo.Point(C.x-10,C.y)
    # similarly for C
    F = geo.get_intersection_line_segment_circle(  
        [C,tmp],[Q,r])[1]
    return D,E,F
    
D,E,F = mirror_triangle_in_circle([A,B,C])

P = geo.get_intersection_for_two_lines(
    [A,B],[E,F])

geo.fill_polygon(ax,[A,B,C],fc='lightsalmon',alpha=0.4)
geo.fill_polygon(ax,[D,E,F],fc='blue',alpha=0.15)

geo.outline_polygon(ax,[A,B,C],ec='r')
geo.outline_polygon(ax,[D,E,F],ec='b')

# ['A',A,'SW',6]

points = [
     ('A',A,'W',4),
     ('B',B,'E',2),
     ('C',C,'N',1),
     ('D',D,'E',2),
     ('E',E,'W',4),
     ('F',F,'N',2),
     ('P',P,'SW',6) ]

geo.label_points(points)

geo.scatter_points(ax,[A,B,C,D,E,F,P])

#----------

#plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/example15.png'
plt.savefig(ofn, dpi=300)