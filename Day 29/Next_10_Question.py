#Exercise 11. Reverse a string using a for loop (no slicing)
# string = "Python"
# reverse = ""
# for char in string:
#     reverse = char + reverse 

# print(f"Orginial String {string}")
# print(f"Rversed String {reverse}")

#Exercise 12. Count vowels and consonants in a sentence
# string = "Loops are Fun!"
# vowels = "aeiou"
# v_count = 0
# c_count = 0

# for char in string.lower():
#     if char in vowels:
#         v_count += 1
#     else:
#         c_count += 1

# print(f"Number of count of Vowels:{v_count}")
# print(f"Number of count of Constant:{c_count}")  

#Exercise 13. Count total number of digits in a number
# num = int(input("Enter the value of N:"))
# count = 0

# while num != 0:
#     num = num // 10
#     count = count + 1

# print("Total digits are:", count)

#Exercise 14. Reverse an integer number
# num = int(input("Enter the  value of Num:"))
# reverse = 0
# while(num>0):
#     digit = num % 10
#     reverse = (reverse*10) + digit

#     num = num // 10

# print(f"Rversed value is:{reverse}")

#Exercise 15. Find largest and smallest digit in a number
# num = int(input("Enter the value of Num:"))
# largest = 0
# smallest = 9

# while num > 0:
#     digit = num % 10
#     if digit > largest:
#         largest = digit
#     if digit < smallest:
#         smallest = digit
        
#     num = num // 10

# print("Largest digit:", largest)
# print("Smallest digit:", smallest)

#Exercise 16. Check if a number is a palindrome
number = int(input("Enter the value of Number:"))
temp = number
reverse_num = 0

while number > 0:
    digit = number % 10
    reverse_num = (reverse_num * 10) + digit
    number = number // 10

if temp == reverse_num:
    print("Yes. Given number is palindrome number")
else:
    print("No. Given number is not palindrome")

#Write a program for factorial
num = 5
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")

#Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1
n = 6
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3 * n) + 1
    print(f", {n}", end="")

