#   Garrett Thompson
#   CSCI 102 – Section A
#   Week 1 - Part B
#   References:
#   Time: 30 minutes
print('Input the total length of fencing available in yards')
length = int(input('LENGTH>'))
length_feet = length * 3
individual_leg = length_feet / 4
max_area = round(individual_leg ** 2, 1)
print('The maximum area that can be made is:')
print('OUTPUT', max_area)
