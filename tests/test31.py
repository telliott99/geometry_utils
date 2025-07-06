import geometry as geo
import matplotlib.pyplot as plt

fig, ax = geo.init()
ax.set(xlim=(-50,110), ylim=(-10,100))

# two points for a line
pL = geo.get_standard_triangle()
pL = geo.scale_triangle(pL,0.5)
A,B,C = pL
geo.dlss(ax,[[A,B],[B,C],[A,C]],ec='r',ls=':')

def get_equi_triangle_on_side(pL):
    A,B = pL
    r = geo.get_length([A,B])
    S,T = geo.xcc([A,r],[B,r])
    if geo.point_is_above_line(S,[A,B]):
        return S
    return T

def get_Napoleon_points_for_line(pL):
    A,B = pL
    P = get_equi_triangle_on_side(pL)
    D = geo.get_centroid_and_medians([A,B,P])
    A1 = geo.get_point_by_fractional_length(
        [A,B],0.333)
    A2 = D['G']
    A3 = geo.get_point_by_fractional_length(
        [A,B],0.666)
    return P,A1,A2,A3

def draw_arrow(plt,pL):
    A,B = pL
    dx,dy = geo.get_deltas([A,B])
    plt.arrow(A.x,A.y,dx,dy,
        head_width=3,head_length=3,
        length_includes_head=True, 
        fc='k',ec='r',lw=1)
        
def do_one_side(plt,pL):
    A,B = pL
    P,A1,A2,A3 = get_Napoleon_points_for_line([A,B])
    #geo.dlss(ax,[[A,P],[P,C]],ec='k',ls=':')
    draw_arrow(plt,[A,A1])
    draw_arrow(plt,[A1,A2])
    draw_arrow(plt,[A2,A3])
    draw_arrow(plt,[A3,B])
    return P,A1,A2,A3

P,_,G,_ = do_one_side(plt,[A,C])
R,_,H,_ = do_one_side(plt,[C,B])
geo.dls(ax,[A,P],ec='b')
geo.dls(ax,[P,C],ec='b')
geo.dls(ax,[C,R],ec='g')
geo.dls(ax,[R,B],ec='g')


geo.scp(ax,[A,B,C,G,H,P,R],s=5)

geo.savefig(plt)