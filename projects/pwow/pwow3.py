import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import math

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))


A = geo.Point(10,10)
B = geo.Point(90,10)
m = geo.get_length([A,B])/2
M = geo.get_midpoint([A,B])
C = geo.Point(M.x,A.y+(m*math.sqrt(3)))

geo.opg(ax,[A,B,C],ec='k')

P = geo.Point(43,27)

tmp = geo.get_point_at_angle_on_circle(
    60,[P,10])
D = geo.xll([P,tmp],[A,B])
G = geo.xll([P,tmp],[B,C])

tmp = geo.get_point_at_angle_on_circle(
    120,[P,10])
H = geo.xll([P,tmp],[A,C])
E = geo.xll([P,tmp],[A,B])

tmp = geo.Point(P.x+5,P.y)
F = geo.xll([P,tmp],[B,C])
I = geo.xll([P,tmp],[A,C])

K = geo.get_midpoint([D,E])
L = geo.get_midpoint([F,G])
M = geo.get_midpoint([H,I])
N = geo.get_midpoint([H,P])
#-------------------

def show(pL):
    A,B,C = pL
    geo.fpg(ax,[A,B,C])
    geo.opg(ax,[A,B,C])
    
geo.opg(ax,[A,B,C],ec='k')
    
def basic():
    show([P,D,E])
    show([P,F,G])
    show([P,H,I])
    geo.dlss(ax,[[P,K],[P,L]],ec='b')
    geo.scp(ax,[P])

def rotate():
    show([P,D,E])
    geo.dlss(ax,[[P,K]],ec='b')

    d = geo.get_length([I,N])
    S = geo.Point(C.x,C.y-d)
    tmp = geo.Point(S.x+5,S.y)
    T = geo.xll([S,tmp],[A,C])
    U = geo.xll([S,tmp],[B,C])
    show([C,T,U])
    geo.dlss(ax,[[C,S]],ec='b')
    
    tmp = geo.Point(P.x+5,P.y)
    X = geo.xll([P,tmp],[A,C])
    
    d = geo.get_length([T,X])
    f = d/geo.get_length([X,P])
    Y = geo.get_point_by_fractional_length(
        [X,P],f)
    tmp = geo.get_midpoint([X,Y])
    
    show([T,X,Y])
    geo.dlss(ax,[[T,tmp]],ec='b')
    geo.scp(ax,[P])


#1
#basic()
#geo.dlss(ax,[[P,M]],ec='b')

#2
#geo.dlss(ax,[[I,N]],ec='b')

#3
rotate()

geo.savefig(plt)

