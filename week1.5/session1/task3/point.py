# Week 1.5, Session 1: Task 3


class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        """
        Creates a Point with coordinates (x, y)
        """
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self):
        """
        returns distance from this Point to origin
        """
        return (self.x**2 + self.y**2) ** 0.5

    # Add distance_to() method here
    def distance_to(self, other):
        """
        returns distance from this Point to another Point
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# Finally, add code here to demonstrate use of Point
p1 = Point(3, 4)
print("p1:", p1.x, p1.y)
print("Distance from origin:", p1.distance())

p2 = Point(6, 8)
print("p2:", p2.x, p2.y)
print("Distance from p1 to p2:", p1.distance_to(p2))
