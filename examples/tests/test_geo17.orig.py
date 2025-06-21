import sys
import matplotlib.pyplot as plt
import numpy as np
import random
import geometry as geo

v = len(sys.argv) > 2

# random testing of geo.get_all_angles
# shows it's good
# angle bisector code has subtle issues
# so here we are debugging the latter

fig, ax = geo.init()
ax.set(xlim=(-10,100), ylim=(-10,100))

pL = geo.get_standard_triangle()
A,B,C = pL
geo.outline_polygon(ax,[A,B,C])

rD = geo.get_incenter_and_bisectors(pL)

# rD has PQR for bisectors and XYZ for perps
P = rD['P']
X = rD['X']

if v: print('A,[B,C]',geo.get_angle(A,[B,C]))
if v: print('A,[C,P]',geo.get_angle(A,[C,P]))
if v: print('A,[P,B]',geo.get_angle(A,[P,B]))

if v: print('A,[C,X]',geo.get_angle(A,[C,X]))
if v: print('A,[X,B]',geo.get_angle(A,[X,B]))

if v: print('X,[A,B]',geo.get_angle(X,[A,B]))

geo.scatter_points(ax,[A,B,C,X,P])

points = [
     ('A',A,'SW',6),
     ('B',B,'S',5),
     ('C',C,'N',2),
     ('P',P,'NE',2),
     ('X',X,'N',2) ]

geo.label_points(points)


#----------

#plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/example17.png'
plt.savefig(ofn, dpi=300)

'''
> p3 test_geo17.py                                                 
A,[B,C] 79.38034472384486
A,[C,P] 39.69017236192244
A,[P,B] 39.69017236192244
A,[C,X] 38.34093119066474
A,[X,B] 41.039413533180145

# this should be 90 but it's not
X,[A,B] 87.88702379917471
>
'''