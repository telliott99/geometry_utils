import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo
import broken_chord as bc

fig,ax,fD = bc.setup()

G = fD['G']; A = fD['A']; B = fD['B']
M = fD['M']; D = fD['D']; E = fD['E']
Q = fD['Q']; r = fD['r']

# ----



# ----

# rescatter to make them clean
geo.scatter_points(ax,[M,A,B,E,D,G],s=8)

plt.gca().set_axis_off()

ofn = '/Users/telliott/Desktop/broken_chordX.png'
plt.savefig(ofn, dpi=300)





