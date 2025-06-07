import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import broken_chord as bc

fig,ax,fD = bc.setup()
ax.set(xlim=(-50,120), ylim=(0,120))

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']


# "erasing" E
geo.scatter_points(ax,[E],c='white',s=12)
geo.draw_line_segment(ax,[B,A])

# ----------------------------------------

Z = geo.get_intersection_line_segment_circle(
    [M,D],[Q,r])[1]
geo.draw_line_segment(ax,[D,Z],ec='r')

K = geo.get_intersection_line_segment_circle(
    [M,Q],[Q,r])[0]
    
geo.draw_line_segment(ax,[M,K],ec='r')

H = geo.get_intersection_for_two_lines(
    [M,K],[A,B])
    
T = geo.get_intersection_for_two_lines(
    [M,K],[A,G])

L = geo.get_point_perp_on_line_for_point(
    K,[A,B])

# redefine E
P = geo.get_intersection_for_two_lines(
    [L,K],[A,G])

# redefine E
E = geo.get_intersection_for_two_lines(
    [M,K],[A,B])

geo.draw_line_segments(ax,[[G,A],[Z,K],[K,L]],ec='r')

geo.fill_polygon(ax,[M,Z,K],alpha=0.5)
geo.fill_polygon(ax,[A,L,P],fc='blue')

geo.scatter_points(ax,[Z,K,H,T,H,M,L,P,E])


points = [
     ('Z',Z,'SW',6),
     ('K',K,'S',5),
     ('T',T,'N',2),
     ('E',E,'NE',2),
     ('L',L,'N',2) ]

geo.label_points(points)


# ----------------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/broken_chord9.png'
plt.savefig(ofn, dpi=300)





