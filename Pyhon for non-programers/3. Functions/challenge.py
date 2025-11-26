x = input('input x: ')
y = input('input y')

def has_remainder(x,y):
    if int(x)/int(y) %2 == 0:
        return False
    else:
        return True
    
print(has_remainder(x,y))

