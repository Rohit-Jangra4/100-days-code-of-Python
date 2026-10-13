# Exercise 1. Print first 10 natural numbers using while loop.
i = 1
while (i<=10):
    print(i)
    i+=1
"------------------------------------------------------------"
# Exercise 2. Display numbers from -10 to -1 using for loop
for i in range(-10,0):
    print(i)
"------------------------------------------------------------"
# Exercise 3. Display a message “Done” after successful execution of for loop
for i in range(0,5):
    print(i)
else:
    print("Done!")
"------------------------------------------------------------"
#Exercise 4. Calculate the sum of all numbers from 1 to N
n = int(input("Enter the value of N:"))
sum = 0
for i in range(1,n+1):
    sum += i
print(f"Sum of {n} is:{sum}")
"------------------------------------------------------------"
#Exercise 4. Print multiplication table of a given number
num = int(input("Enter the numbers for print Table of that number:"))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
"------------------------------------------------------------"
# Exercise 6. Calculate the cube of all numbers from 1 to a given number
n = int(input("Enter the value of N:"))
for i in range(1,n+1):
    print(f"The Cube of 1 to {n} is:{i**3}\n")
"------------------------------------------------------------"
#Exercise 7. Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item>500:
        break

    if item>150:
        continue

    if (item % 5 == 0):
        print(item)
"------------------------------------------------------------"
#Exercise 8. Count occurrences of a specific element in a list
list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0
for num in list1:
    if num == target:
        count+=1
print(f"{target} is appears {count} times.")
"------------------------------------------------------------"
#Exercise 9. Print elements from a list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(1,len(my_list),2):
    print(my_list[i],end=" ")
"------------------------------------------------------------"
#Exercise 10. Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
print(len(list1))
size = len(list1) - 1
for i in range(size,-1,-1):
    print(list1[i])
"------------------------------------------------------------"