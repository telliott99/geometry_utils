import sys, random
import math
import matplotlib.pyplot as plt
import numpy as np

'''
todo:

still need to suppress axes

look into draw_line_segment
when all pairs

compute distance for marked angles
based on the actual angle!

rewrite rotation test code


'''

#---------------------------------------

# drawing code for matplotlib

def init():
    fig, (ax) = plt.subplots(
        subplot_kw = {'aspect': 'equal'})
    ax.set(xlim=(-10, 110), ylim=(-10, 110))
    return fig,ax

#---------------------------------------

'''
points are simply (x1,y1) --- not fancy objects
P = (x1,y1) etc

a line segment or a polygon is an array of points
[P,Q ... ]

so
line segment PQ = [(x1,y1),(x2,y2)] = [P,Q]

matplotlib takes separate lists of xvals,yvals
I've often used capital X and Y for lists of x or y
getXY(pL) below

we enforce two rules ...
pass lists of points to our functions

wrappers on drawing code will call getXY first thing

it seems pedantic to insist on the brackets
so for a single point we just do f(P) etc.

'''

#---------------------------------------

# our convention is to start with line segments and polygons
# as lists of tuples of (x,y)
# and then call getXY before feeding them to matplotlib

# it's important for bisection and angle routines
# to specify vertices in the same direction, CCW

def get_standard_triangle(mode='acute'):
    if mode == 'acute':
        return [(0,0),(90,0),(15,80)]
    if mode == 'right':
        return [(0,0),(100,0),(0,75)]
    if mode == 'obtuse':
        return [(30,0),(0,90),(70,0)]
    if mode == 'isosceles':
        return [(20,0),(80,0),(50,90)]
    if mode == 'equilateral':
        return [(0,0),(100,0),(50,50*3**0.5)]

# Q is a single point by itself so not [Q], not a pL

# circles made here do not retain properties passed as args
# why?
# solution for now is to treat a circle as simply a tuple
# x0,y0,r
# we will not create the "patch" object in this library

'''
def get_circle(ax,Q,r,fc='none',ec='k',ls='-',lw=1,c='k'):
    circle = plt.Circle(Q,r,fc=fc,ec=ec,ls=ls,color=c)
    ax.add_patch(circle)
    return circle
'''

# convenience function, examine the patch object

def get_matplotlib_circle_center_radius(c):
    return (c._center,c.radius)

def get_random_points(n=3):
    N = 101
    cL = list()
    for i in range(2*n):
        cL.append(random.randint(0,N))
    A = cL[0],cL[1]
    B = cL[2],cL[3]
    C = cL[4],cL[5]
    return [A,B,C]  


#---------------------------------------

# draw_one_line_segment
# draw_assorted_segments
# draw_chained_line_segments
# fill_polygon

# abbreviations
# lw linewidth
# ls linestyle - = std, : = dotted
# fc facecolor k = black
# ec edgecolor
# c color

# sensible defaults
# pL is [(x1,y1),(x2,y2) etc.

# point size SZ 
POINT_SZ = 15

# keep interface simple
# if we need more we can always call func directly

def scatter_points(ax,pL,c='k',s=POINT_SZ):
    X,Y = getXY(pL)
    ax.scatter(X,Y,s=s,c=c)
    
# ------

# this works with more than one point, draws all pairs

def draw_line_segment(ax,pL,ec='k',lw=1,ls='-'):
    X,Y = getXY(pL)
    ax.fill(X,Y,fc='none',ec=ec,lw=lw,ls=ls)

# draw separate line segments, not efficient but ...
def draw_multiple_line_segments(ax,pL,ec='k',lw=1,ls='-'):
    for P,Q in pL:
        draw_line_segment(ax,[P,Q],ec=ec,lw=lw,ls=ls)
        
# ------

def draw_chained_line_segments(ax,pL,c='k'):
    X,Y = getXY(pL)
    ax.fill(X,Y,fc='none',ec=c,lw=1,ls='-',alpha=1)     

def fill_polygon(ax,pL,c='lightsalmon',alpha=0.25):
    X,Y = getXY(pL)
    ax.fill(X,Y,fc=c,alpha=alpha)     
    
def outline_polygon(ax,pL,c='red'):
    draw_chained_line_segments(ax,pL,c=c)

