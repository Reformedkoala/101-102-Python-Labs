#   Tracy Camp
#   CSCI 102 – Section A
#   Week 2 - Lab B - List Slicing
#   References:
#   Time: 25 minutes
print('Enter your string:')
user_string = input('STRING>')
print('Enter four numbers to slice the string')
string_slice_zero = int(input('A>'))
string_slice_fixed_one = string_slice_zero + 1
string_slice_one = int(input('B>'))
string_slice_two = int(input('C>'))
string_slice_fixed_two = string_slice_two + 1
string_slice_three = int(input('D>'))
print('OUTPUT', user_string[string_slice_fixed_one:string_slice_one], user_string[string_slice_fixed_two:string_slice_three])
