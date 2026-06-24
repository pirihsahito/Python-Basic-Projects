def calculate(num1, num2, opt):
    if opt == "+":
        return num1 + num2
    elif opt == "-":
        return num1 - num2
    elif opt == "x" or opt == "*":
        return num1 * num2
    elif opt == "/":
        if num2 == 0:
            return "Error: Division by 0 is undefined!"
        return num1 / num2
    else:
        return None
    
while True:
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print("To Add press '+', To Subtract press '-', To Multiply press '*' or 'x', To Devide press '/'")
        opt = input("Enter Symbol from above list: ")

        result = calculate(num1, num2, opt)

        if result is  None:
            print("You ernterd wrong symbol. Try the above given one")
        else:
            print(f"{num1} {opt} {num2} = {result}")

    except ValueError:
        print("Invalid input! Enter a number only.")

    print("-" * 30) # Visualize saparator  for  next turn

    exit = input("Press 'q' to quit or Press any key to continue: ").lower().strip()
    if exit == 'q':
        print("Thank You For Using Calculator! Goodbye!")
        break