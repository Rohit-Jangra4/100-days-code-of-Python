# Now today we learn about doc string

# Question 1
def greet(name):
    '''this greet function take a value
name'''
    print("Hello! Mr.",name)

greet("Rohit Jangra")

# Now we check our doc string
print(greet.__doc__)

# Calculator function
def add(a=23,b=45):
    '''function add is work as adding two numbers and 
its parameters is a and b it print the value of sum'''
    sum=a+b
    print(f"Sum of {a} and {b} is:{sum}")

add()
print(add.__doc__)

# Check Even or Odd
def check_even_odd(num):
    '''This function tells us about number is 
Even or Odd and num is its value it return the number is Even or Odd'''
    if num%2==0:
        return "Even"
    else:
        return "Odd"

result = check_even_odd(8465416685)
print(result)

#Find Maximum
def three_num(a, b, c):
    '''This function finds and displays the greatest among three numbers.'''

    if a >= b and a >= c:
        print(f"A is greatest // A:{a}, B:{b}, C:{c}")
    elif b >= a and b >= c:
        print(f"B is greatest // A:{a}, B:{b}, C:{c}")
    else:
        print(f"C is greatest // A:{a}, B:{b}, C:{c}")


three_num(56345687, 53767543, 767812345)

# factorial of a number 
def fact(num):
    '''this fact tell us about the num this num is input from
the user and find the reuslt of factorial'''
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(fact(5))

# Temprature converter
def celsius_to_fahrenheit(celsius):
    '''in celsius_to_fahrenheit this function tell us about celsius it is used to convert 
celsius to fahrenheit and parameter celsius formula used in it is F=(C*9/5)+32 '''
    F=(celsius*9/5)+32

    print(f"the value of fahrenheit in celsuis is={F}")

celsius_to_fahrenheit(25)

# MINI DOCUMENTATION CHALLENGE

def square(num):
    """Returns the square of the given number."""
    return num * num


def cube(num):
    """Returns the cube of the given number."""
    return num ** 3


def is_prime(num):
    """Checks whether the given number is a prime number."""

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# Taking input from user
num = int(input("Enter a number: "))

# Calling functions
print(f"Square of {num} is: {square(num)}")
print(f"Cube of {num} is: {cube(num)}")

if is_prime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not a Prime Number")


# Checking docstrings
print("\n--- Documentation ---")

print("Square:", square.__doc__)
print("Cube:", cube.__doc__)
print("Is Prime:", is_prime.__doc__)