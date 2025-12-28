num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("""
Choose operation:
1) Addition (+)
2) Subtraction (-)
3) Multiplication (*)
4) Division (/)
5) Exit
""")

operation = int(input("Enter your choice: "))

match operation:
    case 1:
        result = num1 + num2
        print("Result:", result)

    case 2:
        result = num1 - num2
        print("Result:", result)

    case 3:
        result = num1 * num2
        print("Result:", result)

    case 4:
        if num2 == 0:
            print("Error: Division by zero is not allowed")
        else:
            result = num1 / num2
            print("Result:", result)

    case 5:
        print("Calculator exited")

    case _:
        print("Invalid choice")
