#  Garrett Thompson
#  CSCI 101 - Section H
#  Python Lab 8
#  References:
#  Time: yes
import random

print('Would you like to provide your own string or generate a random one? (1 or 2)')
user_choice = int(input('CHOICE> '))
user_string = ''
if user_choice == 1:
    print('Enter a string for the game:')
    user_string = input('STRING> ')
else:
    print('Number to initialize the random generator:')
    user_seed = input('SEED> ')
    random.seed(user_seed)
    my_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for n in range(0, 6):
        user_string += random.choice(my_str)
    print(f'The randomly generated string for this game is {user_string}:')
vowel_list = ['A', 'E', 'I', 'O', 'U']
kevin = 0
stacy = 0
n = 0
length = len(user_string)

while n < len(user_string):
    if user_string[n] not in vowel_list:
        kevin += length - n
        n += 1
    else:
        stacy += length - n
        n += 1

print(f"With the string {user_string}, Kevin's score is {kevin} and Stacy's score is {stacy}")
if kevin > stacy:
    print('Kevin wins!')
    print(f'OUTPUT {kevin}')
    print(f'OUTPUT {stacy}')
    print(f'OUTPUT Kevin')
elif stacy > kevin:
    print('Stacy wins!')
    print(f'OUTPUT {kevin}')
    print(f'OUTPUT {stacy}')
    print(f'OUTPUT Stacy')
else:
    print("It's a tie!")
    print(f'OUTPUT {kevin}')
    print(f'OUTPUT {stacy}')
    print(f'OUTPUT Draw')
