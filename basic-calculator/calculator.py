num1 = float(input (" Enter a number "))
num2 = float(input (" Enter another number "))

operation =  input (" Enter a operation")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print(" error cant divide by zero")
else:
    result = "Inavalid operation"

print("Result is " , result)
