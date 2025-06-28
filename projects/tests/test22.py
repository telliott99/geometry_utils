import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fill = geo.fill_polygon
points = geo.scatter_points
lines = geo.outline_polygon

# spell it out for three panels
fig, ([ax1,ax2,ax3]) = plt.subplots(1,3,
    subplot_kw = {'aspect': 'equal'})
    
ax1.set(xlim=(-10, 110), ylim=(-10, 110))
ax2.set(xlim=(-10, 110), ylim=(-10, 110))
ax3.set(xlim=(-10, 110), ylim=(-10, 110))
                 
#-------------------------------

triangles = ['acute','right','obtuse']
axes = [ax1,ax2,ax3]
colors = list('rbg')

#-------------------------------

for i in range(3):
    # does not turn off first two axes ...
    plt.gca().set_axis_off()
    pL = geo.get_standard_triangle(mode=triangles[i])
    [A,B,C] = pL
    K = geo.get_point_by_fractional_length([A,B],0.5)
    L = geo.get_point_by_fractional_length([B,C],0.5)
    M = geo.get_point_by_fractional_length([C,A],0.5)
    
    ax = axes[i]
    c = colors[i]
    fill(ax,pL,fc=c,alpha=0.15)
    lines(ax,pL,ec=c)
    fill(ax,[K,L,M],fc=c,alpha=0.6)
    points(ax,pL,s=4)

#-------------------------------

ofn = '/Users/telliott/Desktop/ex22.png'
plt.savefig(ofn, dpi=300)