# Exercise 19. Armstrong Number Check
num = int(input("Enter the value of Num:"))
num_string = str(num)
power = len(num_string)
total = 0

for digit in num_string:
    total += int(digit) ** power

if (total == num):
    print(f"{num} is Armstrong Number!")
else:
    print(f"{num} is not a Armstrong Number!")


# Exercise 20. Print right-angled triangle Number Pattern using a Loop
for i in range(6):
    for j in range(i):
        print(i,end=" ")
    print('')
    
# Exercise 21. Print the decreasing pattern
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("")

# Exercise 22. Print the alternate numbers pattern

for i in range(1,21,2):
    print(i)

# Exercise 23. Print Alphabet pyramid (A, BB, CCC) pattern
rows = 5
ascii_value = 65
for i in range(rows):
    letter = chr(ascii_value + i)
    for j in range(i + 1):
        print(letter,end=" ")
    print() 

# Exercise 24. Hollow square pattern
n = 5
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n-1 or j == 0 or j == n-1):
            print("^",end=" ")
        else:
            print(" ",end=" ")
    print()

n = 5
for i in range(n):
    for j in range(n):
        # Check if we are on the border
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Exercise 25. Print pyramid pattern of stars
rows = 5

# Upper part of the pattern
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

# Lower part of the pattern
for i in range(rows - 1, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print("\r")

