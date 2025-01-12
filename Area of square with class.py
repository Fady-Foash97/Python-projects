class Square:
    def __init__(self, length):
        self.length = length

    def calculate_area(self):
        return self.length**2
    
length = float(input("Enter length: "))
square = Square(length)
area = square.calculate_area()
print(area)