#---------------------------------------

big_number = 1000000


# line segment is simply two tuples of (x,y),(x,y)
# triangle is three tuples

# assume that points not coincident

# convert a list of points into lists of x and y
# our convention is to use capital X and Y 
# for lists of xvals, yvals

# pL for point list
def getXY(pL):
    X = [x for x,y in pL]
    Y = [y for x,y in pL]
    return X,Y
    
def get_points_from_XY(X,Y):
    return [(x,y) for x,y in zip(X,Y)]

# delta x and delta y
def get_deltas(pL):
    A,B = pL
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    return dx,dy

# length of a line segment
def get_length(pL):
    # only makes sense for two points
    assert len(pL) == 2
    #print(pL)
    dx,dy = get_deltas(pL)
    if dx == 0:
        return abs(dy)
    if dy == 0:
        return abs(dx)
    return (dx**2 + dy**2)**0.5

#---------------------------------------

# slopes

# slope for a line segment
def get_slope(pL):
    assert len(pL) == 2
    dx,dy = get_deltas(pL)
    if dx == 0:
        # sys.maxsize caused error, overflow I guess
        return big_number 
    return dy/dx
    
def invert_slope(m):
    if m == 0:
        return big_number
    return -1/m

# slope of line perp to line segment
def get_perp_slope(pL):
    assert len(pL) == 2
    m = get_slope(pL)
    return invert_slope(m)

#---------------------------------------

# cut line segment at point determined by f
# bisected when f = 0.5

def get_point_by_fractional_length(pL,f):
    A,B = pL
    dx,dy = get_deltas(pL)
    return A[0] + f*dx, A[1] + f*dy


def get_point_by_absolute_length(pL,d1):
    A,B = pL
    d2 = get_length([A,B])
    f = d1/d2
    return get_point_by_fractional_length(pL,f)

# rather than y0 for a line, label intercept as k
# (k-y)/(0-x) = m
# k = y - mx

def get_intercept_for_point_slope(A,m):
    return A[1] - m*A[0]

def get_slope_intercept_for_two_points(pL):
    assert len(pL) == 2
    A,B = pL
    m = get_slope(pL)
    k = get_intercept_for_point_slope(A,m)
    return m,k
    
# find intersection of two line segments (or their extensions)
# from slope-intercept definitions

# m1*x + k1 = m2*x + k2
# (m1 - m2)*x = k2 - k1

def get_intersection_from_slope_intercept(m1,k1,m2,k2):
    x = (k2-k1)/(m1-m2)
    y = m1*x + k1
    return (x,y)

# from endpoint definitions

def get_intersection_from_two_lines(pL1,pL2):
    A,B = pL1
    P,Q = pL2
    m1,k1 = get_slope_intercept_for_two_points([A,B])
    m2,k2 = get_slope_intercept_for_two_points([P,Q])
    return get_intersection_from_slope_intercept(m1,k1,m2,k2)

#---------------------------------------

# starting from point A and line segment BC
# find point P on BC such that AP perp BC

def get_point_perp_on_line_from_point(A,pL):
    B,C = pL
    if B[0] == C[0]:
        return (B[0],A[1])
        
    if B[1] == C[1]:
        return (A[0],B[1])
        
    # get equation of BC
    m1,k1 = get_slope_intercept_for_two_points([B,C])
    m2 = invert_slope(m1)
    k2 = get_intercept_for_point_slope(A,m2)
    return get_intersection_from_slope_intercept(m1,k1,m2,k2)
    
#=======================================
#=======================================

# circumcircle

'''
we know midpoint x1,y1 i.e. R in AB and 
second midpoint x2,y2 i.e. P in BC
and slopes m1 and m2

m1 = (y-y1)/(x-x1)
m2 = (y-y2)/(x-x2)

m1(x-x1) + y1 = m2(x-x2) + y2
m1x - m2x = m1x1 - m2x2 + y2 - y1

x = [m1x1 - m2x2 + y2 - y1]/(m1-m2)

now sub for x in first equation
y = m1*x - m1*x1 + y1
'''

