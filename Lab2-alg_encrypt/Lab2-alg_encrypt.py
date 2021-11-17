#  Garrett Thompson
#  CSCI 101 – Section H
#  Python Lab 2
#  Reference:
#  Time: 30 minutes
print('Input the fives lists of characters to be encrypted.')

List1 = str(input('LIST1> '))
List2 = str(input('LIST2> '))
List3 = str(input('LIST3> '))
List4 = str(input('LIST4> '))
List5 = str(input('LIST5> '))

List1_encoded = List1[-2:], List1[0:-2]

print('The encrypted message is:')
print(
    f'OUTPUT {List5[0:2]} {List1[-2:]}{List1[0:-2]}{List2[0:-2]}{List3[len(List3) // 2:]}{List4[0:2]}{List4[4]}'
    f'{List4[3]}{List4[2]}{List4[5:]} {List5[2:4]}')
