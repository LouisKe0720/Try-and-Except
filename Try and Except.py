number = (input("Enter a number: "))

while True:
    try:
        number = int(number)
        print(number * 10)
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
        number = (input("Enter a number: "))

#Challenge

def main():
    number1 = input("Enter a number: ")
    while True:
        try:
            number1 = float(number1)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")
    while True:
        try:
            number2 = float(number2)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            number2 = input("Enter another number: ")
    operation = input("Enter an operator (+, -, *, /): ")
    while operation not in ["+", "-", "*", "/"]:
        print("Invalid input. Please enter a valid operator.")
        operation = input("Enter an operator (+, -, *, /): ")
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 == 0:
            print("Error: Division by zero.")
            print("Exiting...")
            print("Would you like to calculate again? (yes/no)")
            exit_choice = input().lower()
            if exit_choice == "no":
                print("Exiting...")
                return
            elif exit_choice == "yes":
                main()
        result = number1 / number2
    print("The result is:", result)
    print("Would you like to perform another calculation? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        main()
    elif answer == "no":
        print("Goodbye!")
        return
main()
        

