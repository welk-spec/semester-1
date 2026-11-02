# Week 1.6, Session 1: Task 3

from shapes import Circle
from point import Point

circle = Circle(radius=2.5, position=Point(x=0.0, y=0.0))

print(circle)
print(f"Area = {circle.area():.3f}")
print(f"Perimeter = {circle.perimeter():.3f}")
print("Moving the circle...")
circle.set_position(Point(x=1.6, y=3.2))
print(circle)
print("Changing the circle's colour...")
circle.set_colour("green")
print(circle)


# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
