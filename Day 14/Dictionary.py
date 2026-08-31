# Dictionary in python 
dict={"Rohit":"CEO","Muskan": "CTO","Neha" : "CFO"}
print(dict)
print(dict["Rohit"])
print(dict.get("Muskan"))

print(dict.keys())

for key in dict.keys():
    print(dict[key])

for values in dict.values():
    print(values)

print(dict.items())

for key,value in dict.items():
    print(f"The value of {key} corresponding is {value}.")

# Question 
student={
    "name":"Rohit Jangra",
    "age":21,
    "course":"Computer Engineering",
    "city":"Sonipat"
}
print(student)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

#That is the 2nd method to find the values in dictionary 
for key in student.keys():
    print(student[key])

marks = {
    "Math": 85,
    "Python": 92,
    "DBMS": 78,
    "Digital": 88
}
print(marks.keys())
print(marks.values())
print(marks.items())
print(len(marks))

marks = {
    "Rohit": 85,
    "Aman": 92,
    "Rahul": 78,
    "Vikas": 95,
    "Karan": 88
}
highest = 0
top_student = ""

for key, value in marks.items():
    if value > highest:
        highest = value
        top_student = key

print("Highest Marks:", highest)
print("Student:", top_student)

# Character Frequency
dict={}
string=input("Enter a string:")

for char in string:
   string.count(char)
   