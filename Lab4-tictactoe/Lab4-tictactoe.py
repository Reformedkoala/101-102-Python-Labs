#   Garrett Thompson
#   CSCI 101 – Section H
#   Python Lab 4
#   References:
#   Time: 20 Minutes
row_0 = input('ROW0> ')
row_1 = input('ROW1> ')
row_2 = input('ROW2> ')

# X Horizontal Lines
if 'X' in row_0[0] and 'X' in row_1[0] and 'X' in row_2[0]:
    print('OUTPUT X')
elif 'X' in row_0[1] and 'X' in row_1[1] and 'X' in row_2[1]:
    print('OUTPUT X')
elif 'X' in row_0[2] and 'X' in row_1[2] and 'X' in row_2[2]:
    print('OUTPUT X')

# X Vertical Lines
elif 'X' in row_0[0] and 'X' in row_0[1] and 'X' in row_0[2]:
    print('OUTPUT X')
elif 'X' in row_1[0] and 'X' in row_1[1] and 'X' in row_1[2]:
    print('OUTPUT X')
elif 'X' in row_2[0] and 'X' in row_2[1] and 'X' in row_2[2]:
    print('OUTPUT X')

# X Diagonals
elif 'X' in row_0[0] and 'X' in row_1[1] and 'X' in row_2[2]:
    print('OUTPUT X')
elif 'X' in row_0[2] and 'X' in row_1[1] and 'X' in row_2[0]:
    print('OUTPUT X')

# O Horizontal Lines
elif 'O' in row_0[0] and 'O' in row_1[0] and 'O' in row_2[0]:
    print('OUTPUT O')
elif 'O' in row_0[1] and 'O' in row_1[1] and 'O' in row_2[1]:
    print('OUTPUT O')
elif 'O' in row_0[2] and 'O' in row_1[2] and 'O' in row_2[2]:
    print('OUTPUT O')

# O Vertical Lines
elif 'O' in row_0[0] and 'O' in row_0[1] and 'O' in row_0[2]:
    print('OUTPUT O')
elif 'O' in row_1[0] and 'O' in row_1[1] and 'O' in row_1[2]:
    print('OUTPUT O')
elif 'O' in row_2[0] and 'O' in row_2[1] and 'O' in row_2[2]:
    print('OUTPUT O')

# O Diagonals
elif 'O' in row_0[0] and 'O' in row_1[1] and 'O' in row_2[2]:
    print('OUTPUT O')
elif 'O' in row_0[2] and 'O' in row_1[1] and 'O' in row_2[0]:
    print('OUTPUT O')

# board full no winner
else:
    print('OUTPUT N')
