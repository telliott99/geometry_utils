import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

fig, ax = geo.init()
                   
[A,B,C] = geo.get_standard_triangle("acute")


geo.outline_polygon(ax,[A,B,C],ec='lightsalmon')

geo.draw_line_segment(ax,[A,B,C])


geo.scatter_points(ax,[A,B,C])

# testing a new way of doing labels
# specify direction from point as NESW etc.

points = [ ['A',A,'SW',6],
           ['B',B,'SE',3],
           ['C',C,'NE',1] ]
           
def label_points2(points):
    for sL in points:
        s,P,mode,how_far = sL
        tmp = geo.nudge(P,mode=mode,f=how_far)
        # extra push
        if s == 'B':
            tmp = geo.nudge(tmp,mode='S',f=2)
        #print(tmp)
        geo.write_one_label(tmp,s)

label_points2(points)
           
plt.gca().set_axis_off()
ofn = '/Users/telliott/Desktop/ex15.png'
plt.savefig(ofn, dpi=300)
