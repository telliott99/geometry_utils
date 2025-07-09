import sys, random
import math
import matplotlib.pyplot as plt
import numpy as np

'''
todo:

compute distance to mark equal angles
based on the actual angle!

place point labels automatically

bugs:

matplotlib bug:
linestyles don't look the same w/different angles

'''

#=======================================

# initialization code for matplotlib
# savefig

def init():
    fig, (ax) = plt.subplots(
        subplot_kw = {'aspect': 'equal'})
    ax.set(xlim=(-10, 110), ylim=(-10, 110))
    return fig,ax

def savefig(plt,ofn=None):  
    plt.gca().set_axis_off()
    module = sys.argv[0]
    name = module.split('/')[-1].split('.')[0]
    path = '/Users/telliott/Desktop/'
    if name.startswith('test'):
        number = str(int(name[4:]))
        ofn = path + 'ex' + number + '.png'
    else:
        ofn = path + name + '.png'
    print('save', name, 'as ', ofn)
    plt.savefig(ofn, dpi=300)

def get_path():
    return sys.path[0]


#=======================================

# Point is the only *class* defined in this library

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        s = '%3.3f,%3.3f' % (self.x,self.y)
        return s

origin = Point(0,0)

def get_random_points(n=3,N=100):
    # rL is a point list
    # called r for return or retvals
    rL = list()
    for i in range(n):
        x = random.randint(0,N)
        y = random.randint(0,N)
        rL.append(Point(x,y))
    return rL

'''

# we deal with lists of Point objects, usually labeled pL
# a pL may be empty or contain only a single Point

# I tried to enforce a rule that
# isolated single Points should always be in a point list pL
# but it's too weird

# we need to check if a result is not a list of expected length

in general, a line segment or a polygon is an array of Points
[P,Q ... ]

so
line segment PQ = [P,Q]

matplotlib takes separate lists of xvals,yvals
I've often used capital X and Y for lists of x or y
getXY(pL) below

wrappers on drawing code will call getXY to get xvals,yvals

we also have a convention about direction
always CCW

it's important for bisection and angle routines
to specify vertices in the same direction, CCW

also, ordering points on a circle
'''


#=======================================

# polygon constructions

def get_standard_triangle(mode='acute'):
    A = Point(10,10)
    B = Point(90,10)
    C = Point(25,90)
    D = Point(100,10)
    E = Point(10,75)
    F = Point(30,0)
    G = Point(0,90)
    H = Point(50,90)
    J = Point(70,0)
    K = Point(90,10)
    if mode == 'acute':
        return A,B,C
    if mode == 'right':
        return A,D,E
    if mode == 'obtuse':
        return F,G,Point(90,0)
    if mode == 'isosceles':
        return Point(10,0),Point(90,0),Point(50,80)
    if mode == 'equilateral':
        return A,K,Point(50,50*3**0.5)

# construct a rectangle on a line segment
# "above" [A,B]

def get_rectangle_for_line(pL,aspect_ratio=1.0):
    A,B = pL
    base = get_length([A,B])
    height = aspect_ratio*base
    
    # construct perp of arbitrary length at B
    # S should be "above" AB
    
    # but it is not when B,A is arg
    S,T = get_perp_at_point_by_fractional_length(
        [A,B],f=1.0)
    if not point_is_above_line(S,[A,B]):
        S,T = T,S
        
    f = height/get_length([B,S])
    C = get_point_by_fractional_length([B,S],f)
    
    # do the same at A
    # U should be "above" AB
    
    U,V = get_perp_at_point_by_fractional_length(
        [A,B],f=0)
    if not point_is_above_line(U,[A,B]):
        U,V = V,U

    f = height/get_length([A,U]) 
    D = get_point_by_fractional_length([A,U],f)
    return A,B,C,D


#=======================================

# construct a parallelogram on a line segment


# get 4th point for pgram 
def get_pgram_point_for_point_diagonal(P,pL):
    M = get_midpoint(pL)
    return get_point_by_fractional_length([P,M],2.0)
     
    
# rather than adjust for orientation
# theta is angle at A wrt x-axis

def get_pgram_for_angle_length_base(theta,d,pL):
    A,B = pL
    C = get_point_at_angle_length_for_point(theta,d,A)
    D = get_pgram_point_for_point_diagonal(A,[B,C])
    return A,B,D,C

