# Today we use a some modules in python like maths pandas.
import math
radius=float(input("Enter the Radius:"))

area=math.pi * radius ** 2
circumference=2*math.pi*radius
diameter=2*radius

print("Area of the circle is:",area)
print("Circumfernce is:",circumference)
print("Diameter of the circle is:",diameter)


a=float(input("Enter the value of A:"))
b=float(input("Enter the value of B:"))

print("Square Root:",math.sqrt(a))
print("Square Root:",math.sqrt(b))
print("Ceiling:",math.ceil(a))
print("Ceiling:",math.ceil(b))
print("Floor:",math.floor(a))
print("Floor:",math.floor(b))
print("Power of A and B:",math.pow(a,b))


#
import random
otp=""
for i in range(6):
    otp += str(random.randint(0, 9))
print("Your otp is:",otp)


number=random.randint(1,100)

while True:
    guess=int(input("Enter a number:"))

    if guess>number:
        print("Too High!")

    elif guess<number:
        print("Too Low!")

    else:
        print("Correct! 🎉")
        break


from datetime import datetime

now=datetime.now()

print("Current Date:", now.strftime("%d-%m-%Y"))
print("Current Time:", now.strftime("%H:%M:%S"))


import pandas as pd

data = {
    "Name": ["Rohit", "Aman", "Rahul", "Sumit"],
    "Marks": [85, 72, 91, 64]
}

df=pd.DataFrame(data)

print(df)

print("Average:", df["Marks"].mean())
print("Highest:", df["Marks"].max())
print("Lowest:", df["Marks"].min())

highest_student = df.loc[df["Marks"].idxmax(), "Name"]

print("Highest scorer:", highest_student)

#
import random
import math

score = 0

for i in range(5):

    a = random.randint(1, 20)
    b = random.randint(1, 20)

    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        answer = a + b

    elif operator == "-":
        answer = a - b

    else:
        answer = a * b

    user_answer = int(input(f"{a} {operator} {b} = "))

    if user_answer == answer:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong ❌")
        print("Correct answer:", answer)

print("\nYour score:", score, "/ 5")