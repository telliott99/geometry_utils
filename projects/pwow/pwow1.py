import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(20,60)
B = geo.Point(20,10)
_,_,C,D = geo.get_rectangle_for_line(
    [A,B],f=math.sqrt(2))

E = geo.get_point_by_fractional_length(
    [B,C],1/math.sqrt(2))
    
geo.opg(ax,[A,B,E],ec='b')
geo.fpg(ax,[A,B,E],fc='b',alpha=0.2)

geo.opg(ax,[A,E,D],ec='k')

geo.opg(ax,[C,D,E])
geo.fpg(ax,[C,D,E])

geo.savefig(plt)

