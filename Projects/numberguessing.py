import random

def get_random_number():
    return random.randint(0, 9)

def play_game():
    chances = 0
    random_number = get_random_number()

    while True:
        chances += 1
        user_number = int(input("Enter the number you think it is: "))

        if user_number not in range(0, 10):
            print("Invalid input!")
        elif user_number == random_number:
            print(f"Congratulations! You got the number in {chances} chances\n")
            break
        elif abs(user_number - random_number) <= 4:
            print(f"Close, try a {'lower' if user_number > random_number else 'higher'} number")
        else:
            print(f"Far from, try a {'lower' if user_number > random_number else 'higher'} number")

while True:
    choice = input("Do you wanna play (y/n): ").lower()
    if choice == 'y':
        play_game()
    elif choice == 'n':
        print("end. ")
        break
    else:
        print("Invalid input!")
