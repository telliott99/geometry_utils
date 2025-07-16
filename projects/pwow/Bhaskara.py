import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,110), ylim=(0,100))
'''
n = 3
a = 5*n
b = 12*n
c = 13*n
'''

a = 24
b = 32
c = 40
d = b-a

A = geo.Point(50,10)
B = geo.Point(A.x+b,A.y)
C = geo.Point(B.x,B.y+a)
D = geo.Point(A.x,A.y+a)

E = geo.Point(B.x+a,B.y)
F = geo.Point(E.x,E.y+b)
G = geo.Point(B.x,B.y+b)

H = geo.Point(G.x-d,G.y)
I = geo.Point(H.x,C.y)

geo.fpg(ax,[A,B,C,D])
geo.opg(ax,[A,B,C,D])

geo.fpg(ax,[B,E,F,G],fc='b',alpha=0.2)
geo.opg(ax,[B,E,F,G],ec='b')

geo.dlss(ax,[[B,D],[B,F]])

geo.opg(ax,[C,G,H,I])

#-----------------------

P = geo.Point(A.x-45,A.y)
Q = geo.Point(P.x+c,P.y)
R = geo.Point(Q.x,Q.y+c)
S = geo.Point(P.x,P.y+c)

T = geo.xcc([P,a],[S,b])[1]
U = geo.xcc([P,b],[Q,a])[1]
_,_,V,W = geo.get_rectangle_for_line(
        [T,U],f=1.0)

geo.opg(ax,[P,Q,R,S])

geo.opg(ax,[P,U,Q],ec='k')
geo.fpg(ax,[P,U,Q])

geo.opg(ax,[Q,V,R],ec='k')
geo.fpg(ax,[Q,V,R],fc='b',alpha=0.2)

geo.opg(ax,[R,W,S],ec='k')
geo.fpg(ax,[R,W,S])

geo.opg(ax,[S,T,P],ec='k')
geo.fpg(ax,[S,T,P],fc='b',alpha=0.2)


geo.opg(ax,[T,U,V,W])

#-----------------------

X = geo.Point(H.x,A.y-5)
Y = geo.Point(H.x,H.y+5)
geo.dls(ax,[X,Y],ls=(0,(2,4)),lw=1.3)

geo.savefig(plt)

