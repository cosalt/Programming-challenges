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
import forex_python.converter
import datetime

def convert_currency():
    """converts currencies between US dollars and British pounds in real time."""

    while True:
        print("\nChoose a conversion:")
        print("1. US dollars to British pounds")
        print("2. British pounds to US dollars")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = float(input("Enter currency in US dollars: "))
            now = datetime.datetime.now()
            converted_amount = forex_python.converter.convert("USD", "GBP", value)
            print(f"Time and Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{value} US dollars is equal to {converted_amount} British pounds.")
            print(f"Exchange Rate: 1 USD = {forex_python.converter.get_rate('USD', 'GBP')} GBP")
            break
        elif choice == 2:
            value = float(input("Enter currency in British pounds: "))
            now = datetime.datetime.now()
            converted_amount = forex_python.converter.convert("GBP", "USD", value)
            print(f"Time and Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{value} British pounds is equal to {converted_amount} US dollars.")
            print(f"Exchange Rate: 1 GBP = {forex_python.converter.get_rate('GBP', 'USD')} USD")
            break
        else:
            print("Invalid input. Please try again.\n")
def convert_lengths():
    """Converts lengths between centimeters and feet/inches."""

    while True:
        print("\nChoose a conversion:")
        print("1. Centimeters to feet and inches")
        print("2. Feet and inches to centimeters")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = float(input("Enter length in centimeters: "))
            inches = value / 2.54
            feet = inches // 12
            inches %= 12
            print(f"{value} centimeters is equal to {feet} feet and {inches} inches.\n")
            break
        elif choice == 2:
            feet = float(input("Enter length in feet: "))
            inches = float(input("Enter length in inches: "))
            length = (feet * 12 + inches) * 2.54
            print(f"{feet} feet and {inches} inches is equal to {length} centimeters.\n")
            break
        else:
            print("Invalid input. Please try again.\n")
