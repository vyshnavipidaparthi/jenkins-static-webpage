import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
operation = int(sys.argv[3])

match operation:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 * num2)
    case 4:
        if num2 == 0:
            print("Division by zero")
        else:
            print(num1 / num2)
    case _:
        print("Invalid operation")
