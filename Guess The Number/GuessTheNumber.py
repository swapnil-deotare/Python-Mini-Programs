from ast import Expression
import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))

        if guess< random_num:
            print('Sorry, Guess again. Too Low!')
        elif guess > random_num:
            print('Sorry, Guess again. Too High!')    
    print('Yay, congrats! you made it!')

guess(10)        

print('\nNow its my turn to guesss the number. Think of a number between 1 to 10!')

def compupter_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        feedback = input(f'Is {guess} too High(h), too Low(l), or Correct(c)!')

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1    

    print(f"I guessed your number: {guess}")
    print("I may be a machine, but I am smarter than you!")

compupter_guess(10)            