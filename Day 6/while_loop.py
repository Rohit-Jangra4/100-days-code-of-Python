# While Loop in Python

# Print number 1 to 10

count=1
while count<11:
    print(count)
    count+=1

# Print even number from 1 to 20

i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1

# Print numbers from 10 to 1

i=10
while i>=1:
    print(i)
    i-=1

# Sum of number from 1 to 10

i=0
total=0

while i<=10:
    total=total+i
    i+=1

print("Sum:",total)

# Multiplication table of user input number

n=int(input("N:"))

i=1

while i<=10:
    print(f"{n}X{i}={n*i}")
    i+=1

