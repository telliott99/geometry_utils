import sys,math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
         
def mark_base_angles(ax,pL):
    A,B,C = pL
    aL = [[C,A,B],[C,B,A]]
    geo.mark_angles(ax,aL,d=5,c='k',s=15)

def mark_top_angles(ax,pL):
    A,B,C = pL
    # although this is repetitive, it was easier to think about
    # some functions need D, and others do not
    D = geo.get_point_by_fractional_length([A,B],0.5)
    aL = [[A,C,D],[B,C,D]]
    geo.mark_angles(ax,aL,d=12,c='r',s=15)

def mark_right_angles(ax,pL):
    A,B,C = pL
    D = geo.get_point_by_fractional_length([A,B],0.5)
    box = geo.mark_right_angle(D,[C,B])
    geo.outline_polygon(ax,box,ec='k')

def draw_vertical(ax,pL):
    A,B,C = pL
    D = geo.get_point_by_fractional_length([A,B],0.5)
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
    geo.draw_line_segment(ax,[U,V],lw=1)

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
    delta = 0.03
    P = geo.get_point_by_fractional_length([A,B],0.5+delta)
    mark_side_at_point(ax,[A,B],P)
    Q = geo.get_point_by_fractional_length([A,B],0.5-delta)
    mark_side_at_point(ax,[A,B],Q)
    
def mark_bases(ax,pL):
    A,B,C = pL
    D = geo.get_point_by_fractional_length([A,B],0.5)
    mark_side_twice(ax,[D,B])
    mark_side_twice(ax,[A,D])
    
def call_func(ax,triL,f):
    for pL in triL:
        f(ax,pL)
#
    

    
    
