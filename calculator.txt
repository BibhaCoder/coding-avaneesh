loop = 100
for i in range(loop):
    operation = input("Enter operation (+, -, *, /) or type 'Exit' to stop: ")
    if operation.lower() == "exit":  # Exits calculator
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = "Invalid operation"
    
    print(result)
    if operation.lower() == "exit":  # Exits calculator
        break
