# set in python 

set={1,2,34,5,"Rohit jangra",4.5,78}
print(set)
print(type(set))

for item in set:
    print(item)

fruits={"Apple","Orange","chiku","banana","strawberry"}
for fruit in fruits:
    print(fruit)

numbers={10,20,30}
numbers.add(40)
numbers.add(50)
print(numbers)

colors = {"red", "blue", "green", "yellow"}
colors.remove("green")
print(colors)

users_num = int(input("Enter a number: "))

member_ship = {1, 2, 3, 4, 5}

if users_num in member_ship:
    print("You are present.")
else:
    print("Not present.")

set1={1,34,56,"murnal thakur",56.45,"coffee",45,67,"Peach","Lion"}
print(len(set1))

# Level 2
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Union of A and B
X=A.union(B)
print(X)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Intersection of A and B
Z=A.intersection(B)
print(Z)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
W=A-B
print(W)
T=B-A
print(T)

if W==T:
    print("commutative property")
else:
    print("Not.")

#symmetric differnce between A and B
A=W.union(T)

python_students = {"Rohit", "Aman", "Rahul", "Vikas", "Neha"}
c_students = {"Rahul", "Vikas", "Priya", "Neha", "Karan"}
X=python_students.intersection(c_students)
print(X)

# Level 3 — Practical Problems
numbers = set([10, 20, 10, 30, 20, 40, 30, 50])
print(type(numbers))
numbers.remove
print(numbers)

user = input("Enter the string: ")

num = set(user)

print(num)

for i in num:
    print(i)

list1 =set([1, 2, 3, 4, 5])
list2 =set([4, 5, 6, 7, 8])
print(type(list1))
print(type(list2))
x=list1.intersection(list2)
print(x)

user_input = input("Enter a sentence: ")

words = user_input.split()

unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))

all_numbers = set(range(1, 11))

numbers = {1, 2, 3, 4, 6, 7, 8, 9, 10}

x = all_numbers.difference(numbers)

print("Missing number:", x)

