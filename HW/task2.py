def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
else:
    result = "Invalid operator!"

if isinstance(result, (int, float)):
        result = int(result) if result.is_integer() else result

print(f"The result is: {result}")
