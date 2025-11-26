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
    

#print(upper_fun('qwer'))

print('after')

class Snotty_error(Exception):
    print('This is a snotty error!')    

def bogus(x):
    try:
        x = int('hello')
        return x
    except:
        raise Snotty_error()
bogus('1')