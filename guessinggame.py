import random


print('-------------------------------------')
print('         Guessing Game App           ')
print('-------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100:')
    #turns the input into a integer
    guess = int(guess_text)
    #turns the input into a string
    guess_str = str(guess_text)
    count += 1


    if guess < the_number :
        print('To low, your number: ' + guess_str)
    elif guess > the_number:
        print('To high, your number: ' + guess_str)
    else:
        print('You win, your number: ' + guess_str)

print('done')