def get_three_parallelograms_for_triangle(pL):
    A,B,C = pL
    D = get_pgram_point_for_point_diagonal(A,[B,C])
    E = get_pgram_point_for_point_diagonal(C,[A,B])
    F = get_pgram_point_for_point_diagonal(B,[C,A])
    return D,E,F

#=======================================

# go to circumcircle for ABC through A at slope m
# this gives two points, one of which is A
# so we return the other one

def get_point_for_cyclic_quadrilateral(P,pL,m=1.0):
    A = P
    B,C = pL
    Q,r = get_circumcircle([A,B,C])
    circle = plt.Circle(
        (Q.x,Q.y),r,fc='none',ec='k')
    
    k = get_intercept_for_point_slope(A,m)
    
    # one point should be A itself
    rL = get_intersection_slope_intercept_circle(
        m,k,[Q,r])
        
    if points_are_close(rL[0],A):
        return rL[1]    
    return rL[0]

#=======================================

# using O here for circle center
# Richmond's construction

def get_pentagon(O,r):

    # get its diameter
    A,L = get_horizontal_intercept_for_circle_point(
        [O,r],O)
        
    # find the point at the top
    S = Point(O.x,O.y+r)
    
    # so as to bisect that radius
    P = get_point_by_fractional_length([O,S],0.5)
    
    # the key construct, bisect < APO
    tmp = bisect_angle_Euclid(P,[O,A])
    
    # find where the bisector cuts the diameter
    Q = get_intersection_for_two_lines([P,tmp],[A,O])
    
    # go up/down vertically to find points of the pentagon
    B,E = get_intersection_line_segment_circle(
        [Q,Point(Q.x,Q.y+10)]
        ,[O,r])
    
    # we want a right angle at P
    tmp = get_perp_at_point_by_fractional_length(
        [Q,P],1.0)
    
    # find where it intersects with the diameter
    R = get_intersection_for_two_lines(tmp,[A,O])
    
    # we want a vertical through R
    tmp = Point(R.x,R.y+10)
    D,C = get_intersection_line_segment_circle([R,tmp],[O,r])
    
    rD = {'vertices':[A,B,C,D,E],
          'extras':[L,P,Q,R,S] }

    return rD

#=======================================


'''
abbreviations
lw linewidth
ls linestyle, std is '-', dotted is ':'
fc facecolor, 'k' is black
ec edgecolor
c color

note: linestyle is really
(0,(2,4))
where 0 is offset, 2 is length of line, 4 is length of space

'''

# standard point size SZ 
POINT_SZ = 8

# keep interface simple
# if we need to we can always call matplotlib directly

def scatter_points(ax,pL,c='k',s=POINT_SZ):
    X,Y = getXY(pL)
    ax.scatter(X,Y,s=s,c=c)
    
# ------

# this works with more than one point, draws all pairs

def draw_line_segment(ax,pL,ec='k',lw=1,ls='-',alpha=1.0):
    X,Y = getXY(pL)
    ax.fill(X,Y,fc='none',ec=ec,lw=lw,ls=ls,alpha=alpha)

# draw separate line segments, not efficient but ...
def draw_line_segments(ax,pL,ec='k',lw=1,ls='-'):
    for P,Q in pL:
        draw_line_segment(ax,[P,Q],ec=ec,lw=lw,ls=ls)
        
# ------

def draw_chained_line_segments(ax,pL,ec='k',lw=1):
    X,Y = getXY(pL)
    ax.fill(X,Y,fc='none',ec=ec,lw=lw,ls='-',alpha=1)     

def fill_polygon(ax,pL,fc='r',alpha=0.10):
    X,Y = getXY(pL)
    ax.fill(X,Y,fc=fc,alpha=alpha)     
    
def outline_polygon(ax,pL,ec='red',lw=1):
    draw_chained_line_segments(ax,pL,ec=ec,lw=lw)


#=======================================


# to give slope near enough to straight up
big_number = 1000000

# we assume that points are unique

# convert a list of points into lists of x and y
# our convention is to use capital X and Y 
# for lists of xvals, yvals

# pL for point list
def getXY(pL):
    X = [P.x for P in pL]
    Y = [P.y for P in pL]
    return X,Y
    
def get_points_for_XY(X,Y):
    return [Point(x,y) for x,y in zip(X,Y)]

