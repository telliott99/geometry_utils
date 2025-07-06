import sys,math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

# draw a line
A = geo.Point(10,70)
B = geo.Point(80,70)

# bisect it
C = geo.get_point_by_fractional_length(
    [A,B],0.5)

#-----

# arbitrary point
f = 0.35
# between C and B
D = geo.get_point_by_fractional_length(
    [C,B],f)

# draw the square on DB (i.e. BD, so down)
BDHM = geo.get_rectangle_for_line(
    [B,D],aspect_ratio=1.0)

geo.outline_polygon(ax,BDHM,ec='k')
H,M = BDHM[2:]

#-----

# find K and L on extension of HM, perp to A and C
S,T = geo.get_perp_at_point_by_fractional_length(
    [A,C],0)

K = geo.get_intersection_for_two_lines(
    [S,T],[H,M])
    
S,T = geo.get_perp_at_point_by_fractional_length(
    [A,C],1)

L = geo.get_intersection_for_two_lines(
    [S,T],[H,M])
        
#-----

# get the square on CB (i.e. BC, so down)
_,_,E,F = geo.get_rectangle_for_line(
    [B,C],aspect_ratio=1.0)

# find G as the intersection
G = geo.get_intersection_for_two_lines(
    [E,F],[D,H])
     
#-----
# we have all the points now

CAKL = [C,A,K,L]
HLEG = [H,L,E,G]
DCLH = [D,C,L,H]
MHGF = [M,H,G,F]

#-----
# finally, fill the polygons

geo.fill_polygon(ax,CAKL,fc='orange',alpha=1.0)
geo.fill_polygon(ax,HLEG,fc='dodgerblue',alpha=1.0)

geo.fill_polygon(ax,[B,C,L,M],fc='salmon',alpha=0.4)
geo.fill_polygon(ax,[B,D,G,F],fc='salmon',alpha=0.4)


geo.outline_polygon(ax,CAKL,ec='k')
geo.outline_polygon(ax,DCLH,ec='k')
geo.outline_polygon(ax,MHGF,ec='k')
geo.outline_polygon(ax,HLEG,ec='b')


geo.scatter_points(
    ax,[A,B,C,D,F,K,M],s=6)

geo.scatter_points(
    ax,[H,L,E,G],s=6,c='b')


geo.label_points(
    [['A',A,'W',4],
     ['B',B,'N',1],
     ['C',C,'N',1],
     ['D',D,'N',1],
     ['E',E,'W',4],
     ['F',F,'E',1],
     ['G',G,'NE',1],
     ['H',H,'NE',1],
     ['K',K,'W',4],
     ['L',L,'NE',1],
     ['M',M,'E',1],
     ])


geo.savefig(plt,ofn='EuclidII_5.png')