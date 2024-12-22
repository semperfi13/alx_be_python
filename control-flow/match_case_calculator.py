num1 = int(input("Enter the first number:"))

num2 = int(input("Enter the second number:"))

operation_type = input("Choose the operation (+, -, *, /):")


if num2 == 0 and operation_type == "/":

    print("Cannot divide by zero.")

else:

    match operation_type:

        case "+":
            result = num1 + num2
            print("The result is " + str(result))
        case "-":
            result = num1 - num2
            print("The result is " + str(result))
        case "*":
            result = num1 * num2
            print("The result is " + str(result))
        case "/":
            result = num1 / num2
            print("The result is " + str(result))
        case _:
            print("Invalid choice")

