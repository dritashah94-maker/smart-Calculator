# loops that will ask the user to calculate again and again
while True:
    # users input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # conditons
    if operator == "+":
        result = num1+ num2
    elif operator == "-":
        result = num1-num2
    elif operator == "*":
        result = num1*num2
    elif operator =="/":
        result = num1/num2
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
    else:
        print ("Invalid opertor")
        continue
    print("Result:", result)

