# Using for loop with else statement in Python

for i in range(5):
    print(i)
else:
    print("Loop completed without break")

# When we use break statement in the loop, the else block will not be executed.

for i in range(5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print(i)
else:
    print("Loop completed without break")

numbers = [10, 20, 30, 40, 50]
for num in numbers:
    if num == 30:
        print("Found the number:", num)
        break
else:
    print("Number not found")

numbers = [10, 20, 30, 40, 50]
for num in numbers:
    if num == 35:
        print("Found the number:", num)
        break
else:
    print("Number not found")

numbers = [3, 7, 11, 15, 19]
for num in numbers:
    if num % 2 == 0:
        print("Found an even number:", num)
        break
else:
    print("No even numbers found in the list")


num=int(input("Enter a number to check if it's prime: "))
for i in range(2, num):
    if num % i != 0:
        continue
    else:   
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")

passwords = ["python123", "hello123", "admin123", "rohit123"]
user_input = input("Enter your password: ")
for password in passwords:
    if user_input == password:
        print("Access granted")
        break
else:
    print("Access denied. No matching password found.")    

students = {
    "Rohit": 85,
    "Aman": 72,
    "Rahul": 91,
    "Karan": 68
}
for student, marks in students.items():
    if marks == 85:
        print(student, "has scored exactly 85 marks.")
        break
else:
    print("No student has scored exactly 85 marks.") 