#   Garrett Thompson
#   CSCI 102 – Section A
#   Week 8 - Lab A - Rolling a Die
#   References: None
#   Time: 15 Minutes

import random

print('Input the number of sides of the die:')
side_die = int(input('SIDES> '))
print('Input the number of rolls to make:')
num_rolls = int(input('ROLLS> '))
print('Input the seed for the random number generator:')
seed_of_num = int(input('SEED> '))
rolls_list = []
current_num = 0
random.seed(seed_of_num)

for n in range(0, num_rolls):
    current_num = random.randint(1, side_die)
    rolls_list.append(current_num)

print(f'Your {num_rolls} rolls of a {side_die}-sided die follow:')
for u in range(1, side_die + 1):
    print(f'OUTPUT {u} occurred {rolls_list.count(u)} times')
