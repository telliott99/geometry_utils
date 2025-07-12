import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))


def get_pentagon(Q,r):

    # get its diameter
    A,L = geo.get_horizontal_intercept_for_circle_point(
        [O,r],O)
        
    # find the point at the top
    S = geo.Point(O.x,O.y+r)
    
    # so as to bisect that radius
    P = geo.get_point_by_fractional_length([O,S],0.5)
    
    # the key construct, bisect < APO
    tmp = geo.bisect_angle_Euclid(P,[O,A])
    
    # find where the bisector cuts the diameter
    Q = geo.get_intersection_for_two_lines([P,tmp],[A,O])
    
    # go up/down vertically to find points of the pentagon
    B,E = geo.get_intersection_line_segment_circle(
        [Q,geo.Point(Q.x,Q.y+10)]
        ,[O,r])
    
    # we want a right angle at P
    tmp = geo.get_perp_at_point_by_fractional_length(
        [Q,P],1.0)
    
    # find where it intersects with the diameter
    R = geo.get_intersection_for_two_lines(tmp,[A,O])
    
    # we want a vertical through R
    tmp = geo.Point(R.x,R.y+10)
    D,C = geo.get_intersection_line_segment_circle([R,tmp],[O,r])
    
    rD = {'vertices':[A,B,C,D,E],
          'extras':[L,P,Q,R,S] }

    return rD

if __name__ == "__main__":

    # construct a circle
    r = 40
    Y = r + 10
    O = geo.Point(Y,Y)

    circle = plt.Circle(
        (O.x,O.y),r,fc='none',ec='k')
    ax.add_patch(circle)
    
    rD = get_pentagon(O,r)
    A,B,C,D,E = rD['vertices']
    L,P,Q,R,S = rD['extras']

    geo.draw_line_segment(ax,[B,E],ls=':',ec='gray')
    geo.draw_line_segments(ax,[[L,A],[O,S],[P,A]])
    geo.draw_line_segment(ax,[O,P],ls=':')
    geo.outline_polygon(ax,[P,Q,R])
    
    # a slight extension of AP
    tmp = geo.get_point_by_fractional_length([A,P],1.2)
    geo.draw_line_segments(ax,[[C,D],[P,tmp]],ls=':')
    
    geo.fill_polygon(ax,[P,Q,R])
    
    points = [
              ['A',A,'E',2],
              ['O',O,'S',4],
              ['Q',Q,'S',4],
              ['B',B,'N',2],
              ['E',E,'S',4],
              ['P',P,'NE',2],
              ['R',R,'S',4],
              ['C',C,'E',2],
              ['D',D,'E',2],
              ]
    
    geo.label_points(points)
    
    geo.scatter_points(ax,[A,O,P,S,L,Q,B,E,R,C,D])
    
    #----------
    
    plt.gca().set_axis_off()
    ofn = '/Users/telliott/Desktop/pentagon_constr1.png'
    plt.savefig(ofn, dpi=300)