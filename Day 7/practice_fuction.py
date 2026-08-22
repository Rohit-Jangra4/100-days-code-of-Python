# Question 1
def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))

# Question 2
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("madam"))

# Question 3
def sum(num):
    sum=0
    i=0
    while i>=num:
        num+=i
        i+=1

    print(sum)

# Question 4
def sum_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total


print(sum_digits(12345))