def get_circumcircle(pL):
    assert len(pL) == 3
    A,B,C = pL
    R = get_point_by_fractional_length([A,B],0.5)
    m1 = get_perp_slope([A,B])
    
    P = get_point_by_fractional_length([B,C],0.5)
    m2 = get_perp_slope([B,C])
    
    # see derivation above
    x = (m1*R[0] - m2*P[0] + P[1] - R[1])/(m1-m2)
    y = m1*x - m1*R[0] + R[1]
    Q = (x,y)
    r = get_length([Q,A])
    
    return (Q,r)
   
    # this approach also works
    '''
    k1 = get_intercept_for_point_slope(R,m1)
    k2 = get_intercept_for_point_slope(P,m2)
    x,y = get_cross_from_slope_intercept(m1,k1,m2,k2)
    return x,y
    '''
#---------------------------------------

# orthocenter and centroid
# P is a point on line segment opposite A, etc

def get_orthocenter_and_altitudes(pL):
    A,B,C = pL
    # perp from point to line segment left-right
    # feet of altitudes are DEF 
    
    # args are point, line segment
    D = get_point_perp_on_line_from_point(A,[B,C])
    E = get_point_perp_on_line_from_point(B,[A,C])
    F = get_point_perp_on_line_from_point(C,[A,B])
    
    H = get_intersection_from_two_lines([A,D],[B,E])
    
    # orthocenter H
    rD = { 'H':H, 'D':D, 'E':E, 'F':F }
    return rD  

def get_centroid_and_medians(pL):
    A,B,C = pL
    #print(A,B,C)
    
    K = get_point_by_fractional_length([B,C],0.5)
    L = get_point_by_fractional_length([A,C],0.5)
    M = get_point_by_fractional_length([A,B],0.5)
    G = get_intersection_from_two_lines([A,K],[B,L])

    # centroid G
    rD = { 'G':G, 'K':K, 'L':L, 'M':M }
    return rD  

#---------------------------------------

'''
# angle bisectors and incircle

# always take points counterclockwise

Let a be side opposite A and P be the point on that side
We find the correct point P on side a as follows

BP = x
PC = y
c/x = b/y

x is the distance on the same side as c, i.e. |BP|
We are looking for the fraction of the distance
|BP|/|BC| = x/a

So...
b/c = y/x
(b+c)/c = (x+y)/x = a/x

so finally
f = x/a = c/(b+c)

We find that fraction of the whole distance |AB|
and this is equal to |AR|
'''

def get_incenter_and_bisectors(pL):
    A,B,C = pL
    a = get_length([B,C])
    b = get_length([A,C])
    c = get_length([A,B])
    #print(pL)
    
    # if B,C is the line segment
    # x is the distance from B to the point P
    P = get_point_by_fractional_length([B,C],c/(c+b))
    Q = get_point_by_fractional_length([C,A],a/(a+c))
    R = get_point_by_fractional_length([A,B],b/(b+a))
        
    I = get_intersection_from_two_lines([A,P],[C,R])
    
    # points where perp from I hits sides
    X = get_point_perp_on_line_from_point(I,[B,C])
    Y = get_point_perp_on_line_from_point(I,[A,C])
    Z = get_point_perp_on_line_from_point(I,[A,B])
            
    # incenter I
    # P,Q,R are bisectors hitting sides
    # X,Y,Z are feet of perps
    rD = { 'I':I, 'P':P, 'Q':Q, 'R':R,
                  'X':X, 'Y':Y, 'Z':Z  }
    return rD  
   
#---------------------------------------

# angles

'''

u dot v = uv cos theta

but also
c^2 = a^2 + b^2 - 2ab cos C
(a^2 + b^2 - c^2)/2ab = cos C

(a^2 + c^2 - b^2)/2ac = cos B
(b^2 + c^2 - a^2)/2bc = cos A

'''

# perhaps modify this to indicate which is vertex

def get_angle(pL):
    A,B,C = pL
    #print(pL)
    a = get_length([B,C])
    b = get_length([A,C])
    c = get_length([A,B])
    
    n = b**2 + c**2 - a**2
    d = (2 * b * c)
    v = n/d
    if v < 0:
        v = -v
    mA = math.degrees(math.acos(v))
    return mA
    
def get_all_angles(pL):
    A,B,C = pL
    mA = get_angle([A,B,C])
    mB = get_angle([B,C,A])
    mC = get_angle([C,B,A])
    return mA, mB, mC
    
