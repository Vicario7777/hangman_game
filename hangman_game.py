import random
from collections import Counter

# List of possible car makes for the game
possible_answers = '''alfa romeo mercedes bmw volkswagen kia honda hyndai
                        ford audi bentley aston martin dodge toyota bugatti
                        pagani ferrari porsche lamborghini'''

# Split the possible answers into individual words
possible_answers = possible_answers.split()

# Randomly select a word from the list of possible car makes
word = random.choice(possible_answers)

if __name__ == '__main__':
    #Prompt the player to guess the word, with a hint
    print("Guess the word! HINT: It's the make of a car")

    # Display underscores for each letter of the word to be guessed
    for _ in word:
        print('_', end=' ')
    print()

    playing = True

    # Initialise variables for guessed letters, remaining chcances, correct guesses
    # and a flag for game status
    guessed_letter = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:

        # Main game loop, continues until no chances left or word is guessed
        while chances != 0 and flag == 0:
            print()
            chances -= 1

            try:

                # Allow player to input a letter guess
                guess = str(input("Enter a letter to guess: "))
            except KeyboardInterrupt:
                print()
                print("Bye! Try again.")
                exit()
            except:
                print("Enter only a letter!")
                continue

            # Validate the input letter
            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter only a SINGLE letter")
                continue
            elif guess in guessed_letter:
                print("You have already guessed that letter")
                continue

            # Handle correct guesses
            if guess in word:
                # Count occurrences of the guessed letter in the word
                k = word.count(guess)
                for _ in range(k):
                    guessed_letter += guess

            # Displaying correctly guessed letters and underscores for unguessed letters
            for char in word:
                if char in guessed_letter and Counter(guessed_letter) != Counter(word):
                    print(char, end=' ')
                    correct += 1
                elif Counter(guessed_letter) == Counter(word):
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print("Congratulations, You won!")
                    break
                else:
                    print('_', end=' ')

        # Handling the case when the player runs out of chances without guessing the word
        if chances <= 0 and Counter(guessed_letter) != Counter(word):
            print()
            print("You lost! Try again...")
            print("The word was {}".format(word))

    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()