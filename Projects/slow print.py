import time

def exit_message(time, message):
    """Prints an exit message with a delay of 5 seconds per letter."""

    message = message
    for letter in message:
        print(letter, end="", flush=True)
        time.sleep(time)
    print()

if __name__ == "__main__":
    message = input("Message: ")
    delay = float(input("Enter the delay time in seconds: "))
    exit_message(delay, message)
