This project is a Python library to help in drawing figures for my geometry textbook.

Paths are hard-coded so it will require a slight bit of configuration to get it to work on another machine.

Here are a couple of examples of figures made with the library:

<img src="broken_chord/figures/bc1.png" width=300>

<img src="tangents/eyeball1.png" width=400>

<img src="tests/example15.png" width=400>

<img src="bisectors/excircle.png" width=400>

There are also a couple of write-ups, e.g. one on Archimedes' broken chord theorem.

Intersections between lines and circles are computed by analytic geometry.  We pretend to implement some of Euclid's constructions, but under the hood it is algebra.

**pL** stands for *point list*.  The only objects we define are members of the class **Point**, to allow access by P.x and P.y.

Here are a few examples of the functions we can call:

```
geo.get_intersection_for_two_lines([A,B],[C,D])
geo.get_point_perp_on_line_for_point(A,pL)
geo.get_perp_at_point_by_fractional_length(pL,f=0.5)

get_intersection_line_segment_circle(pL,cL)
get_intersection_circle_circle(cL1,cL2)
get_tangent_points_on_circle_for_point(cL1,P)
'''