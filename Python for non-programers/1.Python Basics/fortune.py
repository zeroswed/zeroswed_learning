import random

random_number = random.randint(1,99)

fortune_messages = [
    "Today is your lucky day!",
    "You will find success in your endeavors.",
    "Happiness is around the corner.",
    "Expect the unexpected.",
    "A thrilling time is in your immediate future."
]

random_fortune = random.randint(0,4)

print(f'{fortune_messages[random_fortune]} Your lucky numner is {random_number} ')