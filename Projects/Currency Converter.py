from currencyconverter import CurrencyConverter

def convert_currency(base_currency, target_currency, amount):
    """Converts currencies in real time.

    Args:
        base_currency (str): The base currency to convert from.
        target_currency (str): The target currency to convert to.
        amount (float): The amount to convert.

    Returns:
        float: The converted amount.
    """

    try:
        converter = CurrencyConverter()
        converted_amount = converter.convert(amount, base_currency, target_currency)
        return converted_amount
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    while True:
        print("\nChoose a conversion:")
        base_currency = input("Enter the base currency code:").upper()
        target_currency = input("Enter the target currency code:").upper()
        amount = float(input("Enter the amount to convert:" ))

        converted_amount = convert_currency(base_currency, target_currency, amount)
        print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}.\n")

if __name__ == "__main__":
    main()
