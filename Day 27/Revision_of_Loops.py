# While Loops

# Begining of Loops

i = 1
while (i <= 50):
    print("Rohit",i)
    i+=1

i = 1
while (i <=10):
    print(i)
    i+=1

# Question 1
n = int(input("Enter the value of N:"))
i = 1
while (i<=10):
    print(f"{n} x {i:2d} = {n * i:3d}")
    i+=1

# Question 2
l = ["Harry","Soham","Sachin","Rohan"]
for i in l:
    if (i.startswith("S")):
        print(f"Welcome! {i}")

# Question 3
n = int(input("Enter the value of N: "))
for i in range(1, 11):
    print(f"{n} x {i:2d} = {n * i:3d}")

# Question 4
num = int(input("Enter the value of Num:"))
for i in range(2,num):
    if (num % i == 0):
        print("Not Prime Number.")
else:
    print("Prime Number.")

# Question 5
natural = int(input("Enter the value of N:"))
i = 1
sum = 0
while (i <= natural):
    sum += i
    i+=1
print("Sum:",sum)

# Question 6
fact = int(input("Enter the number for find factorial of that number:"))
product = 1
for i in range(1,fact+1):
    product *= i
    i+=1
print(f"Factorial of {fact} is:{product}")

# Question 7
n = int(input("Enter the value of N:"))
for i in range(1,1+n):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end=" ")
    print("\n")

# Question 8
n = int(input("Enter the value of N:"))
for i in range(1,1+n):
    print("*"*i,end=" ")
    print("\n")

# Question 9
n = int(input("Enter the value of N:"))
for i in range(1,1+n):
    if (i == 1 or i == n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")

# Question 10
n = int(input("Enter the value of N:"))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")