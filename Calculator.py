def Calculator():
  while True:
    a = float(input("Insert first number: "))
    b = float(input("Insert second number: "))
    operation = input("Do you want to(Add, Subtract, Multiply, Divide)? ")
    if operation == "Add":
        print(f"result = {a + b}")
    elif operation == "Subtract":
        print(f"result = {a - b}")
    elif operation == "Multiply":
        print(f"result = {a * b}")
    elif operation == "Divide":
        print(f"result = {a / b}")
    else: 
        print("Invalid")
    repeat = input("Do you want to calculate again? ")
    if repeat != "yes":
        print("Goodbye")
        break


Calculator()