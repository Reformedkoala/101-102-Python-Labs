#   Garrett Thompson
#   CSCI 102 – Section H
#   Week 3 - Lab B - Enhanced Calculator
#   References: Cannibalized my code from the simple calculator lab
#   Time: 30 minutes

print('Welcome to the enhanced version of last weeks calculator.')

print('Input the first operand')
operand_one = float(input('FIRST>'))

print('Input the second operand')
operand_two = float(input('SECOND>'))

print('Choose one of the following operations:')
print('  1 - addition')
print('  2 - subtraction')
print('  3 - multiplication')
print('  4 - division')
operation = int(input('OPERATION>'))

if operation == 1:
    sum = operand_one + operand_two
    print('the result of the sum is: {:.6f}'.format(sum))
    print('OUTPUT {:.6f}'.format(sum))
elif operation == 2:
    difference = operand_one - operand_two
    print('The result of the subtraction is: {:.6f}'.format(difference))
    print('OUTPUT {:.6f}'.format(difference))
elif operation == 3:
    product = operand_one * operand_two
    print('The result of the multiplication is: {:.6f}'.format(product))
    print('OUTPUT {:.6f}'.format(product))
elif operation == 4:
    quotient = int(operand_one / operand_two)
    remainder = operand_one % operand_two
    print('The result of the division is: {:.0f} (quotient) and {:.0f} (remainder)'.format(quotient, remainder))
    print('OUTPUT {:d}'.format(quotient))
    print('OUTPUT {:.0f}'.format(remainder))
else:
    print('OUTPUT Invalid Operation')
print('Thank you for using my calculator')
