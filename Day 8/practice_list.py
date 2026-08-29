# Question 1
list = [34, 56, 778, 55, 67, 353, 678, 66575, 45]

sum = 0

for i in list:
    sum += i

print(sum)

# Question 2
numbers=[435,64556,67,57,353,8457,7897,456]
largest = numbers[0]
smallest = numbers[0]

for i in numbers:

    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)

# Question 3
lis1 = [234, 354, 465, 67867, 345345, 4568, 494745, 756, 9, 56416]

Even = 0
Odd = 0

for i in lis1:

    if i % 2 == 0:
        Even += 1
    else:
        Odd += 1

print("Even numbers:", Even)
print("Odd numbers:", Odd)
    
