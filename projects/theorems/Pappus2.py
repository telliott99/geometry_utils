import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(-20,120), ylim=(-50,150))

pL = geo.get_standard_triangle()
pL = geo.scale_triangle(pL,f=0.8)
A,B,C = pL
B = geo.nudge(B,'E',10)

#_,_,D,E = geo.get_parallelogram_for_line(
          #[A,C],70,aspect_ratio=0.5)
          
_,_,D,E = geo.get_pgram_for_angle_length_base(
    170,20,[A,C])

#_,_,F,G = geo.get_parallelogram_for_line(
          #[C,B],310,aspect_ratio=0.25)

_,_,F,G = geo.get_pgram_for_angle_length_base(
    70,30,[C,B])

H = geo.get_intersection_for_two_lines([D,E],[F,G])
T = geo.get_intersection_for_two_lines([H,C],[A,B])

tmp = geo.get_point_parallel_to_line_for_point([H,T],A)
R = geo.get_intersection_for_two_lines([A,tmp],[D,E])
J = geo.get_point_by_fractional_length([R,A],2.0)

tmp = geo.get_point_parallel_to_line_for_point([H,T],B)
S = geo.get_intersection_for_two_lines([B,tmp],[F,G])
I = geo.get_point_by_fractional_length([S,B],2.0)

U = geo.get_intersection_for_two_lines([H,T],[J,I])

geo.opg(ax,[A,B,C],ec='k')

def panel1():
    geo.opg(ax,[A,C,D,E],ec='r')
    geo.opg(ax,[C,B,F,G],ec='b')
    geo.fpg(ax,[A,C,D,E],fc='r',alpha=0.2)
    geo.fpg(ax,[C,B,F,G],fc='b',alpha=0.2)
    
    geo.dlss(ax,[[D,H],[F,H]],ls=':')

def panel2():
    geo.opg(ax,[A,C,D,E],ec='r',ls=':')
    geo.opg(ax,[C,B,F,G],ec='b',ls=':')
    geo.opg(ax,[A,R,H,C],ec='r')
    geo.opg(ax,[C,H,S,B],ec='b') 
    geo.fpg(ax,[A,R,H,C],fc='r',alpha=0.2)
    geo.fpg(ax,[C,H,S,B],fc='b',alpha=0.2)

def panel3():
    geo.opg(ax,[A,R,H,C],ec='r',ls=':')
    geo.opg(ax,[C,H,S,B],ec='b',ls=':')
    geo.opg(ax,[A,C,T,J],ec='r')
    geo.opg(ax,[B,C,T,I],ec='b')    
    geo.fpg(ax,[A,C,T,J],fc='r',alpha=0.2)
    geo.fpg(ax,[B,C,T,I],fc='b',alpha=0.2)

def panel4():
    geo.opg(ax,[A,C,T,J],ec='r',ls=':')
    geo.opg(ax,[B,C,T,I],ec='b',ls=':')    
    geo.opg(ax,[A,T,U,J],ec='r')
    geo.opg(ax,[T,B,I,U],ec='b')
    geo.fpg(ax,[A,T,U,J],fc='r',alpha=0.2)
    geo.fpg(ax,[T,B,I,U],fc='b',alpha=0.2)
    

#panel1()
#panel2()
#panel3()
panel4()

geo.savefig(plt)