# delta x and delta y
def get_deltas(pL):
    # only makes sense for two points
    assert len(pL) == 2
    A,B = pL
    dx = B.x - A.x
    dy = B.y - A.y
    return dx,dy

# length of a line segment
def get_length(pL):
    # only makes sense for two points
    assert len(pL) == 2
    dx,dy = get_deltas(pL)
    if dx == 0:
        return abs(dy)
    if dy == 0:
        return abs(dx)
    return (dx**2 + dy**2)**0.5
    
def points_are_close(A,B):
    e = 1e-3
    dx,dy = get_deltas([A,B])
    if dx < e and dy < e:
        return True
    return False


#=======================================

# slopes
# slope for a line segment

def get_slope_for_two_points(pL):
    assert len(pL) == 2
    dx,dy = get_deltas(pL)
    if dx == 0:
        # sys.maxsize caused error, probably for overflow
        return big_number 
    return dy/dx
    
def invert_slope(m):
    if m == 0:
        return big_number
    return -1/m

# slope of line perp to line segment

def get_perp_slope(pL):
    assert len(pL) == 2
    m = get_slope_for_two_points(pL)
    return invert_slope(m)

#---------------------------------------

# cut line segment at point determined by f
# bisected when f = 0.5

def get_point_by_fractional_length(pL,f):
    A,B = pL
    dx,dy = get_deltas([A,B])
    return Point(A.x + f*dx, A.y + f*dy)

def get_midpoint(pL):
    return get_point_by_fractional_length(pL,0.5)

# original code worked sometimes, but it failed b/c
# it goes in the wrong direction depending on orientation of points

# one workaround is to calculate f = d/get_length([A,B])
# and then do get_point_by_fractional_length(pL,f)
# as long as A ne B then get_length is not 0

def get_point_by_length(pL,d):
    A,B = pL
    f = d/get_length([A,B])
    return get_point_by_fractional_length([A,B],f)

#=======================================

 
# rather use label y0, intercept is k so
# (k-y)/(0-x) = m
# k = y - mx

def get_intercept_for_point_slope(A,m):
    return A.y - m*A.x

def get_slope_intercept_for_two_points(pL):
    assert len(pL) == 2
    [A,B] = pL
    m = get_slope_for_two_points(pL)
    k = get_intercept_for_point_slope(A,m)
    return m,k

# find intersection of two line segments (or their extensions)
# for slope-intercept definitions

# m1*x + k1 = m2*x + k2
# (m1 - m2)*x = k2 - k1

def get_intersection_for_two_slope_intercepts(m1,k1,m2,k2):
    # this is problematic for parallel or identity, either way
    if m1 == m2:
        return []
    x = (k2-k1)/(m1-m2)
    y = m1*x + k1
    return Point(x,y)

# for endpoint definitions

def get_intersection_for_two_lines(pL1,pL2):
    A,B = pL1
    P,Q = pL2
    m1,k1 = get_slope_intercept_for_two_points([A,B])
    m2,k2 = get_slope_intercept_for_two_points([P,Q])
    return get_intersection_for_two_slope_intercepts(m1,k1,m2,k2)
    

def get_point_parallel_to_line_for_point(pL,A):
    m = get_slope_for_two_points(pL)
    delta = 10
    P = Point(A.x+delta,A.y+(m*delta))
    return P

#---------------------------------------

# starting with point A and line segment BC
# find point P on BC *or its extension*, such that AP perp BC
# A may not be *on* BC


def get_perp_on_line_for_point(pL,A):
    B,C = pL
    # [B,C] vertical
    if B.x == C.x:
        return Point(B.x,A.y)
        
    # [B,C] horizontal
    if B.y == C.y:
        return Point(A.x,B.y)
        
    # get equation of BC
    m1,k1 = get_slope_intercept_for_two_points([B,C])
    
    # slope and intercept for line through A perp to BC
    m2 = invert_slope(m1)
    k2 = get_intercept_for_point_slope(A,m2)
    
    rL = get_intersection_for_two_slope_intercepts(
        m1,k1,m2,k2)
        
    return rL

# Euclid's method, below, works fine as well

#---------------------------------------

# these need more testing

# ordering points
# implementing CCW test
  
