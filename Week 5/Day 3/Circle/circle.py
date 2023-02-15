
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def diameter(self):
        return self.radius*2
    def area(self):
        return round((self.radius**2)*22/7,2)
    def __str__(self):
        return (f"This is a circle with a radius of {self.radius}, a diameter of {self.diameter()} and area of {self.area()}")
    def __repr__(self):
        return f"Circle ({self.radius})"
    def __add__(self,other_circle):
        result = Circle(self.radius + other_circle.radius) 
        return result
    def __gt__(self,other_circle):
        return self.area() > other_circle.area()
    def __lt__(self,other_cirle):
        return self.area() < other_cirle.area()
    def __eq__(self,other_circle):
        return self.area()== other_circle.area()
    def __ne__(self,other_circle):
        return self.area()!= other_circle.area()

circle = Circle(3)
circle1 = Circle(2)
circle2 = Circle(5)
circle3 = circle1 + circle2
circles = [circle, circle1, circle2]
circles.sort()
print(circles)
print(circle+ circle1)
print(circle<circle1)
print(circle1<circle)
print(circle2 == circle3)
print(circle)
print(circle3.diameter())
print(circle3)