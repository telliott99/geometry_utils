import sys, random
import math
import matplotlib.pyplot as plt
import numpy as np

'''
todo:
look into draw_line_segment
when all pairs

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
view a line segment or a polygon as an array of points
P = (x1,y1) etc
so
line segment PQ = [(x1,y1),(x2,y2)] = [P,Q]

matplotlib takes separate lists of xvals,yvals hence
getXY(pL) below

enforce two rules then ...
pass arrays of points to our functions
wrappers on drawing code will call getXY first thing

'''

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

# our convention is to start with line segments and polygons
# as lists of tuples of (x,y)
# and then call getXY before feeding them to matplotlib

# it's important for bisection and angle routines
# to specify vertices in the same direction, CCW

def standard_triangle(mode='acute'):
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
def make_circle(ax,Q,r,fc='none',ec='k',ls='-',lw=1):
    circle = plt.Circle(Q,r,fc=fc,ec=ec,ls=ls)
    ax.add_patch(circle)
    return circle

def get_circle_center_radius(c):
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

# slopes

# slope for a line segment
def get_slope(pL):
    assert len(pL) == 2
    dx,dy = get_deltas(pL)
    if dx == 0:
        # this may cause error, other usage did
        # return sys.maxsize
        return big_number
    return dy/dx
    
def invert_slope(m):
    if m == 0:
        return big_number
    return -1/m

# slope of line perp to line segment
def get_perp_slope(pL):
    #print(pL)
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

'''
def get_point_by_absolute_length(pL,d):
    A,B = pL
    d = get_length([A,B])
    dx,dy = get_deltas(pL)
    return A[0] + dx/d, A[1] + dy/d
'''

# rather than y0 for a line, label intercept as k
# (k-y)/(0-x) = m
# k = y - mx

# exception to usual practice:
# a single point is passed as is, 
# not in an array

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
    #print(m1,k1)
    m2 = invert_slope(m1)
    k2 = get_intercept_for_point_slope(A,m2)
    return get_intersection_from_slope_intercept(m1,k1,m2,k2)
    
#---------------------------------------

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

# not sure why, but maxsize causes an error
# probably overflow in m1*R[0] or ...
# 

def get_circumcenter(pL):
    assert len(pL) == 3
    A,B,C = pL
    R = get_point_by_fractional_length([A,B],0.5)
    m1 = get_perp_slope([A,B])
    
    P = get_point_by_fractional_length([B,C],0.5)
    m2 = get_perp_slope([B,C])
    
    # see derivation above
    x = (m1*R[0] - m2*P[0] + P[1] - R[1])/(m1-m2)
    y = m1*x - m1*R[0] + R[1]
    O = (x,y)
    return O
   
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
and this equal to |AR|
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
    print(pL)
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
# rewrite these to take circle objects

def get_intersection_point_slope_circle(m,k,circle):
    Q,r = get_circle_center_radius(circle)
    
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

def get_intersection_circle_circle(c1,c2):
    O,r1 = get_circle_center_radius(c1)
    Q,r2 = get_circle_center_radius(c2)

    d = get_length([O,Q])
    x = (r1**2 - r2**2 + d**2)/(2*d)
    f = x/d

    # P lies on centerline
    # its perpendicular goes through points we want
    P = get_point_by_fractional_length([O,Q],f)
    
    # perpendicular to OQ
    m = get_perp_slope([O,Q])
    k = get_intercept_for_point_slope(P,m)
    
    # pL is a tuple of [xvals],[yvals], this case length 2
    
    return get_intersection_point_slope_circle(m,k,c1)
    
#---------------------------------------

# tangent
# Euclid's method

# this is an exception to standard
# we have just 2 points and they are of different kinds
# we do *not* provide an array of points
# Q is the center of the circle and r its radius

def get_tangent_points_on_circle_from_point(ax,c,P):
    Q,r = get_circle_center_radius(c)
    #print(P)
    d = get_length([P,Q])
    
    Q2 = get_point_by_fractional_length([P,Q],0.5)
    r2 = d/2
    
    #print(P,r2)
    c2 = make_circle(ax,P,r2)
    return get_intersection_circle_circle(c,c2)

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

# more circle utilities

def get_chord_for_circle_from_point_with_length(ax,Q,r,P,d):
    c = plt.Circle(Q,r)
    c2 = plt.Circle(P,d)
    return get_intersection_circle_circle(c,c2)

def find_midpoint_of_arc(pL,c,major=True):
    [G,A] = pL
    tmp = get_point_by_fractional_length(pL,0.5)
    m = get_perp_slope(pL)
    k = get_intercept_for_point_slope(tmp,m)
    
    M1,M2 = get_intersection_point_slope_circle(m,k,c)
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

# Archimedes "Broken Chord"

def get_broken_chord_figure(ax):
    [G,A,B] = [(20,25),(100,70),(10,70)]
    Q = get_circumcenter([G,A,B])
    r = get_length([Q,A])
    c = make_circle(ax,Q,r,lw=1.5)

    M = find_midpoint_of_arc([G,A],c,major=True)
    D = get_point_perp_on_line_from_point(M,[A,B])
    E = get_point_by_fractional_length([B,D],2.0)
    
    return { 'Q':Q,'r':r,'G':G,'A':A,'B':B,
             'M':M,'D':D,'E':E,'circle':c }

def draw_broken_chord_figure(ax):
    # we need ax to register the circle
    fD = get_broken_chord_figure(ax)
    
    G = fD['G']; A = fD['A']; B = fD['B']
    M = fD['M']; D = fD['D']; E = fD['E']
    Q = fD['Q']; r = fD['r']

    c = make_circle(ax,Q,r)
    
    # ----------------------------------------
        
    ax.add_patch(c)
    #scatter_points(ax,[G,A,B,M,D,E])
    
    draw_line_segment(ax,[A,B],lw=1.5)
    draw_line_segment(ax,[B,G],lw=1.5)
    draw_line_segment(ax,[M,D],lw=1.5)
    return fD

#---------------------------------------

def get_9point_circle(pL):
    assert len(pL) == 3
    A,B,C = pL
    P = get_point_by_fractional_length([B,C],0.5)
    Q = get_point_by_fractional_length([A,C],0.5)
    R = get_point_by_fractional_length([A,B],0.5)
    
    # 9point center N
    N = get_circumcenter([P,Q,R])
    
    rD = { 'N':N, 'P':P, 'Q':Q, 'R':R }
    return rD  

#---------------------------------------

def write_one_label(P,s,dx,dy):
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

# vertices taken CCW, the angle here is at vertex B
def mark_angle(pL,d=5):
    bD = get_incenter_and_bisectors(pL)
    [A,B,C] = pL
    line_segment = [B,bD['Q']]
    f = d/get_length(line_segment)
    dot = get_point_by_fractional_length(line_segment,f)
    return dot


