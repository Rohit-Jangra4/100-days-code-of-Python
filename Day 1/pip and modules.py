# Math module
import math
x=int(input("Enter a number: "))
# calculate square root
sqrt=math.sqrt(x)
factorial=math.factorial(x)
print("The square root of", x, "is", sqrt)
print("The factorial of", x, "is", factorial)

# Random Number Generator function:randint,randrange,shuffle,choice
import random
random_number=random.randint(1,100)
print("Random number between 1 and 100:", random_number)

# Random password generator
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a random password of length 12
password = generate_password(12)
print("Generated password:", password)

# Date and Time module
import datetime
current_time = datetime.datetime.now()
print("Current date and time:", current_time)

# Custom module

import calculator
result = calculator.add(5, 3)
print("The result of addition is:", result)

result = calculator.subtract(10, 4)
print("The result of subtraction is:", result)

multiplication_result = calculator.multiply(6, 7)
print("The result of multiplication is:", multiplication_result)

division_result = calculator.divide(15, 3)
print("The result of division is:", division_result)

                                        #level 2

# imort emoji module
import emoji
print(emoji.emojize("Hello, World! :thumbs_up:"))

#
