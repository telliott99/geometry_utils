This project is a small Python library, ``geometry.py``, to use in drawing figures for my geometry textbook.  The library is at top level in ``geometry.py``.  

I am running Python 3.13 obtained via Homebrew, so I put a symbolic link to geometry.py in:

```
 /usr/local/lib/python3.13/site-packages/geometry.py
```
 

``examples`` contains various directories using it. Scripts written during development to test things are in ``tests``.

Here is a [list](lists/list.txt) of the functions defined there.

Some figures made using the library:

**basic demo**

<img src="demo/demo1.png" width=500>

**Euclid II.5**

<img src="figures/EII_5_crop.png" width=500>

**Pizza theorem**

<img src="projects/pizza/pizza_crop.png" width=300>

**Euclid I.47**

<img src="figures/Pyth_new_1.png" width=300>

**triangle rotation**

<img src="figures/rot_32_crop.png" width=300>

**nine point circle**

<img src="figures/ninepoint_rev_crop.png" width=300>

**broken chord proof 1**

<img src="figures/bc1.png" width=300>

**eyeball theorem**

<img src="figures/eyeball1_crop.png" width=400>

**Heron's theorem**

<img src="figures/heron_crop.png" width=400>

**excircle**

<img src="figures/excircle_crop3.png" width=400>

**similar triangles**

<img src="figures/right_tri_similarity.png" width=400>

There are also a couple of write-ups, including one about Archimedes' broken chord theorem and another about excircles.

This is functional programming.  The only objects we define are members of the class **Point**, to allow access by P.x and P.y.

The variable name **pL** found in most function definitions stands for *point list*, i.e. a list of Point objects.  This may be a line segment, a triangle or another polygon.

We pretend to implement some of Euclid's constructions, but intersections between lines and circles are computed by analytic geometry.   Under the hood, it is algebra.  

When there are two points in a result to be returned, the order in which they are returned is challenging to determine.  In the latest version, for two points, say, perpendicular to a line segment, we return the point "above" the line segment first, if you visualize the line segment as oriented left-to-right.  Some examples may differ.

For circle-circle intersection, we return the point closer to the origin first.

For a perpendicular or angle bisector, the *length* of the perpendicular or bisector should be adjusted by the callee, using the following trick:

```
S,T = get_perp_at_point_by_fractional_length([A,B],f=0.5)
X = get_intersection_for_two_lines([A,B],[S,T])
d = 10   # or whatever the desired length is
f = d/get_length([X,S])
get_point_by_fractional_length([X,S],f)


```

As I fiddled with the code, inconsistency in the order of return of two points has messed up many a diagram.  I believe that's all fixed now.

For most examples, output paths for figures are hard-coded so it will require a bit of configuration to get it to work on another machine.  That's on my todo list.  

There is a sym link to the library in each sub-folder.

Here are some functions we can call:

```
geo.get_intersection_for_two_lines([A,B],[C,D])
geo.get_point_perp_on_line_for_point(P,[A,B])
geo.get_perp_at_point_by_fractional_length([A,B],f=0.5)

get_intersection_line_segment_circle([A,B],[Q,r])
get_intersection_circle_circle([Q1,r1],[Q2,r2])
get_tangent_points_on_circle_for_point([Q,r],P)
```

These are from the callee's POV.  In the library's function definition, you cannot have ``([A,B],[C,D])``, it is

```
geo.get_intersection_for_two_lines(pL1,pL2)
```

Errors can be challenging to interpret with matplotlib.  In drawing functions like 

```
geo.outline_polygon(ax,[A,B,E,D],ec='k')
geo.draw_line_segments(ax,[[D,F],[C,F]])
```

If you forget ``ax`` in the first one, the error is:

```
TypeError: outline_polygon() missing 1 required 
positional argument: 'pL'
```

If you forget to make a list of line segments by adding a second pair of brackets in the second one:

```
TypeError: draw_line_segments() got multiple values 
for argument 'ec'
```

Other mistakes with brackets may result in Python trying to access a coordinate like ``P.x`` and complaining that a list doesn't have one.

```
AttributeError: 'tuple' object has no attribute 'x'
```

Finally, the functions in the library have long, but I hope explicit, names.  I'm experimenting with shortcut definitions ([here](lists/short.txt)).

For this we do ``from geometry import *`` in spite of the fact that it's generally not good practice.  That's so the shortcuts can live in the library.  Alternatively, one might place them in each script, prefaced like

```
tr =  geo.get_standard_triangle
```