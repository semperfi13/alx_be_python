def perform_operation(num1, num2, operation):

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()
        result = num1 / num2
    else:
        print("Invalid operation selected.")
        exit()
    """ match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                print("Cannot divide by zero.")
                exit()
            else:
                result = num1 / num2
        case _:
            print("Invalid operation selected.")
            exit() """
    return result
