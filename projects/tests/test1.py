import sys
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fill = geo.fill_polygon
points = geo.scatter_points
lines = geo.outline_polygon

# spell it out for three panels
fig, ([ax1,ax2],[ax3,ax4]) = plt.subplots(2,2,
    subplot_kw = {'aspect': 'equal'})
    
ax1.set(xlim=(-10, 110), ylim=(-10, 110))
ax2.set(xlim=(-10, 110), ylim=(-10, 110))
ax3.set(xlim=(-10, 110), ylim=(-10, 110))
ax4.set(xlim=(-10, 110), ylim=(-10, 110))
                 
#-------------------------------

pL = geo.get_standard_triangle()
ax = ax1
fill(ax,pL)
lines(ax,pL,ec='red')
points(ax,pL)

#-------------------------------

pL = geo.get_standard_triangle(mode="right")
ax = ax2
fill(ax,pL,fc='blue',alpha=0.3)
lines(ax,pL,ec='blue')
points(ax,pL)

#-------------------------------

pL = geo.get_standard_triangle(mode="obtuse")
ax = ax3
fill(ax,pL,fc='green')
lines(ax,pL,ec='green')
points(ax,pL)
#-------------------------------

pL = geo.get_standard_triangle(mode="isosceles")
ax = ax4
fill(ax,pL,fc='purple',alpha=0.3)
lines(ax,pL,ec='purple')
points(ax,pL)

#-------------------------------

#plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ex1.png'
plt.savefig(ofn, dpi=300)

