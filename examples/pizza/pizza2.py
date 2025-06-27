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
for a circle on center Q of radius r
and a point A
find the angle the ray QA makes with the horizontal
'''

def points_are_close(A,B):
    e = 1e-3
    dx,dy = geo.get_deltas([A,B])
    if dx < e and dy < e:
        return True
    return False

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


def test():
    N = 10000
    for i in range(N):
        while True:
            x = np.random.randint(20,80)
            y = np.random.randint(20,80)
            if r**2 > ((x-Q.x)**2 + (y-Q.y)**2):
                break
        
        if i < N-20:
            continue
            
        A = geo.Point(x,y)
        theta = get_angle_for_point_on_center(A,Q)
        geo.scatter_points(ax,[A])
        geo.write_one_label(
            A,str(round(theta)),dx=2,dy=2,SZ=8)
        geo.draw_line_segment(ax,[Q,A])
        
#test()

# angle in degrees ccw from x-axis
def get_point_at_angle_on_circle(angle, cL):
    Q,r = cL
    rad = math.radians(angle)
    #print(rad)
    y = (math.sin(rad) * r) + Q.x
    x = (math.cos(rad) * r) + Q.y
    return geo.Point(x,y)

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


phi1 = 0
phi2 = 110

A = get_point_at_angle_on_circle(phi1,[Q,r])
B = get_point_at_angle_on_circle(phi2,[Q,r])

result = get_angles_for_center_and_points(Q,A,B)
minor, major = result
points = []
for angle in minor:
    P = get_point_at_angle_on_circle(angle, [Q,r])
    points.append(P)
geo.fill_polygon(ax,points + [Q],fc='m',alpha=1.0)


#-----

# arc for any inscribed point

'''
M = geo.get_point_by_fractional_length([A,B],0.5)
S,T = geo.get_intersection_line_segment_circle(
          [Q,M],[Q,r])
                    
# S should be closer to origin, but this sometimes fails
geo.scatter_points(ax,[S])
geo.fill_polygon(ax,points + [S],fc='m',alpha=0.3)
'''

theta = round((phi1+phi2)/2 + 180) % 360
M = get_point_at_angle_on_circle(theta,[Q,r])
geo.fill_polygon(ax,points + [M],fc='m',alpha=0.3)



plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/pizza.png'
plt.savefig(ofn, dpi=300)


