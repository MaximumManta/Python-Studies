import random

word_list = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(word_list)

print("Guess the word!")

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('*', end=' ')
            failed += 1

    if failed == 0:
        print("\nCongratulations! You guessed the word.")
        break

    guess = input("\nGuess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong guess. You have", turns, "more guesses.")

        if turns == 0:
            print("Game Over! The word was:", word)
