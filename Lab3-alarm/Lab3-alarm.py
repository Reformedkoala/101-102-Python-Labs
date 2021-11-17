#   Garrett Thompson
#   CSCI 101 – Section H
#   Python Lab 3
#   References:
#   Time: 35 minutes

hours = int(input('HOURS>'))
minutes = int(input('MINUTES>'))

if hours != 0 and hours < 11 and minutes <= 39:
    print(f'OUTPUT 0{hours - 1} {60 + (minutes - 40)}')

elif hours != 0 and hours < 10 and 40 <= minutes <= 49:
    print(f'OUTPUT 0{hours} 0{minutes - 40}')

elif hours != 0 and hours < 10 and 50 <= minutes <= 59:
    print(f'OUTPUT 0{hours} {minutes - 40}')

elif hours == 10 and 40 <= minutes <= 49:
    print(f'OUTPUT {hours} 0{minutes - 40}')

elif hours == 10 and 50 <= minutes <= 59:
    print(f'OUTPUT {hours} {minutes - 40}')

elif hours == 0 and minutes <= 39:
    print(f'OUTPUT {hours + 23} {60 + (minutes - 40)}')

elif hours == 0 and 40 <= minutes <= 49:
    print(f'OUTPUT 0{hours} 0{minutes - 40}')

elif hours == 0 and 50 <= minutes <= 59:
    print(f'OUTPUT {hours} {minutes - 40}')

elif 10 <= hours <= 23 and minutes <= 39:
    print(f'OUTPUT {hours - 1} {60 + minutes - 40}')

elif 10 <= hours <= 23 and 40 <= minutes <= 49:
    print(f'OUTPUT {hours} 0{minutes - 40}')

elif 10 <= hours <= 23 and 50 <= minutes <= 59:
    print(f'OUTPUT {hours} {minutes - 40}')

else:
    print('Incorrect Input')
