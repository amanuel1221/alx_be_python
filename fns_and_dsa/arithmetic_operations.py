
def perform_operation(num1, num2, operation):
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
           return print("Cannot divide by zero.")
        else:
         return num1 / num2
    else:
        print("Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'.")
       
