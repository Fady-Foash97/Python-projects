class Calculator:
    def __init__(self, a, b):
        self.a = float(a) 
        self.b = float(b)

    def calculations(self, operation):
        if operation == "plus":
            return self.a + self.b 
        elif operation == "minus":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b 
        elif operation == "divide":
            if self.b != 0:
                return self.a / self.b 
            else:
                print("Error: Division by zero is not allowed")

a = input("Enter first number: ")
b = input("Enter second number: ")

operation = input("What operation would you like to enter(plus, minus, multiply, divide): ").lower()

calc = Calculator(a, b)
result = calc.calculations(operation)
print(f"Result is {result}")

 

