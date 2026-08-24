# Question

tup1=(1,2,3,4,5,6,7,8,9,10)
print(tup1)

print(tup1[0])
print(tup1[-1])
print(tup1[5])

# Question
tup2=(10, 20, 10, 30, 40, 10, 50, 20)
print(tup2)

print(tup2.count(10))

print(tup2.count(10))

# Question
tup3=("Python", "C", "Java", "Python", "C++")
print(tup3)

print(tup3.index("Java"))

print(tup3.index("Python"))

# Question

a, b, c, d, e = map(int, input("Enter 5 numbers: ").split())

tup = (a, b, c, d, e)

print(tup)
print(sum(tup))

average = sum(tup) / len(tup)

# Qustion 
tup4=(12, 45, 67, 88, 90, 23, 34, 51)
print(tup4)

for item in tup4:
    if item%2==0:
        print(item,"Even")
    else:
        print(item,"Odd")

# Question
tup5=(12, 45, 67, 88, 90, 23, 34, 51)
largest = tup5[0]
smallest = tup5[0]
for item in tup5:
    if item > largest:
        largest = item

    if item < smallest:
        smallest = item

print("Largest:", largest)
print("Smallest:", smallest)

# Question
tup = (10, 20, 30, 20, 40, 10, 50, 30, 60, 20)

duplicates = ()
unique = ()

for item in tup:

    # Duplicate values
    if tup.count(item) > 1:
        if item not in duplicates:
            duplicates = duplicates + (item,)
            print(item, "->", tup.count(item), "times")

    # Unique values
    if item not in unique:
        unique = unique + (item,)

print("Duplicate Tuple:", duplicates)
print("Unique Tuple:", unique)

