import sys,math
import geometry as geo
from geometry import np, plt

fig, ax = geo.init()

A = geo.Point(40,40)
B = geo.Point(50,50)

C = geo.get_point_at_angle_length_for_point(
    75,geo.get_length([A,B])*1.5,A)

#_,_,C,D = geo.get_three_parallelograms_for_triangle(
    #[A,B],75,aspect_ratio=1.5)

D,E,F = geo.get_three_parallelograms_for_triangle([A,B,C])
    
geo.scp(ax,[A],s=20,c='r')
geo.scp(ax,[B],s=20,c='b')
geo.scp(ax,[C],c='k')
geo.scp(ax,[D],c='lightgray')

print(C,D)

geo.savefig(plt)



