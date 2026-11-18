# Question -------------------------------------------------------------------------------------------------------------

# Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result 
# as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, 
# with one space between x and y and one space between y and z, wherein:
# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0


### Solution ###

# Request arithimetic expression
operation = input('Enter Arithimetic Operation: ').strip()

# Split the users input into x,y,z where y is the mathemathical function
x, y, z = operation.split(" ")

# Convert x and z to integers
x = int(x)
z = int(z)

# Computing the arithimetic conditionally depending on the function - 
# because function is still string and cannot be used in that state
if y == '+':
    solution = (float(x + z))
    print(round(solution, 1))
elif y == '-':
    solution = (float(x - z))
    print(round(solution, 1))
elif y == '*':
    solution = (float(x * z))
    print(round(solution, 1))
elif y == '/' and z == 0:
    print('cannot be computed')
elif y == '/':
    solution = (float(x / z))
    print(round(solution, 1))
else:
    print('cannot be computed')
