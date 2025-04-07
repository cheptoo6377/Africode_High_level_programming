a = 1
b =2
def divide(a, b):
    return a / b
results = divide(1, 0)
# print(results)
try:
    result = divide(1, "one")
except ZeroDivisionError as e:
    print(e)
except TypeError:
    print("invalid input,atleast enter a number")
except:
    print("Error: Division by zero")
else:
    print("execution was succesful")
finally:
    print("i am being executed,no matter what")

