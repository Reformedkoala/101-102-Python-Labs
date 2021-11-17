#  Garrett Thompson
#  CSCI 102 – Section A
#  Week 7 - Lab A - Checkerboard
#  References:
#  Time: 30 minutes
print('How many rows does the checkerboard have?')
num_rows = int(input('ROWS> '))
print('How many columns does the checkerboard have?')
num_col = int(input('COLUMNS> '))
print('What are the strings with which to pattern it?')
first_string = input('FIRST> ')
second_string = input('SECOND> ')
print(f'A checkerboard with {num_rows} rows, {num_col} columns, first string is {first_string}, \
and second string is {second_string} is:')
i = 0
total_list = []
while i < num_rows:
    if (i % 2) == 0:
        for n in range(num_col):
            if (n % 2) == 0:
                total_list.append(first_string)
            else:
                total_list.append(second_string)
        i += 1
    else:
        for k in range(num_col):
            if (k % 2) == 0:
                total_list.append(second_string)
            else:
                total_list.append(first_string)
        i += 1

i = 0
two_d_list = []
while i < num_rows:
    if (i % 2) == 0:
        print(f'OUTPUT {total_list[0:num_col]}')
        two_d_list += [total_list[0:num_col]]
        i += 1
    else:
        print(f'OUTPUT {total_list[num_col:(num_col + num_col)]}')
        two_d_list += [total_list[num_col:(num_col + num_col)]]
        i += 1
print('And the 2D array representation is:')
print(f'OUTPUT {two_d_list}')
