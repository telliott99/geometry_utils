import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))


Q = geo.Point(50,50)
r = 30

# alpha = 0.3
f = 0.3

c1 = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(c1)

def get_random_point_in_circle(cL):
    Q,r = cL
    while True:
        x = np.random.randint(20,80)
        y = np.random.randint(20,80)
        if r**2 > ((x-Q.x)**2 + (y-Q.y)**2):
            break
    return geo.Point(x,y)

#P = get_random_point_in_circle([Q,r])
P = geo.Point(65,60)

# horizontal left,right
RIGHT,LEFT = geo.get_intersection_line_segment_circle(
    [P,geo.Point(P.x+5,P.y)],[Q,r])
    
# above method orders points by distance from P
# RIGHT is closer so first
    
# vertical up,down
UP,DOWN = geo.get_intersection_line_segment_circle(
    [P,geo.Point(P.x,P.y+5)],[Q,r])
    
# upper right 45 lower left
UR,LL = geo.get_intersection_line_segment_circle(
    [P,geo.Point(P.x+5,P.y+5)],[Q,r])
    
# upper left 45 lower right
LR,UL = geo.get_intersection_line_segment_circle(
    [P,geo.Point(P.x-5,P.y+5)],[Q,r])
    
#-----------------------------------

# no Q

# offset for small triangles and corners
d = 4

# central points

# R is mirror horizontal image of P
# left point of small triangle c
dx = RIGHT.x - P.x
R = geo.Point(LEFT.x+dx,P.y)

# T is mirror vertical image of P
dy = UP.y - P.y
T = geo.Point(P.x,DOWN.y+dy)

magic = math.sqrt(2)

# corner point for bHGg
# slightly right of R, down from T
S = geo.Point(R.x+d,T.y-d*magic)

#-----------------------------------

fa = 0.6

# interior point(s) first, CCW direction for all points

# special point for A
# point on circle cut by line through R with slope -1
k = geo.get_intercept_for_point_slope(R,-1)
A1 = geo.get_intersection_slope_intercept_circle(
        -1,k,[Q,r])[1]

poly_A = [R,A1,LEFT]
geo.fill_polygon(ax,poly_A,fc='orange',alpha=1.0)

poly_a = [P,RIGHT,UR]
geo.fill_polygon(ax,poly_a,fc='orange',alpha=fa)

#----------

# polygon b has a corner cut out, vertex of c
b1 = geo.Point(R.x+d,R.y-d)

# special point for b
k = geo.get_intercept_for_point_slope(R,1)
b2 = geo.get_intersection_slope_intercept_circle(
        1,k,[Q,r])[0]
        
poly_b = [S,b1,R,b2,LL]
geo.fill_polygon(ax,poly_b,fc='b',alpha=f)

B1 = geo.Point(P.x-2*d,P.y)
B2 = geo.Point(P.x-d,P.y+d)

poly_B = [R,B1,B2,UL,A1]
geo.fill_polygon(ax,poly_B,fc='b',alpha=1.0)

#----------

# sector fills for b,B

geo.fill_sector(ax,Q,r,b2,LL,fc='blue',alpha=f)
geo.fill_sector(ax,Q,r,UL,A1,fc='blue',alpha=1.0)

#----------

poly_d = [P,UP,UL]
geo.fill_polygon(ax,poly_d,fc='m',alpha=0.6)

# special point for D
k = geo.get_intercept_for_point_slope(T,1)
D1 = geo.get_intersection_slope_intercept_circle(
        1,k,[Q,r])[0]

poly_D = [T,D1,DOWN]
geo.fill_polygon(ax,poly_D,fc='m',alpha=1.0)

#----------

# sector fills for d,D

geo.fill_sector(ax,Q,r,UP,UL,fc='m',alpha=0.6)
geo.fill_sector(ax,Q,r,D1,DOWN,fc='m',alpha=1.0)

#----------

# special point for e
k = geo.get_intercept_for_point_slope(T,-1)
e1 = geo.get_intersection_slope_intercept_circle(
        -1,k,[Q,r])[0]

poly_e = [T,DOWN,e1]
geo.fill_polygon(ax,poly_e,fc='yellow',alpha=f)

poly_E = [P,UR,UP]
geo.fill_polygon(ax,poly_E,fc='yellow',alpha=1.0)

#----------

ff = 0.6

# special point for f
k = geo.get_intercept_for_point_slope(R,1)
f1 = geo.get_intersection_slope_intercept_circle(
        1,k,[Q,r])[0]
        
poly_f = [R,LEFT,f1]
geo.fill_polygon(ax,poly_f,fc='brown',alpha=ff)

poly_F = [P,LR,RIGHT]
geo.fill_polygon(ax,poly_F,fc='brown',alpha=1.0)

#----------

# sector fills for f,F

geo.fill_sector(ax,Q,r,LEFT,f1,fc='brown',alpha=ff)
geo.fill_sector(ax,Q,r,LR,RIGHT,fc='brown',alpha=1.0)

#-----------------------------------

poly_h = [P,T,e1,LR]
geo.fill_polygon(ax,poly_h,fc='gray',alpha=f)

#H1 = geo.Point(T.x-d,T.y-d)
H1 = geo.Point(T.x-d,S.y)

k = geo.get_intercept_for_point_slope(T,1)
H2 = geo.get_intersection_slope_intercept_circle(
        1,k,[Q,r])[0]

poly_H = [H1,S,LL,H2]
geo.fill_polygon(ax,poly_H,fc='gray',alpha=1.0)

#-----------------------------------

# sector fills for h,H

geo.fill_sector(ax,Q,r,e1,LR,fc='gray',alpha=f)
geo.fill_sector(ax,Q,r,LL,H2,fc='gray',alpha=1.0)

#-----------------------------------

g1 = geo.Point(R.x+2*d,R.y)
poly_g = [g1,b1,S,P]
geo.fill_polygon(ax,poly_g,fc='green',alpha=f)

poly_G = [P,S,H1,T]
geo.fill_polygon(ax,poly_G,fc='green',alpha=1.0)

#-----------------------------------

poly_c = [R,b1,g1]
geo.fill_polygon(ax,poly_c,fc='r',alpha=f)

poly_c = [P,B2,B1]
geo.fill_polygon(ax,poly_c,fc='r',alpha=1.0)

#-----------------------------------

# problem
# LL seems out of place but it is not
# there is a problem with the small triangles

geo.draw_line_segments(ax,
    [[LEFT,RIGHT],[UP,DOWN],[UL,LR],[UR,LL]],ec='w')

#-----------------------------------

geo.scatter_points(ax,[P])

#geo.scatter_points(ax,[LEFT,RIGHT,UP,DOWN])
#geo.scatter_points(ax,[UR,LL,LR,UL])
geo.write_one_label(
    Q,'+',SZ=12)


geo.savefig(plt)
