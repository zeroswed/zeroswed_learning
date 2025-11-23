user_text = input('Enter some text:')

print(user_text.upper())

user_number = input('what do you want to double?')

print(int(user_number) * 2)


user_input = input('enter the txt: ')
font_size = input('would you like this to be lower or upper?')

if font_size == 'lower':
    print(user_input.lower())
else:
    print(user_input.upper())