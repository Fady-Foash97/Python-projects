## Declare 0 value for previous number variable
previous_num = 0
## Loop from 1 to 10
for i in range(1, 11):
    print(f"Current number: {i}, Previous number: {previous_num}, Sum: {previous_num + i}")
    previous_num = i

