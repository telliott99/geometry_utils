import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

# this test is for debugging issues with bisection
# which tracked down to
# always specify triangles and angles CCW direction
# vertex is second point

ofn = '/Users/telliott/Desktop/example13.png'

fig, ax = geo.init()
ax.set(xlim=(-20,120), ylim=(-20,120))

pL = geo.get_standard_triangle('acute')
[A,B,C] = pL
geo.draw_line_segment(ax,pL)

# side lengths
a = geo.get_length([B,C])
b = geo.get_length([A,C])
c = geo.get_length([A,B])

# do not worry about exact placement
geo.write_labels([(A,'A'),
                  (B,'B'),
                  (C,'C') ])

bD = geo.get_incenter_and_bisectors([A,B,C])
P = bD['P']
Q = bD['Q']
R = bD['R']
geo.scatter_points(ax,[P,Q,R])

# calculate bisectors directly
U = geo.get_point_by_fractional_length([B,C],c/(b+c))
V = geo.get_point_by_fractional_length([C,A],a/(a+c))
W = geo.get_point_by_fractional_length([A,B],b/(a+b))

geo.scatter_points(ax,[U,V,W],c='red')

geo.write_labels([(U,'U'),
                  (V,'V'),
                  (W,'W') ])

# check angles directly
mA = geo.get_angle(A,[B,C])
mB = geo.get_angle(B,[A,C])
mC = geo.get_angle(C,[A,B])
#print(mA,mB,mC)

'''
gD = geo.get_centroid_and_medians([A,B,C])
K = gD['K']
L = gD['L']
M = gD['M']
geo.scatter_points(ax,[K,L,M],c='b')

geo.write_labels([(K,'K'),
                  (L,'L'),
                  (M,'M') ])
'''
plt.savefig(ofn, dpi=300)