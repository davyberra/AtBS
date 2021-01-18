import random
import logging

logging.basicConfig(level=logging.DEBUG)

def take_guess(i):
    guess = ''
    score = 0
    coin_sides = ['heads', 'tails']
    for _ in range(i):
        while guess not in ('heads', 'tails'):
            print('Guess the coin toss! Enter heads or tails:')
            guess = input()

        toss = random.randint(0, 1) # 0 is tails, 1 is heads
        logging.debug(f"Guess is {guess} | Toss is {coin_sides[toss]}.")
        if guess == coin_sides[toss]:
            print('You got it!')
            score += 1
        else:
            print('Nope! Guess again!')
        guess = ''

    if score > (i / 2):
        print(f"Nice job! You got {score} out of {i} correct!")
    else:
        print(f"Sorry, you're not very good at this. You only got {score} out of {i} correct.")

take_guess(5)