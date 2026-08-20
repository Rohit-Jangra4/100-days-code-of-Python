# Question 1 (1. Counting)

i=0
while i<101:
    print(i)
    i+=1

# Question 2 (2. Even Numbers)

i = 1

while i <= 50:
    if i % 2 == 0:
        print(i)

    i += 1

# Question 3 (3. Sum)

i=0
total=0
while i<=100:
    total+=i
    i+=1

print("Sum:",total)

# Question 4 (4. Multiplication Table)

n=int(input("N:"))

i=1

while i<=10:
    print(f"{n}X{i}={n*i}")
    i+=1

# Question 5 (Reverse count 20 to 1)

i=20
while i>=1:
    print(i)
    i-=1