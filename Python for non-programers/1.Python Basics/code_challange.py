number = int(input("Enter a number: "))

remainder = number % 2

if remainder == 1:
    print("Number is odd")
else:
    print("Number is even")

print(remainder)