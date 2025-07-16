import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(10,10)
B = geo.Point(70,10)
_,_,C,D = geo.get_rectangle_for_line(
    [A,B],f=1.2)
    
E = geo.get_point_by_fractional_length(
    [B,C],0.7)
    
_,_,tmp,_ = geo.get_rectangle_for_line(
    [A,E],f=0.1)
F = geo.xll([E,tmp],[C,D])


geo.opg(ax,[A,B,C,D],ec='k')
geo.fpg(ax,[A,B,E],fc='b',alpha=0.2)

geo.fpg(ax,[A,E,F])
geo.opg(ax,[A,E,F])

geo.savefig(plt)

