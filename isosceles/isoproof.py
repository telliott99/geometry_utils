import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,120), ylim=(-10,100))

pL = geo.get_standard_triangle(mode='isosceles')
A,B,C = pL
lw = 2
SZ = 22

geo.outline_polygon(ax,[A,B,C],lw=lw)
geo.fill_polygon(ax,[A,B,C])
         
points = [
          ['A',A,'W',6],
          ['B',B,'E',2],
          ['C',C,'NW',3],
         ]

geo.label_points(points,SZ=SZ)

def mark_base_angles(ax,pL):
    A,B,C = pL
    aL = [[C,A,B],[C,B,A]]
    geo.mark_angles(ax,aL,d=5,c='k',s=25)

def mark_top_angles(ax,pL,D):
    A,B,C = pL
    aL = [[A,C,D],[B,C,D]]
    geo.mark_angles(ax,aL,d=10,c='r',s=25)

def mark_right_angle(ax,pL,D):
    A,B,C = pL
    box = geo.mark_right_angle(D,[C,B])
    geo.outline_polygon(ax,box,ec='k')

def draw_vertical(ax,pL,D):
    A,B,C = pL
    geo.draw_line_segment(ax,[C,D])

def mark_side_at_point(ax,pL,P):
    A,B = pL
    
    # we don't have get_perp_at_point yet
    m = geo.get_length([A,P])
    n = geo.get_length([A,B])
    f = m/n
    S,T = geo.get_perp_at_point_by_fractional_length(
        pL,f)
        
    length = geo.get_length([P,S])
    d = 4
    f = d/length 
      
    U = geo.get_point_by_fractional_length([P,S],f)
    length = geo.get_length([P,T])
    f = d/length   
    V = geo.get_point_by_fractional_length([P,T],f)
    geo.draw_line_segment(ax,[U,V],lw=2)

def mark_side_once(ax,pL):
    A,B = pL
    P = geo.get_point_by_fractional_length([A,B],0.5)
    mark_side_at_point(ax,[A,B],P)
    
def mark_sides(ax,pL):
    A,B,C = pL
    mark_side_once(ax,[A,C])
    mark_side_once(ax,[B,C])

def mark_side_twice(ax,pL):
    A,B = pL
    delta = 0.02
    P = geo.get_point_by_fractional_length([A,B],0.5+delta)
    mark_side_at_point(ax,[A,B],P)
    Q = geo.get_point_by_fractional_length([A,B],0.5-delta)
    mark_side_at_point(ax,[A,B],Q)
    
def mark_base(ax,pL,D):
    A,B,C = pL
    mark_side_twice(ax,[D,B])
    mark_side_twice(ax,[A,D])

def show_P(ax,P):
    geo.write_one_label(P,'D',dx=0,dy=-9,SZ=SZ)  
    #geo.scatter_points(ax,[P])

def all(ax,pL,P):
    A,B,C = pL
    draw_vertical(ax,[A,B,C],D)
    show_P(ax,P)  
    mark_top_angles(ax,[A,B,C],P)
    mark_base_angles(ax,[A,B,C])  
    mark_right_angle(ax,[A,B,C],P)
    mark_base(ax,[A,B,C],P)


D = geo.get_point_by_fractional_length([A,B],0.5)

mark_sides(ax,[A,B,C])

draw_vertical(ax,[A,B,C],D)
show_P(ax,D)
# mark_top_angles(ax,[A,B,C],D)

#all(ax,[A,B,C],D)

# mark_base_angles(ax,[A,B,C])

mark_base(ax,[A,B,C],D)

geo.scatter_points(ax,[A,B,C],s=10)

#mark_right_angle(ax,[A,B,C],D)

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/isoproof.png'
plt.savefig(ofn, dpi=300)