def point_is_above_line(P,pL):
    A,B = pL
    phi = get_angle_for_point_on_center(B,A)
    #print('phi',phi)
    theta = get_angle_for_point_on_center(P,A)
    #print('theta',theta)
    #if (theta-phi) < 180:
    if phi <= theta <= (180 + phi) % 360:
        return True
    return False

def CCW_point_first(pL,rL):
    assert len(rL) == 2
    p,q = rL
    if point_is_above_line(p,pL):
        return p,q  
    return q,p

#---------------------------------------

def order_points_by_distance_from_point(pL,point=origin):
    if len(pL) < 2:
        return pL
    assert len(pL) == 2
    
    P,Q = pL
    
    dP = get_length([point,P])
    dQ = get_length([point,Q])
    
    if dP <= dQ:
        return P,Q
    return Q,P

#---------------------------------------

'''

construct perp at fraction f of line segment
(even outside of line segment)

length is arbitrary, caller should adjust later

get_perp_at_point_by_fractional_length

this is the first method which returns two points

which might have been returned in reverse order
so how to order them?

- by distance from the origin
- by distance from one or the other end of a line segment
- by being "above" or "below" a line segment

'''

# this seems to work well

# we use get_angle_for_point_on_center
# to return the "top" point

def get_perp_at_point_by_fractional_length(pL,f=0.5):
    A,B = pL
    
    # we need f large enough that circles cross
    if f < 0.5:
        A,B = B,A
        f = 1.0 - f 
               
    #P = get_point_by_fractional_length([A,B],f)
    Q = get_point_by_fractional_length([A,B],2*f)
    r = get_length([A,B]) * 1.2 * f
    rL = get_intersection_circle_circle([A,r],[Q,r])
    
    S,T = rL
    
    # with reference to unswitched points
    
    # get original values
    A,B = pL
    phi = get_angle_for_point_on_center(B,A)
    theta = get_angle_for_point_on_center(S,A)
    if (theta-phi) < 180:
        return S,T
    
    return T,S


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
    # remember, we even wrap single points in a list
    R = get_point_by_fractional_length([A,B],0.5)
    m1 = get_perp_slope([A,B])
    
    P = get_point_by_fractional_length([B,C],0.5)
    m2 = get_perp_slope([B,C])
    
    # see derivation above
    x = (m1*R.x - m2*P.x + P.y - R.y)/(m1-m2)
    y = m1*x - m1*R.x + R.y
    Q = Point(x,y)
    r = get_length([Q,A])
    
    return Q,r
   
    # this approach also works
    '''
    k1 = get_intercept_for_point_slope(R,m1)
    k2 = get_intercept_for_point_slope(P,m2)
    x,y = get_intersection_for_two_slope_intercepts(m1,k1,m2,k2)
    return x,y
    '''
#---------------------------------------

# orthocenter and centroid
# P is a point on line segment opposite A, etc

def get_orthocenter_and_altitudes(pL):
    A,B,C = pL
    # perp for point to line segment left-right
    # feet of altitudes are DEF 
    
    # args are point, line segment
    D = get_perp_on_line_for_point([B,C],A)
    E = get_perp_on_line_for_point([A,C],B)
    F = get_perp_on_line_for_point([A,B],C)
    
    H = get_intersection_for_two_lines([A,D],[B,E])
    
    # orthocenter H
    rD = { 'H':H, 'D':D, 'E':E, 'F':F }
    return rD  

def get_centroid_and_medians(pL):
    A,B,C = pL
    
    K = get_point_by_fractional_length([B,C],0.5)
    L = get_point_by_fractional_length([A,C],0.5)
    M = get_point_by_fractional_length([A,B],0.5)
    G = get_intersection_for_two_lines([A,K],[B,L])

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

Then finally
f = x/a = c/(b+c)

We find that fraction of the whole distance |AB|
and this is equal to |AR|
'''

def get_incenter_and_bisectors(pL):
    A,B,C = pL
    a = get_length([B,C])
    b = get_length([A,C])
    c = get_length([A,B])
    
    # if B,C is the line segment
    # x is the distance from B to the point P
    P = get_point_by_fractional_length([B,C],c/(c+b))
    Q = get_point_by_fractional_length([C,A],a/(a+c))
    R = get_point_by_fractional_length([A,B],b/(b+a))
        
    I = get_intersection_for_two_lines([A,P],[C,R])
    
    # points where perp from I hits sides
    X = get_perp_on_line_for_point([B,C],I)
    Y = get_perp_on_line_for_point([A,C],I)
    Z = get_perp_on_line_for_point([A,B],I)
            
    # incenter I
    # P,Q,R are bisectors hitting sides
    # X,Y,Z are feet of perps
    rD = { 'I':I, 'P':P, 'Q':Q, 'R':R,
                  'X':X, 'Y':Y, 'Z':Z  }
    return rD  
   
#=======================================

# points where 
# line meets circle
# circles cross
# tangent line meets circle

'''
derivation:

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
# use caps just to retain standard letters but still distinguish 

