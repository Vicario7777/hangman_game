import random
from collections import Counter

possible_answers = '''alfa romeo mercedes bmw volkswagen kia honda hyndai
                        ford audi bentley aston martin dodge toyota bugatti
                        pagani ferrari porsche lamborghini'''

possible_answers = possible_answers.split()
word = random.choice(possible_answers)

if __name__ == '__main__':
    print("Guess the word! HINT: It's the make of a car")

    for _ in word:
        print('_', end=' ')
    print()

    playing = True

    guessed_letter = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while chances != 0 and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input("Enter a letter to guess: "))
            except KeyboardInterrupt:
                print()
                print("Bye! Try again.")
                exit()
            except:
                print("Enter only a letter!")
                continue

            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter only a SINGLE letter")
                continue
            elif guess in guessed_letter:
                print("You have already guessed that letter")
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    guessed_letter += guess

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

        if chances <= 0 and Counter(guessed_letter) != Counter(word):
            print()
            print("You lost! Try again...")
            print("The word was {}".format(word))

    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()