
number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2 if number2 != 0 else "Error (division by zero)"
else:
    result = "Invalid operator"

print(f'{number1} {operator} {number2} = {result}')