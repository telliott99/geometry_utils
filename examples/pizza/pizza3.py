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
geo.scatter_points(ax,[P])

# horizontal left,right
LEFT,RIGHT = geo.get_intersection_line_segment_circle(
    [P,geo.Point(P.x+5,P.y)],[Q,r])
    
# switched output for now
LEFT,RIGHT = RIGHT,LEFT
    
# vertical up,down
UP,DOWN = geo.get_intersection_line_segment_circle(
    [P,geo.Point(P.x,P.y+5)],[Q,r])
    
# upper right 45 lower left
UR,LL = geo.get_intersection_line_segment_circle(
    [P,geo.Point(P.x+5,P.y+5)],[Q,r])
    
# upper left 45 lower right
LR,UL = geo.get_intersection_line_segment_circle(
    [P,geo.Point(P.x-5,P.y+5)],[Q,r])
# switched output for now
#LR,UL = UL,LR

geo.scatter_points(ax,[LEFT,RIGHT,UP,DOWN])
geo.scatter_points(ax,[UR,LL,LR,UL])
geo.write_one_label(
    Q,'+',SZ=12)

#-----------------------------------

# no Q
dx = RIGHT.x - P.x
R = geo.Point(LEFT.x+dx,P.y)
dy = UP.y - P.y
S = geo.Point(R.x,DOWN.y+dy)
T = geo.Point(P.x,S.y)

geo.scatter_points(ax,[R,S,T],c='r')

d = 5 # distance for offset of central square)

# two more oddball points
# point on circle cut by line through R w/slope -1
k = geo.get_intercept_for_point_slope(R,-1)

# pick the second one
U = geo.get_intersection_slope_intercept_circle(
        -1,k,[Q,r])[1]

# point on circle cut by line through T w/slope -1
k = geo.get_intercept_for_point_slope(T,-1)

V = geo.get_intersection_slope_intercept_circle(
        -1,k,[Q,r])[0]

geo.scatter_points(ax,[U,V],c='r')

#-----------------------------------

geo.label_points([('P',P,'N',1),
                  ('LEFT',LEFT,'W',11),
                  ('RIGHT',RIGHT,'E',1),
                  ('UP',UP,'N',1),
                  ('DOWN',DOWN,'S',4),
                  ('UR',UR,'N',1),
                  ('UL',UL,'N',2),
                  ('LR',LR,'E',2),
                  ('LL',LL,'N',1),
                  ('R',R,'N',1),
                  ('S',S,'N',1),
                  ('T',T,'N',1),
                  ('U',U,'W',4),
                  ('V',V,'SE',3),
                  ])


'''

# interior point(s) first, CCW direction for all points
poly_A = [P,HR,UR]
poly_a = [R,U,HL]
geo.fill_polygon(ax,poly_A,fc='r',alpha=1.0)
geo.fill_polygon(ax,poly_a,fc='r',alpha=0.3)

# b,B
# interior point first, CCW direction for arc points
poly_B = [R,P,UL,U]
geo.fill_polygon(ax,poly_B,fc='b',alpha=1.0)


# d,D
# interior point first, CCW direction for arc points
poly_d = [P,VU,UL]
geo.fill_polygon(ax,poly_d,fc='m',alpha=0.3)

'''

#-----------------------------------

plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/pizza3.png'
plt.savefig(ofn, dpi=300)


