import random
import time

print('Welcome to the guessing games. I will going to pick a number between 1 and 100.')
time.sleep(3)
print('Picking a number ...')
time.sleep(2)

correct_guess = int(random.randint(1, 100))

guess = 0
tries = 0

while guess != correct_guess:
    time.sleep(1)
    tries += 1
    guess = int(input('Enter your guess from 1 - 100: '))
    if guess < correct_guess:
        print('guess higher')
    elif guess > correct_guess:
        print('guess lower')    
    else:
        print(f'You guesss is right, correct guess is {correct_guess} and it took you {tries} tries!!')
    
