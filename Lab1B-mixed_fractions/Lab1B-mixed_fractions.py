#   Garrett Thompson
#   CSCI 101 – Section H
#   Python Lab 1B
#   References:
#   Time: 20 minutes
print('Input the numerator of the fraction')
numerator = int(input('NUMERATOR>'))
print('Input the denominator of the fraction')
denominator = int(input('DENOMINATOR>'))
whole_number = int(numerator / denominator)
mixed_fraction = numerator % denominator
print('OUTPUT {:d} {}/{}'.format(whole_number, mixed_fraction, denominator))
