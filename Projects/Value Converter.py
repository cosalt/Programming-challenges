def convert_temperature():
    while True:
        print("\nChoose a conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            temp = float(input("Enter temperature in Celsius: "))
            print(f"{temp} degrees Celsius is equal to {(temp * 9 / 5) + 32} degrees Fahrenheit.\n")
            break
        elif choice == 2:
            temp = float(input("Enter temperature in Fahrenheit: "))
            print(f"{temp} degrees Fahrenheit is equal to {(temp - 32) * 5 / 9} degrees Celsius.\n")
            break
        else:
            print("Invalid input. Please try again.\n")
