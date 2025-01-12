class Rectangle:
    def __init__(self, length, width):
        self.length = length 
        self.width = width 
    def calculate_area(self):
        return self.length * self.width
#Using class and its objects
length = float(input("Enter length: "))
width = float(input("Enter width: "))
rectangle = Rectangle(length, width)
area = rectangle.calculate_area()
print(area)
