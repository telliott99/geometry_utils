import path
import matplotlib.pyplot as plt
import numpy as np
import geometry as geo

ofn = '/Users/telliott/Desktop/broken_chord0.png'

def setup():
    fig, ax = geo.init()
    ax.set(xlim=(0,120), ylim=(0,120))
    fD = geo.get_broken_chord_layout(ax)
    
    # ----------------------------------------
    
    G = fD['G']; A = fD['A']; B = fD['B']
    M = fD['M']; D = fD['D']; E = fD['E']
    Q = fD['Q']; r = fD['r']
    
    geo.draw_line_segments(
        ax,[[A,B],[D,M],[G,B]])
    
    circle = plt.Circle(
        (Q.x,Q.y),r,fc='none',ec='k')
    ax.add_patch(circle)
    
    geo.scatter_points(ax,[M,A,B,D,G],s=8)
    
    geo.write_labels([(A,'A',2,1),
                      (B,'B',-5,1),
                      (G,'G',-7,-4),
                      (D,'D',1,1),
                      (M,'M',-3,3) ])
    
    circle = plt.Circle((Q.x,Q.y),r,fc='none',ec='k')
    ax.add_patch(circle)

    return fig,ax,fD

if __name__ == '__main__':

    fig,ax,fD = setup()
    plt.gca().set_axis_off()
    plt.savefig(ofn, dpi=300)



