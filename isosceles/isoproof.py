import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo
import isoutils as iso

fig, ax = geo.init()
ax.set(xlim=(-5,180), ylim=(-5,100))

A = geo.Point(0,0)
B = geo.Point(40,0)
C = geo.Point(20,45)
         
K,L,M = geo.translate_points(
    [A,B,C],dx=60)

S,T,U = geo.translate_points(
    [A,B,C],dx=120)

#-------------------------------

f = iso.call_func
tL = [[A,B,C],[K,L,M],[S,T,U]]
L = [A,B,C,K,L,M,S,T,U]


def panel_a():
    f(ax,tL,geo.outline_polygon)
    f(ax,tL,geo.fill_polygon)  
    f(ax,tL,iso.mark_sides)
    f(ax,tL[1:],iso.draw_vertical)
    f(ax,tL[1:],iso.mark_top_angles)
    f(ax,tL[2:],iso.mark_base_angles)
    f(ax,tL[2:],iso.mark_right_angles)
    f(ax,tL[2:],iso.mark_bases)
    #geo.scatter_points(ax,L,s=8)
    

def panel_b():
    f(ax,tL,geo.outline_polygon)
    f(ax,tL,geo.fill_polygon)  
    f(ax,tL,iso.mark_base_angles)
    f(ax,tL[1:],iso.mark_top_angles)
    f(ax,tL[1:],iso.draw_vertical)
    f(ax,tL[2:],iso.mark_sides)
    f(ax,tL[2:],iso.mark_right_angles)
    f(ax,tL[2:],iso.mark_bases)
    #geo.scatter_points(ax,L,s=8)


def panel_c():
    pL1 = tL[0]
    pL2 = tL[1]
    
    f(ax,tL[:2],geo.outline_polygon)
    f(ax,tL[:2],geo.fill_polygon)  
    f(ax,tL[:2],iso.mark_sides)
    f(ax,tL[:2],iso.draw_vertical)

    f(ax,[tL[0]],iso.mark_right_angles)
    f(ax,[tL[1]],iso.mark_bases)
    #geo.scatter_points(ax,L[:6],s=8)


def panel_d():
    pL1 = tL[0]
    pL2 = tL[1]
    
    f(ax,tL[:2],geo.outline_polygon)
    f(ax,tL[:2],geo.fill_polygon)  
    f(ax,tL[:2],iso.mark_base_angles)
    f(ax,tL[:2],iso.draw_vertical)

    f(ax,[tL[0]],iso.mark_right_angles)
    f(ax,[tL[1]],iso.mark_bases)
    #geo.scatter_points(ax,L[:6],s=8)


panel_a()

#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/isoproof.png'
plt.savefig(ofn, dpi=300)