import random

ROCK = 'rock'
PAPER = 'paper'
SCISSOR = 'scissor'
choices = [ROCK, PAPER, SCISSOR]
positive = [[PAPER, ROCK], [SCISSOR, PAPER], [ROCK, SCISSOR]]
negative = [[ROCK, PAPER], [PAPER, SCISSOR], [SCISSOR, ROCK]]

def get_computer_move():
    move = random.choice(choices)
    return move

def find_winner(user_move, computer_move):
    if [user_move, computer_move] in positive:
        return 1
    elif [user_move, computer_move] in negative:
        return -1
    return 0

while True:
    choice = input("Do you wanna play (y/n): ")
    if 'y' in choice.lower():
        computer_move = get_computer_move()
        while True:
            move = input("Select a move ('r' for rock/'p' for paper/'s' for scissor): ").lower()
            print(f"Computer's Move: {computer_move}")
            if 'r' in move or 'p' in move or 's' in move():
                if 'r' in move:
                    user_move = ROCK
                elif 'p' in move:
                    user_move = PAPER
                elif 's' in move:
                    user_move = SCISSOR
                print(f"User Move: {user_move}")
                output = find_winner(user_move, computer_move)
                if output == 1:
                    print("You Won1!!!11!!1!1!!")
                elif output == -1:
                    print("Computer Won!!!1!!1!!")
                else:
                    print("Tie !!!")
                break
            else:
                print("Invalid input")
