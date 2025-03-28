# n = int(input('enter a number'))
# m = int(input('enter a number'))

def calculator(operation):
    def add(n, m):
        return n + m
    def subtract(n, m):
        return n - m
    def multiply(n, m):
        return n * m
    def divide(n, m):
        if m == 0:
            return "Error! Division by zero."
        return n / m

operation = ( )

calculation=calculator(operation)

n = int(input('enter a number'))#input  a number of choice
m = int(input('enter a number'))# input a number of choice

result =[ n + m] 
print(f"the results of adding {n} {m} is {result}")

result =[ n - m]
print(f"the results of subtracting {n} {m} is {result}")
result =[ n * m]
print(f"the results of multiplying {n} {m} is {result}")
if operation == '+':#addition
        n = int(input('enter a number'))
        m = int(input('enter a number'))
        result = n + m
        print(f"Result: {n} + {m} = {(n, m)}")
elif operation == '-':#subtraction
        n = int(input('enter a number'))
        m = int(input('enter a number'))
        result = n - m
        print(f"Result: {n} - {m} = {(n, m)}")
elif operation == '*':#multiplication
         print(f"Result: {n} * {m} = {multiply(n, m)}")
elif operation == '/':#division
         print(f"Result: {n} / {m} = {(n,m)}")
else:
        print('invalid operation')
        print(calculation)  # Add empty line for better 

