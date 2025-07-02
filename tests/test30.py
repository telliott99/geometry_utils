import geometry as geo
import matplotlib.pyplot as plt

fig, ax = geo.init()
ax.set(xlim=(-20,110), ylim=(-10,100))

def get_rectangle_for_line(pL,aspect_ratio=1.0):
    A,B = pL
    base = geo.get_length([A,B])
    height = aspect_ratio*base
    
    # construct perp of arbitrary length at B
    # S should be "above" AB
    
    # but it is not when B,A is arg
    S,T = geo.get_perp_at_point_by_fractional_length(
        [A,B],f=1.0)
    if not geo.point_is_above_line(S,[A,B]):
        S,T = T,S
        
    f = height/geo.get_length([B,S])
    C = geo.get_point_by_fractional_length([B,S],f)
    
    # do the same at A
    # U should be "above" AB
    
    U,V = geo.get_perp_at_point_by_fractional_length(
        [A,B],f=0)
    if not geo.point_is_above_line(U,[A,B]):
        U,V = V,U

    f = height/geo.get_length([A,U]) 
    D = geo.get_point_by_fractional_length([A,U],f)
    return A,B,C,D
  
# two points for a line
A = geo.Point(20,50)
B = geo.Point(20,70)

# construct the square on AB or BA

_,_,C,D = get_rectangle_for_line(
    [B,A],aspect_ratio=1.0)
    

geo.label_points(
    [['A',A,'N',0],
     ['B',B,'N',0],
     ['C',C,'N',0],
     ['D',D,'N',0],
     ])

geo.scp(ax,[A,B,C,D])

geo.savefig(plt)