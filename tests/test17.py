import sys,random,math
p = '/Users/telliott/Library/CloudStorage/'
p += 'Dropbox/geometry_project'
sys.path.insert(0,p)    
import geometry as geo

import matplotlib.pyplot as plt
import numpy as np

v = len(sys.argv) > 2

# angle bisector code seemed to have subtle issues
# so here we are implement Euclid's method

fig, ax = geo.init()
ax.set(xlim=(-50,150), ylim=(-50,150))

#----------------

pL = geo.get_standard_triangle()
A,B,C = pL
geo.outline_polygon(ax,[A,B,C])

# returns more than the standard form
def bisect_angle_Euclid(A,pL):
    B,C = pL
        
    # make sure K is in [A,B], L in [A,C]
    r1 = geo.get_length([A,B])
    r2 = geo.get_length([A,C])
    r = min(r1,r2)*0.5
    
    # get equidistant points from A on AB and AC
    # if P is closer to B or C than Q is
    # returns P first 
    S = geo.get_intersection_line_segment_circle(
        [A,B],[A,r])[0]
    T = geo.get_intersection_line_segment_circle(
        [A,C],[A,r])[0] 
               
    rho = 1.5 * geo.get_length([S,T])    
    
    # in principle either point gives a good line
    U,V = geo.get_intersection_circle_circle(
        [S,rho],[T,rho])
    W = geo.get_intersection_for_two_lines([U,V],[B,C])
    return W,U,V,S,T

# this is a bit confusing
# originally used P,Q,R as points where bisectors cross sides

# but in this code for Euclid's method
# we have used S,T for points along AB and AC
# U,V for points to draw bisector
# W for intersection with BC

# Euclid's method in the library will just return P, i.e. W

W,U,V,S,T = bisect_angle_Euclid(A,[B,C])

# compare with incenter code

rD = geo.get_incenter_and_bisectors(pL)

P = rD['P']
X = rD['X']
Y = rD['Y']
Z = rD['Z']
I = rD['I']

points = [
     ('A',A,'W',8),
     ('B',B,'SE',5),
     ('C',C,'N',3),
     
     ('S',S,'S',8),
     ('T',T,'W',8),
     ('U',U,'N',2),
     ('V',V,'NW',4),
     
     ('W',W,'N',6) ]

geo.label_points(points)
geo.draw_line_segment(ax,[U,V],ls=':',ec='b')
geo.scatter_points(ax,[A,B,C,S,T,U,V,W])

if v: print('A,[B,C]',geo.get_angle(A,[B,C]))
if v: print('A,[C,W]',geo.get_angle(A,[C,W]))
if v: print('A,[W,B]',geo.get_angle(A,[W,B]))

if v: print('incenter, bisector cross at P')
if v: print('A,[B,C]',geo.get_angle(A,[B,C]))
if v: print('A,[C,P]',geo.get_angle(A,[C,P]))
if v: print('A,[P,B]',geo.get_angle(A,[P,B]))

if v: print('incenter, perpendicular X')
if v: print('A,[B,X]',geo.get_angle(A,[B,X]))
if v: print('A,[X,B]',geo.get_angle(A,[X,B]))
if v: print('A,[C,X]',geo.get_angle(A,[C,X]))
if v: print('A,[X,C]',geo.get_angle(A,[X,C]))

# X should be perp ??
if v: print('X,[A,B]',geo.get_angle(X,[A,B]))
if v: print('X,[B,A]',geo.get_angle(X,[B,A]))
if v: print('X,[A,C]',geo.get_angle(X,[A,C]))
if v: print('X,[C,A]',geo.get_angle(X,[C,A]))

# conclusion
# P looks fine
# X is not perp!

# !!!
# But AP not supposed to be perp BC
# IP is!


# I should be perp
if v:  print('X,[I,B]',geo.get_angle(X,[I,B]))
if v:  print('X,[I,C]',geo.get_angle(X,[I,C]))
if v:  print('Y,[I,A]',geo.get_angle(Y,[I,A]))
if v:  print('Y,[I,C]',geo.get_angle(Y,[I,C]))
if v:  print('Z,[I,A]',geo.get_angle(Z,[I,A]))
if v:  print('Z,[I,B]',geo.get_angle(Z,[I,B]))


'''
> p3 test_geo17.py
A,[B,C] 79.38034472384486
A,[C,W] 39.69017236192244
A,[W,B] 39.69017236192244
incenter, bisector cross at P
A,[B,C] 79.38034472384486
A,[C,P] 39.69017236192244
A,[P,B] 39.69017236192244
incenter, perpendicular X
A,[B,X] 41.039413533180145
A,[X,B] 41.039413533180145
A,[C,X] 38.34093119066474
A,[X,C] 38.34093119066474
X,[A,B] 92.11297620082529
X,[B,A] 92.11297620082529
X,[A,C] 87.88702379917473
X,[C,A] 87.88702379917473
X,[I,B] 90.00000000000001
X,[I,C] 89.99999999999997
Y,[I,A] 90.0
Y,[I,C] 90.00000000000001
Z,[I,A] 90.0
Z,[I,B] 89.99999999999999
> 
'''

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/example17.png'
plt.savefig(ofn, dpi=300)

