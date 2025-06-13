import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,120), ylim=(0,100))

LB = geo.Point(10,40)
RB = geo.Point(110,40)
LT = geo.Point(10,70)
RT = geo.Point(110,70)

x0 = 20
y0 = 40
P1 = geo.Point(x0,y0)
P2 = geo.Point(P1.x+20,P1.y)

x1 = 80
y1 = 70
Q1 = geo.Point(x1,y1)
Q2 = geo.Point(Q1.x+20,Q1.y)

geo.draw_line_segments(
    ax,[[LB,RB],[LT,RT],[P1,Q1],[P2,Q2]],lw=2)

N = 5
step = 1.0/N
f = step
U,V = P1,P2

for i in range(N):
    X = geo.get_point_by_fractional_length([P1,Q1],f)
    Y = geo.get_point_by_fractional_length([P2,Q2],f)
    f += step
    
    if i < N-1:
        geo.draw_line_segment(
            ax,[X,Y],ec='r',ls=':',lw=2)
        
    if i % 2 == 0:
        geo.fill_polygon(
            ax,[U,V,Y,X],alpha=0.2)
    U,V = X,Y


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/problem.png'
plt.savefig(ofn, dpi=300)