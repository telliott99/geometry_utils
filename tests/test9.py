import path
import matplotlib
import matplotlib.pyplot as plt
import geometry as geo

ofn = '/Users/telliott/Desktop/example9.png'

# we don't do much with this
# but it's an arc, can even be elliptical

fig, ax = geo.init()
ax.set(xlim=(-25, 110), ylim=(-25, 110))

Q = (40,40)    # ellipse center
w = 40         # ellipse
h = 40         # ellipse
angle = 0      # ellipse rotation

#theta1         # default 0
#theta2         # default 360

arc = matplotlib.patches.Arc(
    Q,w,h,theta1=0,theta2=90)
    
ax.add_patch(arc)
plt.savefig(ofn, dpi=300)
