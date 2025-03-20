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
    