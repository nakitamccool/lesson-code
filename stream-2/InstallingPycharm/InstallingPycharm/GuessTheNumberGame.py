#!/usr/bin/python3

import random

NUMBER_OF_GUESSES = 10
RANGE = 10

while True:
    # generate the random number
    random_number = random.randint(0, RANGE)

    # give the user a certain amount of guesses
    for i in range(NUMBER_OF_GUESSES):
        print('Guess a number: ')
        guess = int(input())
        if guess == random_number:
            print('well done')
            break
        elif guess > random_number:
            print('too high')
        else:
            print('too low')

    print('Let\'s try a new number!')