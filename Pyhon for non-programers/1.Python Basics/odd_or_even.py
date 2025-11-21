number = int(input('Chose a number you want to be examened: '))

remainder = number %4

if remainder == 1:
    print('number is odd')
else:
    print('nuber is even')