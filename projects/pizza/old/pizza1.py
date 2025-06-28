import sys,math
import matplotlib.pyplot as plt
import numpy as np

import geometry as geo

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))


Q = geo.Point(50,50)
r = 30

c1 = plt.Circle(
    (Q.x,Q.y),r,fc='none',ec='k')
ax.add_patch(c1)

'''

# first idea
# given a line
# find points on the circle whose radii pass through it

# start with a point and a line hoz through it
A = geo.Point(75,40)
B = geo.Point(A.x+10,A.y)

geo.scatter_points(ax,[A,Q])

# find points at an angle to the hoz
C,D = geo.get_points_at_angle_to_line(45,[A,B])

# find two points on the circle
S,T = geo.get_intersection_line_segment_circle(
    [A,C],[Q,r])

geo.draw_line_segments(ax,[[S,T]],ec='b')

X = []
R = np.arange(0,1,0.1)
# lose the first point, it's on the circle
R = R[1:]

for f in R:
    P = geo.get_point_by_fractional_length([S,T],f)
    X.append(P)

Y = []
for P in X:
    U,V = geo.get_intersection_line_segment_circle(
        [Q,P],[Q,r])
    if geo.get_length([Q,U]) > r:
        U,V = V,U
    Y.append(U)

geo.scatter_points(ax,X,c='b')
geo.scatter_points(ax,Y)

'''

# next idea
# given a circle Q,r find points evenly spaced
# construct a dict to hold values, keyed by theta

# step size for angles
def get_edge_points_for_circle(Q,r,step=0.1):
    # we choose a dict b/c we may e.g. theta = 135.2
    D = dict()    
    # can try increasing the delta, start with 1
    for theta in np.arange(0.,360.0+step,step):
        x = math.cos(math.radians(theta)) * r
        y = math.sin(math.radians(theta)) * r
        D[theta] = geo.Point(Q.x+x,Q.y+y)
    return D

D = get_edge_points_for_circle(Q,r)

'''
for theta in np.arange(0,271,15):
    A = D[theta]
    B = D[theta+2]
    
    geo.fill_polygon(ax,[A,B,Q],fc='m',alpha=1.0)
'''

# given point on the circle
def get_closest_angle_in_dict(A):
    # first find the angle the ray QA makes w/x-axis
    hoz = geo.Point(Q.x+10,Q.y)    
    phi = geo.get_angle(A,[Q,hoz])
    
    # find the closest key in the dict
    # do we have to search from the beginning?

    angleL = sorted(D.keys())
    for i,angle in enumerate(angleL):
        # first angle is zero, so first test will not fail
        if phi - angle < 0:
            next = angle
            break
            
    # i is index of first angle in dict > phi
    # that could be good enough, or test for diff?
    prev = angleL[i-1]
    if abs(phi-prev) < abs(next-phi):
        phi = prev
    else:
        phi = next
    return phi

def get_points_on_circle_between_AB(pL):
    A,B = pL
    U = get_closest_angle_in_dict(A)
    V = get_closest_angle_in_dict(B)
    if U > V:
        U,V = V,U
    
    arc1 = []
    arc2 = []
    for angle in D.keys():
        if angle < V and angle > U:
            arc1.append(angle)
        else:
            arc2.append(angle)
        
    return arc1, arc2
        
'''      
minor, major = get_points_on_circle_between_AB(
         [geo.Point(60,70), geo.Point(70,70)])
         
if len(minor) > len(major):
    minor,major = major,minor

'''

step=0.1

def get_circle_points(Q,r,step=step):
    Y = []
    rsq = r**2
    X = np.arange(Q.x-r,Q.x+r+step,step)
    for x in X:
        xsq = (x-Q.x)**2
        # delta can be slightly < 0 for x ≈ r
        delta = abs(rsq-xsq)
        y = math.sqrt(abs(delta))
        x,y = round(x,3), round(y,3)
        print(x,xsq,rsq,delta,y)
        Y.append(geo.Point(x,y))
    return X,Y

