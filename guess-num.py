import random

def get_guess(num_try):
    guess = -1
    while guess < 1 or guess > 100:
        try:
            guess = int(input("Input a guess between 1 - 100: "))
            num_try += 1
        except NameError as ne:
            print("Invalid input type! Please input your guess as an integer!")
    return guess, num_try

def handle_hint(ans, guess):
    if guess > ans:
        print("You guessed high!")
    elif guess < ans:
        print("You guessed low!")
    else:
        print("You guessed right!")

if __name__ == "__main__":
    ans = random.randrange(1, 101)
    num_try = 0
    print("Guess the number from 1 - 100.")
    guess, num_try = get_guess(num_try)
    handle_hint(ans, guess)
    while guess != ans:
        guess, num_try = get_guess(num_try)
        handle_hint(ans, guess)
    print("You found the answer after {0:d} tries!".format(num_try))