solve:
np.roots([A,B,C])

'''

# use cL = [Q,r]
# for line segment and circle, solve derivation above

# note this fails for v.large slopes and v.negative intercepts

# order by point closest to origin
def get_intersection_slope_intercept_circle(m,k,cL):
    Q,r = cL
    x0,y0 = Q.x,Q.y
        
    A = 1 + m**2
    B = 2*(m*(k-y0) - x0)
    C = x0**2 + (k-y0)**2 - r**2
    
    roots = np.roots([A,B,C])    
    if any(np.iscomplex(roots)):
        return []
        
    X = roots[:]
    Y = [float(m*r+k) for r in X]
    
    rL = get_points_for_XY(X,Y)

    # order by point closest to origin
    rL = order_points_by_distance_from_point(
        rL,point=origin)
         
    return rL


#---------------------------------------


# extend line segment if necessary
# need to check for cases where there is no intersection


# order by point closest to "left" end of line segment
def get_intersection_line_segment_circle(pL,cL,mode='left'):
    A,B = pL
    m,k = get_slope_intercept_for_two_points(pL)
    # P,Q on line segment, *or its extension*
    # how to distinguish
    rL = get_intersection_slope_intercept_circle(m,k,cL)
    
    if mode == 'left':
        point = A
    elif mode == 'right':
        point = B
    else:
        point = origin
        
    rL = order_points_by_distance_from_point(
        rL,point=A)
    return rL

# order by point closest to origin
def get_intersection_circle_circle(cL1,cL2):
    Q1,r1 = cL1
    #(x1,y1) = Q1
    
    Q2,rho = cL2
    #(x2,y2) = Q2
    
    d = get_length([Q1,Q2])
    x = (r1**2 - rho**2 + d**2)/(2*d)
    f = x/d

    # P lies on centerline
    # its perpendicular goes through points we want
    P = get_point_by_fractional_length([Q1,Q2],f)
    
    # perpendicular to Q1,Q2
    m = get_perp_slope([Q1,Q2])
    k = get_intercept_for_point_slope(P,m)    
    
    rL = get_intersection_slope_intercept_circle(m,k,[Q1,r1])

    if len(rL) < 2:
        return rL
    rL = order_points_by_distance_from_point(rL,point=origin)
        
    return rL
    

#=======================================

# tangent by Euclid's method

def get_tangent_points_on_circle_for_point(cL1,P):
    # given cicrcle on Q1
    Q1,r1 = cL1
    # distance from P to center Q1
    d = get_length([P,Q1])
    
    # bisect and construct second circle w/radius d/2
    Q2 = get_point_by_fractional_length([P,Q1],0.5)
    r2 = d/2
    cL2 = [Q2,r2]
    
    rL = get_intersection_circle_circle(cL1,cL2)
    
    return CCW_point_first([P,Q1],rL)
    

#=======================================

# more circle utilities

def get_chord_for_point_on_circle_with_length(cL,P,d):
    Q,r = cL

    cL2 = [P,d]
    return get_intersection_circle_circle(cL,cL2)

def find_midpoint_of_arc(pL,cL,major=True):
    G,A = pL
    Q,r = cL
    
    # bisect the chord AG
    tmp = get_point_by_fractional_length(pL,0.5)
    
    # erect perp
    m = get_perp_slope(pL)
    k = get_intercept_for_point_slope(tmp,m)
    
    M1,M2 = get_intersection_slope_intercept_circle(m,k,cL)
    
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


def get_point_reflected_on_diameter(A,cL):
    Q,r = cL
    return get_point_by_fractional_length(
        [A,Q],2.0)

def get_point_on_circle_at_distance_for_point(cL,d,A):
    Q,r = cL
    rL = get_intersection_circle_circle(cL,[A,d])  
    return CCW_point_first([A,Q],rL)
    
def get_horizontal_intercept_for_circle_point(cL,A):
    Q,r = cL
    m = 0
    k = A.y
    U,V = get_intersection_slope_intercept_circle(m,k,cL)
    if U.x < V.x:
        return U,V
    return V,U

def get_vertical_intercept_for_circle_point(cL,A):
    Q,r = cL
    
    #m = big_number
    #k = get_intercept_for_point_slope(A,m)
    
    # the call to get_intersection... gets complex roots
    # so the whole idea fails
    #pL = get_intersection_slope_intercept_circle(m,k,cL)
    
    
    # better to just compute y
    x = A.x
    y = math.sqrt(r**2 - x**2)
    B = Point(A.x,Q.y+y)
    C = Point(A.x,Q.y-y)
    
    return C,B

#=======================================

# angles

'''
law of cosines

