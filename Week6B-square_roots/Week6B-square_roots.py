#   Garrett Thompson
#   CSCI 102 – Section A
#   Week 6 - Lab B - Estimating Square Roots
#   References:
#   Time: 25 minutes
print('How many numbers am I estimating John?')
guess_number = int(input('COUNT> '))
print('Input each number to estimate.')
num = []
for n in range(guess_number):
    num.append(float(input('NUMBER> ')))

initial_guess = 10
better_guess = 0
square_roots_guessed = 0
i = 0
print('The square roots are as follows:')
while square_roots_guessed < guess_number:
    better_guess = (initial_guess + num[square_roots_guessed] / initial_guess) / 2
    i += 1
    if initial_guess == better_guess:
        print(f'OUTPUT After {i} iterations, {num[square_roots_guessed]}^0.5 = {better_guess:.3f}')
        initial_guess = 10
        i = 0
        square_roots_guessed += 1
    else:
        initial_guess = better_guess
