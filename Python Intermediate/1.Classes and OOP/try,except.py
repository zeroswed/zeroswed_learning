print("before")

try:
    #4 / 0
    print(age)
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except Exception as e:
    print(e)

class Cheerse_Error(Exception):
    pass

def upper_fun(word):
    
    if len(word) <=0:
        raise Cheerse_Error('The word has to have at least one letter!')
    return word.upper()
    

print(upper_fun(''))

print('after')