X,Y = get_circle_points(Q,r,step)

'''

def find_points_between_AB_on circle(A,B,X,Y):
    if A > B:
        A,B = B,A
    start = 0
    while 
        
    

goal is to be able to find points on a circle between 
two given points
so as to fill in a polygon ≈ circle

I have fooled around with pre-computing all points, but ...
'''

# suppose we have a point somewhere, not = Q
# compute the angle with Q

# we have to take account of quadrant
# and the fact that we are counting theta ccw from pos x

def get_angle_on_circle_for_point(Q,A):
    dx,dy = geo.get_deltas([Q,A]) 
    if abs(dx) < 0.1:
        if dy > 0: 
            return 90
        return 270    
    theta = math.degrees(math.atan(dy/dx))
    if dx < 0 and dy > 0:
        theta += 180
    elif dx < 0 and dy < 0:
        theta += 180
    elif dx > 0 and dy < 0:
        theta += 360
    return round(theta,1)
    
# A does not have to be inside the circle

def test():
    for i in range(15):
        x = np.random.randint(20,80)
        y = np.random.randint(20,80)
        A = geo.Point(x,y)
        theta = get_angle_on_circle_for_point(Q,A)
        geo.scatter_points(ax,[A])
        geo.write_one_label(
            A,str(theta),dx=2,dy=0,SZ=8)
        geo.draw_line_segment(ax,[Q,A])
        
test()






'''

def get_points_on_circle(Q,r,step=1):
    aL = np.arange(0.,360.+step,step)
    rL = []
    for theta in aL:
        x = math.cos(math.radians(theta)) * r + Q.x
        y = math.sin(math.radians(theta)) * r + Q.y
        rL.append((theta,geo.Point(x,y)))
    return rL

#-------------------------------------

def get_arcs(Q,A,B,cL):
    hoz = geo.Point(Q.x+r,Q.y)    
    theta = geo.get_angle(A,[Q,hoz])
    phi = geo.get_angle(B,[Q,hoz])

    arc1 = []
    arc2 = []
    for angle,P in cL:
        if theta <= angle <= phi:
            arc1.append(P)
        else:
            arc2.append(P)
    if len(arc1) <= len(arc2):
        return arc1,arc2
    return arc2,arc1

cL = get_points_on_circle(Q,r)
A = geo.Point(80,50)
B = geo.Point(50,80)
minor,major = get_arcs(Q,A,B,cL)
print(minor)


def get_projection_on_circle(Q,r,A):
    hoz = geo.Point(Q.x+r,Q.y)    
    theta = geo.get_angle(A,[Q,hoz])
    phi = geo.get_angle(B,[Q,hoz])
    aL,_ = get_angles_for_sector(Q,r,theta,phi)

def get_angles_in_sector(Q,r,theta,phi):
    # adjust for step size
    if theta > phi:
        theta,phi = phi,theta
    arc1 = []
    arc2 = []
    for angle in D.keys():
        if theta <= angle <= phi:
            arc1.append(angle)
        else:
            arc2.append(angle)
    # return minor arc first
    if len(arc1) < len(arc2):
        return arc1,arc2
    return arc2,arc1

def get_points_on_circle_for_endpoints(Q,r,A,B):
    hoz = geo.Point(Q.x+r,Q.y)    
    theta = geo.get_angle(A,[Q,hoz])
    phi = geo.get_angle(B,[Q,hoz])
    aL,_ = get_angles_for_sector(Q,r,theta,phi)
    rL = [D[k] for k in aL]
    return rL

x1 = 10
x2 = 20
A = geo.Point(Q.x + x1, math.sqrt(r**2 - x1**2) + Q.y)
B = geo.Point(Q.x + x2, math.sqrt(r**2 - x2**2) + Q.y)
rL = get_points_on_circle_for_endpoints(Q,r,A,B)
'''








plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/pizza1.png'
plt.savefig(ofn, dpi=300)


