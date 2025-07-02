import sys,math
import geometry as geo
from geometry import np, plt

fig, ax = geo.init()

A = geo.Point(40,40)
B = geo.Point(50,50)

_,_,C,D = geo.get_parallelogram_for_line(
    [A,B],75,aspect_ratio=1.5)
    
geo.scp(ax,[A],s=20,c='r')
geo.scp(ax,[B],s=20,c='b')q
geo.scp(ax,[C],c='k')
geo.scp(ax,[D],c='lightgray')

print(C,D)


'''
geo.opg(ax,rL[:4])

geo.scp(ax,[A],s=20,c='r')
geo.scp(ax,[B],s=20,c='b')
geo.scp(ax,[S,C],c='k')
geo.scp(ax,[D],c='orange')
'''



geo.savefig(plt)



