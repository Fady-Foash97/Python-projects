class Triangle:
    def __init__(self, base, height):
        self.base = base 
        self.height = height 

    def calculate_area(self):
        return 1/2 * self.base * self.height
    
base = float(input("Base: "))
height = float(input("Height: "))

triangle = Triangle(base, height)
area = triangle.calculate_area()
print(area)