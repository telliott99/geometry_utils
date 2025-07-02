import sys,math
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

# draw a line
A = geo.Point(20,50)
B = geo.Point(60,50)

# construct the square on BA
BADC = geo.get_rectangle_for_line(
    [B,A],aspect_ratio=1.0)
_,_,D,C = BADC
geo.opg(ax,BADC)

# bisect AC
E = geo.get_point_by_fractional_length(
    [A,D],0.5)
    
# draw the circle on center E with radius BE
r = geo.get_length([B,E])
circle = plt.Circle(
    (E.x,E.y),r,fc='none',ec='k')
ax.add_patch(circle)

# find F on the circle
F = geo.get_intersection_line_segment_circle(
        [D,A],[E,r])[1]
        
# construct the square on FA
# b/c get_rectangle_for_line not currently working
f = geo.get_length([A,F])/geo.get_length([A,B])
H = geo.get_point_by_fractional_length(
    [A,B],f)
    
M = geo.get_point_by_fractional_length(
    [H,F],0.5)
G = geo.get_point_by_fractional_length(
    [A,M],2)

FAHG = [F,A,H,G]
geo.opg(ax,FAHG)

K = geo.get_intersection_for_two_lines([C,D],[G,H])
HBCK = [H,B,C,K]

geo.fpg(ax,HBCK)
geo.fpg(ax,FAHG,fc='b',alpha=0.2)

geo.dls(ax,[B,E])
geo.dls(ax,[H,K],ls=':')

geo.scp(ax,[A,B,C,D,E,F,G,H,K])

geo.savefig(plt,ofn='EuclidII_10.png')