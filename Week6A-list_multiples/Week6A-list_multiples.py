#   Garrett Thompson
#   CSCI 102 – Section A
#   Week 6 - Lab A - List of Multiples
#   References:
#   Time: 20 minutes
print('Enter the number to create multiples for.')
num = int(input('NUMBER> '))
print('Enter the maximum index of the list.')
max_index = int(input('INDEX> '))
output_list = []
temp_num = 0

for n in range(1, max_index + 2):
    temp_num = num
    temp_num *= n
    output_list.append(temp_num)

print('OUTPUT', output_list)
