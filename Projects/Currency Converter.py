import forex_python.converter

def convert_currency(base_currency, target_currency, amount):
    """Converts currencies in real time.

    args:
        base_currency (str) - the base currency to convert from.
        target_currency (str) - the target currency to convert to.
        amount (float) = the amount to convert.

    returns:
        float - the converted amount.
    """

    try:
        converted_amount = forex_python.converter.convert(base_currency, target_currency, amount)
        return converted_amount
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    while True:
        print("\nChoose a conversion:")
        print("Enter the base currency code:")
        base_currency = input().upper()
        print("Enter the target currency code:")
        target_currency = input().upper()
        print("Enter the amount to convert:")
        amount = float(input())

        converted_amount = convert_currency(base_currency, target_currency, amount)
        print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}.\n")

if __name__ == "__main__":
    main()
