num1 = float(input("First number: "))
num2 = float(input("Second number: "))

valid_ops = {"+", "-", "*", "/"} # set of valid operators, so we can easily check if the user input is valid

operator = ""
while operator not in valid_ops:
    operator = input("Operator (+, -, *, /): ").strip()
    if operator not in valid_ops:
        print("Must be +, -, *, or /")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    if num2 == 0:
        print("Can't divide by zero")
        result = None
    else:
        result = num1 / num2

if result is not None:
    print(f"{num1} {operator} {num2} = {result}")