
def calculator(operation):
n = int(input('enter a number'))
m = int(input('enter a number'))
operation = input('enter an operation')
if operation == '+':
    print(n + m)
elif operation == '-':
    print(n - m)
elif operation == '*':
    print(n * m)
elif operation == '/':
    print(n / m)
else:
    print('invalid operation')
    
    #  def add(x, y):
    
    #     return x + y

    #  def subtract(x, y):
    #     return x - y

    #  def multiply(x, y):
    #     return x * y
    #  def divide(x, y):
    #     return x / y
    #  if operation == "add":
    #     return add
    #  elif operation == "subtract":
    #     return subtract
    #  elif operation == "multiply":
    #     return multiply
    #  elif operation == "divide":
    #     return divide
    #  else:
    #     return "Invalid operatin"