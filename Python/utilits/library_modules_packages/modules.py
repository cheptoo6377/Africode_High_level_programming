print("this file runnning is",__name__)
def calculator(operation ):
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

    # operation = input("Enter operation (+, -, *, /): ")

    n = int(input('Enter a number: '))
    m = int(input('Enter another number: '))

    if operation == '+':
        result = add(n, m)
        print(f"Result: {n} + {m} = {result}")
    elif operation == '-':
        result = subtract(n, m)
        print(f"Result: {n} - {m} = {result}")
    elif operation == '*':
        result = multiply(n, m)
        print(f"Result: {n} * {m} = {result}")
    elif operation == '/':
        result = divide(n, m)
        print(f"Result: {n} / {m} = {result}")
    else:
        print('Invalid operation')
# results = calculator("add")(5,3)
# print(f"Result: {results}")
if __name__ == "__main__":
    # results = calculator("add")()
    print(f"Result: {calculator('add')(5,3)}")