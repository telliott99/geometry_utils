import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

def finish():
    plt.gca().set_axis_off()
    ofn = '/Users/telliott/Desktop/Yiu_circles.png'
    plt.savefig(ofn, dpi=300)
    
    

# radius a
a = 30
# y-coordinate of centers O and P
Y = a + 5

O = geo.Point(Y,Y)
c1 = plt.Circle(
    (O.x,O.y),a,fc='none',ec='k')
ax.add_patch(c1)

P = geo.Point(O.x+a,Y)
c2 = plt.Circle(
    (P.x,P.y),a,fc='none',ec='k')
ax.add_patch(c2)

L = geo.Point(O.x-a,P.y)
K = geo.Point(P.x+a,P.y)
geo.draw_line_segment(ax,[L,K])

# we must compute x and r to actually draw the figure

'''
by eye
x = 10.98
r  = 13
'''


f = math.sqrt(3)
x = (f-1)* (a/2)
r = f*(a/4)


Q = geo.Point(O.x-x,Y+r)
c3 = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(c3)


geo.draw_line_segment(ax,[P,Q],ec='r')

T = geo.get_intersection_line_segment_circle([O,Q],[Q,r])[1]
geo.draw_line_segment(ax,[O,P],ec='r')

X = geo.Point(Q.x,Y)
geo.draw_line_segments(ax,[[Q,X],[O,T]],ec='r')

geo.scatter_points(ax,[O,P,Q,X,T],s=8)


points = [
          ['O',O,'SW',6],
          ['P',P,'NE',2],
          ['Q',Q,'N',1],
          ['X',X,'SW',6],
          ['T',T,'W',3],
         ]

geo.label_points(points)

# end part1
part2 = False
if not part2:
    finish()
    sys.exit()

# part 2

M = geo.get_point_by_fractional_length([O,P],0.5)
N = geo.get_perp_at_point_by_fractional_length(
        [O,M],f=1.0)[0]
C = geo.get_intersection_line_segment_circle(
        [M,N],[O,a])[0]
D = geo.Point(Q.x,C.y)

geo.draw_line_segments(
    ax,[[M,C],[C,D],[D,Q]],ec='b',ls=':')

geo.scatter_points(ax,[M,C,D],s=8)

points = [
          ['M',M,'SW',6],
          ['C',C,'N',3],
          ['D',D,'N',3],
         ]

geo.label_points(points)

finish()
#----------
