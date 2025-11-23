def even_number_sum():   
#    numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
    even_numbers = []
    numbers = input("Enter numbers: ").split(' ')
    numbers = [int(num) for num in numbers]
    for number in numbers:
        if number %2 == 0:
            even_numbers.append(number)

    

    
    return print(sum(even_numbers))

even_number_sum().even_numbers
    