u dot v = uv cos theta

but also
c^2 = a^2 + b^2 - 2ab cos C
(a^2 + b^2 - c^2)/2ab = cos C

(a^2 + c^2 - b^2)/2ac = cos B
(b^2 + c^2 - a^2)/2bc = cos A

'''

# vertex comes first to help keep things straight
# A is the vertex, pL has other two points


def get_angle(A,pL):
    B,C = pL
    a = get_length([B,C])
    b = get_length([A,C])
    c = get_length([A,B])
    
    n = b**2 + c**2 - a**2
    d = (2 * b * c)
    v = n/d
    
    mA = math.degrees(math.acos(v))
    return mA
    
def get_all_angles(pL):
    A,B,C = pL
    mA = get_angle(A,[B,C])
    mB = get_angle(B,[C,A])
    mC = get_angle(C,[A,B])
    return mA, mB, 
# this works well


#=======================================


'''
I liked the idea of using
get_intersection_line_segment_circle

but we must understand which point is returned first
sometimes we grab the wrong one.

This code circumvents the problem.
'''

def bisect_angle_Euclid(A,pL):
    B,C = pL
        
    # make sure K is in [A,B], L in [A,C]
    r1 = get_length([A,B])
    r2 = get_length([A,C])
    
    # distance to point on bisector is arbitrary
    # we adjust this below
    
    r = min(r1,r2)*0.3
    
    # get equidistant points from A on AB and AC
        
    '''
    K = get_intersection_line_segment_circle(
        [A,B],[A,r])[0]
    L = get_intersection_line_segment_circle(
        [A,C],[A,r])[0]
    print('K',K,'L',L)
    '''
    
    # alternatively get point distance r away from A
    d = r
    
    K = get_point_by_fractional_length(
        [A,B],d/get_length([A,B]))
    L = get_point_by_fractional_length(
        [A,C],d/get_length([A,C]))
          
    '''     
    rho = 1.5 * get_length([K,L]) 
        
    # in principle either point gives a good line
    P,Q = get_intersection_circle_circle(
        [K,rho],[L,rho])
    R = get_intersection_for_two_lines([P,Q],[B,C])
    '''
    
    # rather than true Euclid just do this
    M = get_point_by_fractional_length([K,L],0.5)
    
    # point on bisector where it crosses opposing side
    R = get_intersection_for_two_lines([A,M],[B,C])
    # note: R is a Point object
    return R

#=======================================

# caveman style, ccw rotation

# here P is a single point
# theta in degrees

# rotation around the origin

def rotate_one_point(P,theta):
    x,y = P.x,P.y
    c = math.cos(math.radians(theta))
    s = math.sin(math.radians(theta))
    u = c*x - s*y
    v = s*x + c*y
    return Point(u,v)
 
def rotate_point_list(pL,theta):
    return [rotate_one_point(P,theta) for P in pL]

# rotation on an arbitrary center

# starting for a center point Q
# normalize points to Q
# rotate by theta
# add Q back again

# theta in degrees

def rotate_points_around_center_by_angle(pL,Q,theta):
    h,k = Q.x,Q.y
    pL2 = [Point(P.x-h,P.y-k) for P in pL]
    pL3 = rotate_point_list(pL2,theta)
    rL = [Point(P.x+h,P.y+k) for P in pL3]
    return rL

def translate_points(pL,dx=0,dy=0):
    rL = []
    for p in pL:
        rL.append(Point(p.x+dx,p.y+dy))
    return rL

def mirror_points(pL,mL,mode='horizontal'):
    rL = []
    d = 10
    assert len(mL) > 0
    if len(mL) == 1:
        M = mL[0]
        if mode == 'horizontal':
           #i.e. mirror left-right
           N = Point(M.x,M.y+d)
        elif mode == 'vertical':
           #i.e. mirror up,down
           N = Point(M.x+10,M.y)
    else:
        assert len(mL) == 2
        M,N = mL
    
    for P in pL:
        Q = get_perp_on_line_for_point([M,N],P)
        R = get_point_by_fractional_length([P,Q],2.0)
        rL.append(R)
    return rL

def scale_triangle(pL,f=1.0):
    A,B,C = pL
    Q,r = get_circumcircle([A,B,C])
    rL = []
    for P in pL:
        new_point = get_point_by_fractional_length(
            [Q,P],f)
        rL.append(new_point)
    return rL

#=======================================

# Archimedes "Broken Chord"

def get_broken_chord_layout(ax):
    [G,A,B] = [
        Point(20,25),
        Point(100,70),
        Point(10,70)]
    Q,r = get_circumcircle([G,A,B])

    M = find_midpoint_of_arc([G,A],[Q,r],major=True)    
    D = get_perp_on_line_for_point([A,B],M)
    E = get_point_by_fractional_length([B,D],2.0)
    
    return { 'Q':Q,'r':r,'G':G,'A':A,'B':B,
             'M':M,'D':D,'E':E }

def get_broken_chord_alternate_layout(ax):
    # G,A very close together, B close to M
    G = Point(30,10)
    A = Point(70,10)
    Q = Point(50,50)
    r = get_length([A,Q])
    
    M = find_midpoint_of_arc([G,A],[Q,r],major=True)
    pL = get_intersection_slope_intercept_circle(0,70,[Q,r])
    B = pL[0]

    D = get_perp_on_line_for_point([A,B],M)
    E = get_point_by_fractional_length([B,D],2.0)
    
    return { 'Q':Q,'r':r,'G':G,'A':A,'B':B,
             'M':M,'D':D,'E':E }


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

#=======================================

# routines for sectors
# developed to make the pizza figure

'''
for a circle on center Q of radius r
and a point A
find the angle the ray QA makes with the horizontal
'''

# degrees ccw from x-axis
def get_angle_for_point_on_center(A,Q):
    dx = A.x - Q.x
    dy = A.y - Q.y
    
    if dx == 0:
        if dy > 0:
            return 90
        return 270
    if dy == 0:
        if dx > 0:
            return 0
        return 180
        
    result = math.degrees(
        math.atan(abs(dy)/abs(dx)))
    if dx > 0 and dy > 0:
        return result
    if dx < 0 and dy > 0:
        return 180 - result
    if dx < 0 and dy < 0:
        return 180 + result
    if dx > 0 and dy < 0:
        return 360 - result
        
    if points_are_close(A,Q):
        return 0
        
    print('here',A,Q)


# angle in degrees ccw from x-axis
def get_point_at_angle_on_circle(angle, cL):
    Q,r = cL
    rad = math.radians(angle)
    #print(rad)
    y = (math.sin(rad) * r) + Q.y
    x = (math.cos(rad) * r) + Q.x
    return Point(x,y)


def get_point_at_angle_length_for_point(theta,d,A):
    # arbitrary
    r = 10
    P = get_point_at_angle_on_circle(theta,[A,r])
    f = d/get_length([A,P])
    return get_point_by_fractional_length([A,P],f)


# i and j endpoints for *both* arcs
def arcs_from_indexes(i,j):
    def do_slices(L,i,j):
        a1 = L[i:j+1]
        a2 = L[j:] + L[:i+1]
        return a1,a2
    
    L = list(range(0,360))
    if i < j:
        a1,a2 = do_slices(L,i,j)
    if j < i:
        a1,a2 = do_slices(L,j,i)
        a1.reverse()
        a2.reverse()
    if len(a1) > len(a2): 
        return a2,a1
    return a1,a2

# get all the angles for the two arcs between A and B on Q

def get_angles_for_center_and_points(Q,A,B):
    t1 = get_angle_for_point_on_center(A,Q)
    t2 = get_angle_for_point_on_center(B,Q)
    #print('t',t1,t2)
    t1,t2 = round(t1),round(t2)
    L = list(range(0,360))
    i = L.index(t1)
    j = L.index(t2)
    #print('i,j',i,j)
    return arcs_from_indexes(i,j)


# circle on center Q, points on circle A,B

def fill_sector(ax,Q,r,A,B,fc='r',alpha=1.0):
    result = get_angles_for_center_and_points(Q,A,B)
    minor, major = result
    points = []
    for angle in minor:
        P = get_point_at_angle_on_circle(angle, [Q,r])
        points.append(P)
    fill_polygon(ax,points,fc=fc,alpha=alpha)


#=======================================

# labels and marks

# original method

def write_one_label(P,s,dx=0,dy=0,SZ='none'):
    if SZ == 'none':
        SZ = 14

    plt.text(P.x+dx,P.y+dy,s,fontstyle='italic',
        # 16 looks better, but screws up all the old stuff
        fontsize=SZ,fontfamily='serif')

def write_labels(L,SZ='none'):
    for e in L:
        P,s = e[0:2]
        try:
            dx,dy = e[2:4]
            write_one_label(P,s,dx,dy,SZ=SZ)
        except ValueError:
            dx,dy = 0,0
        write_one_label(P,s,dx,dy,SZ=SZ)
        
# new approach

def nudge(P,mode='none',f=1.0):
    x,y = P.x,P.y
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
    return Point(x,y)

def label_points(points,SZ='none'):
    for sL in points:
        s,P,mode,how_far = sL
        tmp = nudge(P,mode=mode,f=how_far)
        write_one_label(tmp,s,SZ=SZ)

# dots to show equal angles

# vertices taken CCW, the angle here is at vertex B
# should probably change this to vertex,pL w/arms to be consistent

def mark_angle(pL,d=5):
    assert len(pL) == 3
    bD = get_incenter_and_bisectors(pL)
    A,B,C = pL
    
    line_segment = [B,bD['Q']]
    f = d/get_length(line_segment)
    dot = get_point_by_fractional_length(line_segment,f)
    return dot

def mark_angles(ax,aL,d=5,c='k',s=20):
    rL = list()
    for angle in aL:
        rL.append(mark_angle(angle,d=d))
    #print('scatter','s',s)
    scatter_points(ax,rL,c=c,s=s)
    
def mark_angles_open(ax,aL,d=5,c='k',s=20,ws=3):
    mark_angles(ax,aL,d=d,c=c,s=s)
    mark_angles(ax,aL,d=d,c='w',s=ws)


# had trouble with approaches computing angles

# this works easily, predates get_rectangle routine
# same trick to turn d into a fractional length
# solves issue of which way new point is from A

def mark_right_angle(A,pL,n=3):
    # A is the vertex
    B,C = pL
    d = get_length([A,B])
    
    # moves a given number n of points along AB
    P = get_point_by_fractional_length([A,B],n/d)
    
    d = get_length([A,C])
    Q = get_point_by_fractional_length([A,C],n/d)
    
    # find the fourth point of the square
    M = bisect_angle_Euclid(A,[P,Q])
    N = get_point_by_fractional_length([A,M],2.0)
    return A,P,N,Q


def mark_side_at_point(ax,pL,P):
    A,B = pL
    
    # we don't have get_perp_at_point yet
    m = geo.get_length([A,P])
    n = geo.get_length([A,B])
    f = m/n
    S,T = geo.get_perp_at_point_by_fractional_length(
        pL,f)
        
    length = geo.get_length([P,S])
    d = 4
    f = d/length 
      
    U = geo.get_point_by_fractional_length([P,S],f)
    length = geo.get_length([P,T])
    f = d/length   
    V = geo.get_point_by_fractional_length([P,T],f)
    geo.draw_line_segment(ax,[U,V],lw=1)

def mark_side_twice(ax,pL):
    A,B = pL
    delta = 0.03
    P = geo.get_point_by_fractional_length([A,B],0.5+delta)
    mark_side_at_point(ax,[A,B],P)
    Q = geo.get_point_by_fractional_length([A,B],0.5-delta)
    mark_side_at_point(ax,[A,B],Q)

#=======================================


# short names

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
mvp =  translate_points
sct =  scale_triangle
mka =  mark_angle
mra =  mark_right_angle
grl =  get_rectangle_for_line


