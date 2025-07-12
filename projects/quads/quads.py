import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))


A = geo.Point(10,20)
B = geo.Point(80,20)

_,_,C,D = geo.get_rectangle_for_line([A,B],f=0.25)    
geo.opg(ax,[A,B,C,D],ec='magenta')

A = geo.Point(40,70)
B = geo.Point(60,70)
C = geo.Point(25,99)
geo.opg(ax,[A,B,C])

D,E,F = geo.get_three_parallelograms_for_triangle(
    [A,B,C])

geo.dlss(ax,[[B,D],[D,C]],ec='g')
geo.dlss(ax,[[A,F],[F,C]],ec='b')
geo.dlss(ax,[[A,E],[B,E]],ec='r')

geo.savefig(plt)





