import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(-10,120), ylim=(-50,130))

A = geo.Point(20,50)
B = geo.Point(90,50)
C = geo.Point(40,65)

geo.opg(ax,[A,B,C],ec='k')

_,_,D,E = geo.get_rectangle_for_line(
    [A,C],f=1.0)
geo.opg(ax,[A,C,D,E])
geo.fpg(ax,[A,C,D,E])

_,_,F,G = geo.get_rectangle_for_line(
    [C,B],f=1.0)
geo.opg(ax,[C,B,F,G])
geo.fpg(ax,[C,B,F,G])

geo.fpg(ax,[C,D,G],fc='b',alpha=0.2)
geo.dls(ax,[D,G])

#---------------

def part2():

    H = geo.get_diagonal_for_point_diagonal(
        C,[A,B])
    geo.opg(ax,[A,C,B,H])
    
    geo.dls(ax,[C,H],ec='k',ls=(0,(2,5)))
    
    _,_,I,J = geo.get_rectangle_for_line(
        [H,A],f=1.0)
    geo.opg(ax,[H,A,I,J])
    geo.fpg(ax,[H,A,I,J])
    
    _,_,K,L = geo.get_rectangle_for_line(
        [B,H],f=1.0)
    geo.opg(ax,[B,H,K,L])
    geo.fpg(ax,[B,H,K,L])
    
    geo.dls(ax,[J,K],ec='b')

    geo.fpg(ax,[A,H,C],fc='b',alpha=0.2)
    geo.fpg(ax,[H,J,K],fc='b',alpha=0.2)



part2()

geo.savefig(plt)

