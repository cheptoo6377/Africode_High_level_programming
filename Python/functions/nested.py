
def calculator(operation):

    
   
     



     
    
 def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

def calculator(operation):
    
    while True:
       
        if operation == '5':
            print("Exiting calculator...")
            break
            
        if operation not in ['1', '2', '3', '4']:
            print("Invalid input. Please try again.")
            continue
            
        try:
            # Get user input for numbers
             # Get user input for operation choice
          num1 = input("Enter choice (1/2/3/4/5): ")
          num2 = input("enter number")
          operation =input
          
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
            
        # Perform calculation based on user's choice
        if operation == '+':
            print(f"Result: {num1} + {num2} = {(num1, num2)}")
        elif operation == '-':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '*':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '/':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
            
        print()  # Add empty line for better readability

# Start the calculator

            
    

       
        
 