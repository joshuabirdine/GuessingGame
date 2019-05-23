import random


print('-------------------------------------')
print('         Guessing Game App           ')
print('-------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
name = input('Player what is your name?')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100:')
    #turns the input into a integer
    guess = int(guess_text)
    #turns the input into a string
    # guess_str = str(guess_text)



    if guess < the_number :
        # print('To low, your number: ' + guess_str)
        # Using string format to convert to strings, and use indexing to add to string
        print('Sorry {1}, your guess of {0} was too low.'.format(guess, name))
    elif guess > the_number:
        # print('To high, your number: ' + guess_str)
        print('Sorry {1}, your guess of {0} was to high'.format(guess, name))
    else:
        # print('You win, your number: ' + guess_str)
        print('You won {1}, with the guess of {0}!'.format(guess, name))

print('done')


