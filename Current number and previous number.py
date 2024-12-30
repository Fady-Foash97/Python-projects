## Declare 0 value for previous number variable
previous_num = 0
## Loop from 1 to 10
for i in range(1, 11):
    sum = previous_num + i 
    print("Current number:", i, "Previous number:", previous_num, "Sum: ", sum)
    previous_num = i

