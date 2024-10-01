import time
def set_countdown():
    seconds = int(input("Enter the number of seconds: "))
    print("Countdown starts now...")
    for i in range(seconds, 0, -1):
        print(f"\r{i:02d} seconds remaining", end="")
        time.sleep(1)
    print("\nCountdown complete!\n")
def main():
    print("Countdown Timer.")
    while True:
        choice = input("Do you want to set a countdown (y/n): ").lower()
        if choice == "y":
            set_countdown()
        elif choice == "n":
            print("Exiting...")
            break
        else:
            print("Invalid input. Please try again.")
if __name__ == "__main__":
    main()
