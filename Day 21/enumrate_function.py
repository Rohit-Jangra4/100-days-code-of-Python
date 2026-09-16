# Enumerate Function is Python
fruits = ["Apple", "Banana", "Mango", "Orange"]
for index,fruit in enumerate(fruits):
    print(index,fruit)

# Question 2
names = ["Rohit", "Aman", "Rahul", "Vikas"]
for index,name in enumerate(names,start=1):
    print(index,name)

# Question 3
fruits = ["Apple", "Banana", "Mango", "Orange"]
for index, fruit in enumerate(fruits):
    if fruit=="Mango":
        print("Mango is at index",index)

# Question 4
numbers=[10, 20, 30, 40, 50, 60]
for index,digit in enumerate(numbers):
    if index%2==0:
        print("Numbers:",digit)

# Question 5
items = ["Milk", "Bread", "Eggs", "Rice"]
for number, item in enumerate(items,start=1):
    print(f"{number}.{item}")

# Question 6
numbers = [10, 25, 30, 25, 40, 25, 50]
for index,value in enumerate(numbers):
    if value==25:
        print("25 is at index",index)

# Question 7
marks = [78, 92, 85, 96, 88, 91]
highest = 0
highest_index = 0

for index, mark in enumerate(marks):
    if mark > highest:
        highest = mark
        highest_index = index

print(f"Highest marks is:{highest}")
print(f"Index is:{highest_index}")

# Question 8
students = ["Rohit", "Aman", "Rahul", "Vikas", "Karan"]
marks = [85, 32, 76, 28, 91]
for index,mark in enumerate(marks):
    if mark<40:
        students[index]
        print(f"Name{students[index]}\nIndex:{index}\nMarks:{mark}")
# Question 9
list1 = [10, 20, 30, 40, 50]
list2 = [10, 25, 30, 45, 50]

for index, value in enumerate(list1):
    if value != list2[index]:
        print(f"Index {index}: {value} != {list2[index]}")