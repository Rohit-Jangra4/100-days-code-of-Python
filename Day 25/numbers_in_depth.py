#1. Operator Precedence + Boolean Logic
# Question 1
x = 10
y = 20
z = 30

result = x < y < z and not (x + y > z) or y == 20

print(result)

# Question 2
a = True
b = False

result = a + b + True * 5 - False

print(result)
print(type(result))

# Question 3
x = 5

print(1 < x < 10)
print(1 < x == 5 < 10)
print(10 > x > 3)

# Question 4
# floor() vs trunc()
import math

numbers = [4.9, -4.9, 4.1, -4.1]

for n in numbers:
    print(n, math.floor(n), math.trunc(n))

# Question 5
n = 2 ** 1000

print(n)
print(len(str(n)))

x = 999999999999999999999999999999999
y = 888888888888888888888888888888888

print(x * y)

# Question 6
x = 0.1
y = 0.2

print(x + y == 0.3)
# we expect this to be True, but due to floating point precision issues, it may not be.
# we can use from decimal import Decimal to get a more accurate result
from decimal import Decimal

x = Decimal("0.1")
y = Decimal("0.2")

print(x + y == Decimal("0.3"))

# Question 7
from decimal import Decimal, getcontext

getcontext().prec = 20

x = Decimal(1)
y = Decimal(7)

print(x / y)

# Question 8
from fractions import Fraction

a = Fraction(2, 3)
b = Fraction(4, 9)
c = Fraction(5, 6)

result = a + b * c

print(result)

# -------------------------------------------
from fractions import Fraction

a = Fraction(2, 3)
b = Fraction(4, 9)
c = Fraction(5, 6)

result1 = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 6)
print(result1)

# Question 9
print(int("101101", 2))
print(int("745", 8))
print(int("2AF", 16))
print(int("255",8))
print(int("255",10))
print(int("255",2))

# Question 10
z1 = 3 + 4j
z2 = 1 - 2j

print(z1 + z2)
print(z1 * z2)
print(z1.real)
print(z1.imag)

# Question 11
import random
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(random.choice(list))
print(random.shuffle(list))
x = random.sample(list, 5)
print(x)
import random

# Step 1: Create numbers from 1 to 20
numbers = list(range(1, 21))

# Step 2: Select 5 random numbers
selected = random.sample(numbers, 5)

# Step 3: Print the selected numbers
print("Selected numbers:", selected)

# Step 4: Calculate their sum
total = sum(selected)
print("Sum:", total)

# Step 5: Find the largest number
largest = max(selected)
print("Largest:", largest)

# Step 6: Find the smallest number
smallest = min(selected)
print("Smallest:", smallest)





# Question 12
students_python = {"Amit", "Rahul", "Priya", "Neha", "Karan"}
students_java = {"Rahul", "Neha", "Vikas", "Karan", "Riya"}
print(students_python.intersection(students_java))
print(students_python)
print(students_java)

