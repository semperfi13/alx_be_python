def perform_operation(num1, num2, operation):
    match operation:
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
            result = num1 / num2
        case _:
            print("Invalid operation selected.")
            exit()
    return result
