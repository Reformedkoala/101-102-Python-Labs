#   Garrett Thompson
#   CSCI 102 – Section A
#   Week 2 - Lab A - Simple Calculator
#   References:
#   Time: 30 minutes
print('Input the first operand')
operand_one = float(input('FIRST>'))
print('Input the second operand')
operand_two = float(input('SECOND>'))

sum = operand_one + operand_two
difference = operand_one - operand_two
quotient = int(operand_one / operand_two)
product = operand_one * operand_two
remainder = operand_one % operand_two

print('The sum of {:.1f} and {:.1f} is {:.1f}'.format(operand_one, operand_two, sum))
print('OUTPUT {:.1f}'.format(sum))
print('The difference of {:.1f} and {:.1f} is {:.1f}'.format(operand_one, operand_two, difference))
print('OUTPUT {:.1f}'.format(difference))
print('The product of {:.1f} and {:.1f} is {:.1f}'.format(operand_one, operand_two, product))
print('OUTPUT {:.1f}'.format(product))
print('The quotient of {:.1f} and {:.1f} is {:d}'.format(operand_one, operand_two, quotient))
print('OUTPUT {:d}'.format(quotient))
print('The remainder of {:.1f} and {:.1f} is {:.2f}'.format(operand_one, operand_two, remainder))
print('OUTPUT {:.2f}'.format(remainder))
