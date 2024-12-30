## Declare the number groups
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print("Given list: ", numbers_x, "\n            ", numbers_y)
## Find out if the first and last number in each group are equal to each other
if numbers_x[0] == numbers_x[4]:
    print (True)
else:
    print (False)

if numbers_y[0] == numbers_y[4]:
    print (True)
else:
    print (False)
