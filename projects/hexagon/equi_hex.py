import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

delta = 30
A = geo.Point(20,20)
B = geo.Point(A.x+delta,A.y)
Q = geo.xcc([A,delta],[B,delta])[1]
pL = [Q,A,B]

for i in range(6):
    if i % 2:
        c = 'b'
    else:
        c = 'r'
    pL = geo.rpa(pL,Q,60)
    geo.opg(ax,pL,ec=c)
    geo.fpg(ax,pL,fc=c,alpha=0.05*(i+1))

geo.scp(ax,[Q])

geo.savefig(plt)