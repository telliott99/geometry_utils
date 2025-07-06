import sys
import matplotlib.pyplot as plt
import geometry as geo

fig,ax = geo.init()

    
B = geo.Point(50,30)
C = geo.Point(80,30)

A = geo.Point(65 ,60)
dx = C.x-B.x
dy = C.y-B.y
D = geo.Point(A.x+dx,A.y+dy)
    

E = geo.get_point_by_fractional_length(
    [C,D],1.6)
I = geo.get_intersection_for_two_lines(
        [E,A],[C,B])

dx = C.x-I.x
G = geo.Point(E.x-dx,E.y)
  

F = geo.get_intersection_for_two_lines(
        [G,E],[A,B])
H = geo.get_intersection_for_two_lines(
        [A,D],[I,G])
    
geo.opg(ax,[A,B,C,D])
geo.opg(ax,[A,H,G,F])

geo.dlss(ax,[[B,I],[H,I],[D,E],[E,F]])
geo.dls(ax,[E,I],ec='k',ls=':')

geo.fpg(ax,[A,B,C,D])
geo.fpg(ax,[A,H,G,F])

geo.scp(ax,[A,B,C,D,E,F,G,H,I])

geo.label_points(
    [['A',A,'NW',3],
     ['B',B,'NW',3],
     ['C',C,'E',2],
     ['D',D,'E',2],
     ['E',E,'N',2],
     ['F',F,'N',2],
     ['G',G,'N',2],
     ['H',H,'W',5],
     ['I',I,'W',3],
     ])


ofn = '/Users/telliott/Desktop/EI_43.png'
geo.savefig(plt,ofn=ofn)