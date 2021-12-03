# define a variable to store a secret number

secret_number = 9
# define a variable
guess_count = 0
guess_limit = 3

while guess_count  < guess_limit :
    guess = int(input('Guess: '))
    guess_count += 1
    if guess ==secret_number :
        print('You won!')
        break
    else:print('Sorry you failed!')