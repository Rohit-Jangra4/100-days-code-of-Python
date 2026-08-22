# Now we learn about function so function is two types in python first is built in function and second is user defind function.

# problem 1

def greet():
    print("Hello,Python")


greet()

# Problem 2
def greet(name):
    print("Hello",name)

greet("Rohit Jangra")

# Problem 3
def sum(a,b):
    sum_two_numbers=(a+b)
    print(sum_two_numbers)

sum(5678,9865)

# Problem 4

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(15))

# Problem 5
def square(num):
    x=num*num
    print(x)

square(45)

# Problem 6
def largest(a,b):
    if a>b:
        print("A greater than B")
    else:
        print("B greater than A")

largest(567575,989696)

# Problem 7
def fact(num):
    result=1
    for i in range(1,num+1):
        result*=i

    print(result)

fact(5)

# Problem 8
def count_vowels(text):
    count=0
    for char in text:
        if char.lower() in "aeiou":
            count+=1

    return count

print(count_vowels("Python Programming"))

# Problem 9
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime(17))

# MINI CALCULATOR

def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation=="+":
    print(sum(num1,num2))

elif operation=="*":
    print(multiply(num1+num2))

elif operation=="-":
    print(subtract(num1+num2))

elif operation == "/":
    if num2 != 0:
        print(divide(num1/num2))
    else:
        print("Zero division Error")

else:
    print("Invalid Operation")