#=======================================
#=======================================

def get_point_reflected_on_diameter(A,cL):
    Q,r = cL
    return get_point_by_fractional_length(
        [A,Q],2.0)

def get_point_on_circle_at_distance_from_point(cL,d,A):
    Q,r = cL
    pL = get_intersection_circle_circle(cL,[A,d])
    return pL
    
def get_horizontal_intercept_for_circle_point(cL,A):
    Q,r = cL
    m = 0
    k = A[1]
    return get_intersection_point_slope_circle(k,m,cL)

#---------------------------------------

# points where 
# line meets circle
# circles cross
# tangent line meets circle

'''
intersection of line
y = mx + k

and circle on center x0,y0
(x - x0)^2 + (y - y0)^2 = r^2

sub 
(x - x0)^2 + (mx + k - y0)^2 = r^2
x^2 - 2xx0 + x0^2 + m^2x^2 + k^2 + y0^2 + 2mkx - 2mxy0 - 2ky0 = r^2

quadratic with
A = 1 + m^2
B = 2(m(k-y0) - x0)
C = x0^2 + (k-y0)^2 - r^2

# use x0,y0 to avoid confusion k
# use caps just for yuks 

solve:
np.roots([A,B,C])

'''

# to find points on a circle intersecting with 
# something else
# although we use the center and radius
# have reverted to use cL = [Q,r]

def get_intersection_point_slope_circle(m,k,cL):
    [Q,r] = cL
    x0,y0 = Q
    
    A = 1 + m**2
    B = 2*(m*(k-y0) - x0)
    C = x0**2 + (k-y0)**2 - r**2
    
    rL = np.roots([A,B,C])
    if any(np.iscomplex(rL)):
        return [],[]
    X = rL[:]
    Y = [float(m*r+k) for r in X]
    result = get_points_from_XY(X,Y)
    return result

# extend line segment if necessary
def get_intersection_line_segment_circle(pL,cL):
    [A,B] = pL
    m,k = get_slope_intercept_for_two_points(pL)
    return get_intersection_point_slope_circle(m,k,cL)

def get_intersection_circle_circle(cL1,cL2):
    (Q1,r1) = cL1
    (x1,y1) = Q1
    
    (Q2,rho) = cL2
    (x2,y2) = Q2
    
    d = get_length([Q1,Q2])
    x = (r1**2 - rho**2 + d**2)/(2*d)
    f = x/d

    # P lies on centerline
    # its perpendicular goes through points we want
    P = get_point_by_fractional_length([Q1,Q2],f)
    
    # perpendicular to Q1,Q2
    m = get_perp_slope([Q1,Q2])
    k = get_intercept_for_point_slope(P,m)    
    return get_intersection_point_slope_circle(m,k,[Q1,r1])
    
#---------------------------------------

# tangent by Euclid's method

# this is an exception to standard

# we have just 2 points and they are of different kinds
# we do *not* provide an array of points
# Q is the center of the circle and r its radius

def get_tangent_points_on_circle_from_point(cL1,P):
    [Q1,r] = cL1
    (x1,y1) = Q1

    d = get_length([P,Q1])
    
    Q2 = get_point_by_fractional_length([P,Q1],0.5)
    x2,y2 = Q2
    r2 = d/2
    cL2 = [Q2,r2]
    return get_intersection_circle_circle(cL1,cL2)

# more circle utilities

def get_chord_for_circle_from_point_with_length(ax,cL1,P,d):
    [Q,r] = cL1

    cL2 = [P,d]
    return get_intersection_circle_circle(cL1,cL2)

def find_midpoint_of_arc(pL,cL,major=True):
    [G,A] = pL
    [Q,r] = cL
    tmp = get_point_by_fractional_length(pL,0.5)
    m = get_perp_slope(pL)
    k = get_intercept_for_point_slope(tmp,m)
    
    M1,M2 = get_intersection_point_slope_circle(m,k,cL)
    M1_bigger = get_length([A,M1]) > get_length([A,M2])
    if major:
        if M1_bigger:
            return M1
        else:
            return M2
    else:
        if M1_bigger:
            return M2
        else:
            return M1

#---------------------------------------

# rotation on an arbitrary center
# caveman style, ccw rotation

