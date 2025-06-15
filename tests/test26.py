import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

A = geo.Point(10,10)
B = geo.Point(50,10)
C = geo.Point(20,50)

#print(geo.is_above(C,[A,B]))
#print(geo.is_above(B,[A,C]))

#print(geo.is_above(C,[B,A]))
#print(geo.is_above(B,[A,C]))
