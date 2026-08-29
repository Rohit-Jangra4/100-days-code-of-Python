# Utility Tools for Day 1

# Random Number
import random
random_number = random.randrange(1,10)
print("Random number between 1 and 10:", random_number)

# calulator module
import calculator
result = calculator.add(5, 3)
print("The result of addition is:", result)

#Date and Time module
import datetime
current_date = datetime.datetime.now()
print("Current date and time:", current_date)

# Random Password
import random
password_length = 8
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
print("Generated password:", password)

# Exit the program
import sys 
sys.exit()