# here pL is a single point
def rotate_one_point(pL,theta):
    x,y = pL
    c = math.cos(theta)
    s = math.sin(theta)
    u = c*x - s*y
    v = s*x + c*y
    return u,v
 
def rotate_point_list(pL,theta):
    rL = [rotate_one_point([x,y],theta) for x,y in pL]
    return rL

# starting from a center point Q
# normalize points to Q
# rotate by theta
# add Q back again

def rotate_points_around_center_by_angle(pL,Q,theta):
    h,k = Q
    tmp = [(x-h,y-k) for x,y in pL]
    tmp = rotate_point_list(tmp,theta)
    result = [(u+h,v+k) for u,v in tmp]
    return result

#---------------------------------------

# Archimedes "Broken Chord"

def get_broken_chord_layout(ax):
    [G,A,B] = [(20,25),(100,70),(10,70)]
    Q,r = get_circumcircle([G,A,B])

    M = find_midpoint_of_arc([G,A],[Q,r],major=True)    
    D = get_point_perp_on_line_from_point(M,[A,B])
    E = get_point_by_fractional_length([B,D],2.0)
    
    return { 'Q':Q,'r':r,'G':G,'A':A,'B':B,
             'M':M,'D':D,'E':E }

def get_broken_chord_alternate_layout(ax):
    # G,A very close together, B close to M
    G = [30,10]
    A = [70,10]
    Q = [50,50]
    r = get_length([A,Q])
    
    M = find_midpoint_of_arc([G,A],[Q,r],major=True)
    pL = get_intersection_point_slope_circle(0,70,[Q,r])
    B = pL[1]

    D = get_point_perp_on_line_from_point(M,[A,B])
    E = get_point_by_fractional_length([B,D],2.0)
    
    return { 'Q':Q,'r':r,'G':G,'A':A,'B':B,
             'M':M,'D':D,'E':E }

#---------------------------------------

def get_9point_circle(pL):
    assert len(pL) == 3
    A,B,C = pL
    P = get_point_by_fractional_length([B,C],0.5)
    Q = get_point_by_fractional_length([A,C],0.5)
    R = get_point_by_fractional_length([A,B],0.5)
    
    # 9point center N
    [N,r] = get_circumcircle([P,Q,R])
    
    rD = { 'N':N, 'r':r, 'P':P, 'Q':Q, 'R':R }
    return rD  

#---------------------------------------

# original method

def write_one_label(P,s,dx=0,dy=0):
    plt.text(P[0]+dx,P[1]+dy,s,fontstyle='italic',
        fontsize=14,fontfamily='serif')

def write_labels(L):
    for e in L:
        P,s = e[0:2]
        try:
            dx,dy = e[2:4]
            write_one_label(P,s,dx,dy)
        except ValueError:
            dx,dy = 0,0
        write_one_label(P,s,dx,dy)
        
# new approach

def nudge(P,mode='none',f=1.0):
    x,y = P
    # takes a point and nudges it in that direction
    # with a fractional adjustment
    if   mode == 'N':   y += 1.414 * f
    elif mode == 'NE':  x += 1 * f; y += 1 * f
    elif mode == 'E':   x += 1.414 * f
    elif mode == 'SE':  x += 1 * f; y -= 1 * f
    elif mode == 'S':   y -= 1.414 * f
    elif mode == 'SW':  x -= 1 * f; y -= 1 * f
    elif mode == 'W':   x -= 1.414 * f
    elif mode == 'NW':  x -= 1 * f; y += 1 * f
    return x,y

def label_points(points):
    for sL in points:
        s,P,mode,how_far = sL
        tmp = nudge(P,mode=mode,f=how_far)
        #print(tmp)
        write_one_label(tmp,s)

#---------------------------------------

# dots to show equal angles

# vertices taken CCW, the angle here is at vertex B
def mark_angle(pL,d=5):
    bD = get_incenter_and_bisectors(pL)
    [A,B,C] = pL
    line_segment = [B,bD['Q']]
    f = d/get_length(line_segment)
    dot = get_point_by_fractional_length(line_segment,f)
    return dot

def mark_angles(ax,aL,d=5,c='k',s=20):
    rL = list()
    for angle in aL:
        rL.append(mark_angle(angle,d=d))
    scatter_points(ax,rL,c=c,s=s)

