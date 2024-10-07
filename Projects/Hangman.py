import random

# list of words
words = ['python', 'java', 'hangman', 'computer', 'programming', 'science', 'mathematics']

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    wrong_attempts = 0
    max_attempts = 6
    
    print("Welcome to Hangman!")
    
    while wrong_attempts < max_attempts:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Wrong attempts: {wrong_attempts}/{max_attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            wrong_attempts += 1
            print("Wrong guess!")
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

if __name__ == '__main__':
    hangman()
