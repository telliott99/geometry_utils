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

geo.fpg(ax,[A,C,D,E],fc='r',alpha=0.2)
geo.fpg(ax,[C,B,F,G],fc='b',alpha=0.2)
geo.fpg(ax,[A,B,I,J],fc='g',alpha=0.2)

geo.opg(ax,[A,C,D,E],ec='r')
geo.opg(ax,[C,B,F,G],ec='b')
geo.opg(ax,[A,B,I,J],ec='g')

# dotted lines

geo.dlss(ax,[[H,D],[H,F],[H,U]],ec='k',ls=':')

tmp = geo.get_point_by_fractional_length(
    [A,R],80/geo.get_length([A,R]))
geo.dls(ax,[A,tmp],ec='r',ls=':')

tmp = geo.get_point_by_fractional_length(
    [B,S],80/geo.get_length([B,S]))
geo.dls(ax,[B,tmp],ec='b',ls=':')


geo.scp(ax,[A,B,C,D,E,F,G,H,I,J,R,S,T,U])

geo.savefig(plt)