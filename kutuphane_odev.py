from pyslope import *

s = Slope(height=10, angle=25, length=None)

m1 = Material(
    unit_weight=18,
    friction_angle=0,
    cohesion=50,
    depth_to_bottom=2
)

m2 = Material(20, 30, 2, 5)

s.set_materials(m1, m2)

u1 = Udl(magnitude = 15)

s.set_udls(u1)

p1 = LineLoad(magnitude = 15, offset = 3)

s.set_lls(p1)

s.set_water_table(5)

s.set_analysis_limits(s.get_top_coordinates()[0] - 5, s.get_bottom_coordinates()[0] + 5)

s.update_analysis_options(
    slices=50,
    iterations=2500,
    tolerance=0.005,
    max_iterations=50
)

s.analyse_slope()

print(s.get_min_FOS())

s.plot_boundary()
s.plot_critical()
s.plot_all_planes(max_fos=2)
