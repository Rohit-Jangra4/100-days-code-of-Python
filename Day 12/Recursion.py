# Basically it is used to call itself function

def factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(23))
print(factorial(34))
print(factorial(67))
print(factorial(89))
print(factorial(87))
print(factorial(99))
print(factorial(98))
print(factorial(78))
print(factorial(88))

# sum of n numbers
def sum_n(num):
    if num==0:
        return 0
    else:
        return num + sum_n(num-1)

print(sum_n(56))

# Reverse a string
def reverse_string(text):

    if len(text) <= 1:
        return text
    else:
        return text[-1] + reverse_string(text[:-1])


print(reverse_string("python"))

# Fibonnaci Problem
def term(n):

    if n == 0 or n == 1:
        return n

    else:
        return term(n-1) + term(n-2)


print(term(6))

# Digit count
def count_digits(n):

    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)


print(count_digits(12345))