#   Garrett Thompson
#   CSCI 102 – Section A
#   Week 5 - Lab A - Tally for Kids
#   References:
#   Time: 20 minutes

user_numbers_list = []
sum_final = 0

print('Enter values to add. Enter quit when done.')

while 'quit' not in user_numbers_list:
    user_input = input('NUMBER> ')
    if user_input != 'quit':
        user_numbers_list.append(int(user_input))
    elif user_input == 'quit':
        break
    else:
        break

print(f'The addition of the {len(user_numbers_list)} numbers entered is:')
print(f'OUTPUT {len(user_numbers_list)} numbers')
print(f'OUTPUT {sum(user_numbers_list)} total')
