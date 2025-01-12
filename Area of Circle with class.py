class Circle:
    def __init__(self, pi, radius):
        self.pi = pi 
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius**2
    
pi = 3.14
radius = float(input("Enter radius: "))

circle = Circle(pi, radius)
area = circle.calculate_area()
print(round(area))