import sys, path
import matplotlib.pyplot as plt
import numpy as np
import random
import geometry as geo

# random testing of geo.get_all_angles

v = len(sys.argv) > 2

fig, ax = geo.init()
ax.set(xlim=(0,100), ylim=(0,100))

def test1():
    pL = geo.get_standard_triangle(mode='isosceles')
    if v: print(geo.get_all_angles(pL))

def test2():
    A,B = geo.get_random_points(n=2)
    f = random.uniform(0,1)
    while f < 0.5:
        f *= 2
    d = geo.get_length([A,B])*f
    if v: print(A,B)
    if v: print('d = %3.2f' % d)
    P,Q = geo.get_intersection_circle_circle(
            [A,d],[B,d])
    # tri ABP is isosceles
    
    return geo.get_all_angles([A,B,P]) 

for i in range(10):
    result = test2()
    if v: print('%3.2f, %3.2f, %3.2f' % result)
    if v: print()



'''
> p3 test_geo16.py v
23.000,74.000 82.000,84.000
d = 39.63
40.97, 40.97, 81.94

0.000,69.000 29.000,22.000
d = 38.50
44.17, 44.17, 88.33

53.000,46.000 43.000,87.000
d = 41.66
59.57, 59.57, 60.86

12.000,58.000 33.000,89.000
d = 23.72
37.90, 37.90, 75.79

61.000,70.000 15.000,28.000
d = 60.72
59.14, 59.14, 61.71

39.000,59.000 54.000,77.000
d = 15.80
42.15, 42.15, 84.30

63.000,49.000 36.000,100.000
d = 37.61
39.91, 39.91, 79.81

68.000,73.000 69.000,46.000
d = 26.17
58.92, 58.92, 62.15

41.000,79.000 88.000,19.000
d = 41.15
22.16, 22.16, 44.33

10.000,32.000 62.000,94.000
d = 74.09
56.90, 56.90, 66.20

> 
'''