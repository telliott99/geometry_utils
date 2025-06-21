import sys,math
import matplotlib.pyplot as plt
import numpy as np

# contrary to best practice
# import *all* the symbols from the library
import geometry as geo
from geometry import *

fig, ax = geo.init()
ax.set(xlim=(0,150), ylim=(0,150))

'''
circle = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(circle)
'''
'''
gtr =  get_standard_triangle
scp =  scatter_points
dls =  draw_line_segment
dlss = draw_line_segments
fpg =  fill_polygon
opg =  outline_polygon
gpf =  get_point_by_fractional_length
gpp =  get_perp_at_point_by_fractional_length
gcc =  get_circumcircle
goa =  get_orthocenter_and_altitudes
gcm =  get_centroid_and_medians
gib =  get_incenter_and_bisectors
xll =  get_intersection_for_two_lines
xlc =  get_intersection_line_segment_circle
xcc =  get_intersection_circle_circle
bae =  bisect_angle_Euclid
rpa =  rotate_points_around_center_by_angle
tp =   translate_points
sct =  scale_triangle
ma =   mark_angle
mra =  mark_right_angle
rl  =  get_rectangle_for_line
'''

A = Point(5,5)
B = Point(70,5)
C = Point(80,90)

opg(ax,[A,B,C])
fpg(ax,[A,B,C])

# get the median points
cD = gcm([A,B,C])
K,L,M = cD['K'],cD['L'],cD['M']
opg(ax,[K,L,M],ec='b')

# get the incircle center and feet
iD = gib([A,B,C])
I,X,Y = iD['I'],iD['X'],iD['Z']
r = get_length([I,X])
dls(ax,[I,X],ec='gray')

incircle = plt.Circle(
    (I.x,I.y),r,fc='none',
    ec='gray',ls=':')
ax.add_patch(incircle)

# extend the sides and find the 
# excircle center
tmp = gpf([A,C],1.5)
tmp2 = bae(C,[B,tmp])
N = xll([C,tmp2],[A,I])
dls(ax,[A,N],ls=':')

# get the inversion circle on K
rho = get_length([X,K])
Xa = gpf([X,K],2.0)
dls(ax,[N,Xa],ec='gray')

inv_circle = plt.Circle(
    (K.x,K.y),rho,fc='none',ec='k',ls=':')
ax.add_patch(inv_circle)

R = get_length([Xa,N])
excircle = plt.Circle(
    (N.x,N.y),R,
    fc='none',ec='gray',ls=':')
ax.add_patch(excircle)

D,E = get_tangent_points_on_circle_for_point(
    [N,R],A)
dlss(ax,[[A,D],[A,E]])

# S is at the intersection of the tangnets
S = xll([A,N],[B,C])

# one of these should be X
rL = get_tangent_points_on_circle_for_point(
    [I,r],S)
# it is the second
T,_ = rL

# find all the speccial points
B1 = xll([S,T],[A,C])
Bp = xll([S,T],[K,L])
Cp = xll([S,T],[K,M])
C1 = xll([S,T],[A,B])
dls(ax,[B1,C1])

def do_points(s=6):
    scp(ax,[A,B,C],s=s)
    scp(ax,[K,L,M],c='b',s=s)
    scp(ax,[X,Xa],s=s)
    
    scp(ax,[I,N],s=s)
    scp(ax,[D,E],s=s)
    
    scp(ax,[B1,S,T,C1],c='r',s=s)
    scp(ax,[Bp,Cp],c='b',s=s)
    
#do_points()


# to make separate figures showing
# various similar triangles

def group1():
    fpg(ax,[Bp,L,B1],fc='r',alpha=0.3)
    fpg(ax,[Bp,K,Cp],fc='r',alpha=0.3)
    fpg(ax,[M,Cp,C1],fc='r',alpha=0.3)

def group2():
    fpg(ax,[K,Bp,S],fc='r',alpha=0.2)
    fpg(ax,[S,B,C1],fc='r',alpha=0.2)

def group3():
    fpg(ax,[I,S,X],fc='m',alpha=0.2)
    fpg(ax,[S,N,Xa],fc='m',alpha=0.2)


#group1()
#group2()
#group3()




aL = [[C,A,B],[K,M,B],[C,L,K],[L,K,M]]
mark_angles(ax,aL,d=5,c='b',s=10)

aL = [[A,C,B],[M,K,B],[B,C1,S],[K,M,L],[A,L,M],
      [K,Bp,S]]
mark_angles(ax,aL,d=5,c='r',s=8)

aL = [[A,B,C],[K,L,M],[L,M,A],[L,K,C]]
mark_angles(ax,aL,d=3,c='g',s=12)

aL = [[C,B1,S],[C,B,E],[T,Cp,M]]
mark_angles(ax,aL,d=3,c='lightgreen',s=10)

aL = [[K,Bp,B1]]
mark_angles(ax,aL,d=3,c='m',s=10)

aL = [[N,A,C],[N,A,B]]
mark_angles_open(ax,aL,d=12,c='b',s=10,ws=5)



# again, so it's on top
opg(ax,[K,L,M],ec='b')


#----------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/Feuerbach.png'
plt.savefig(ofn, dpi=300)