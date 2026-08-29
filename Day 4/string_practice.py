# Question 1
user_name=input("Enter your full name:")
space=user_name.find(" ")
first=user_name[:space]
last=user_name[space+1:]
print("First Name:",first)
print("Last Name:",last)

# Question 2
str="PythonProgramming"
print(str[0:6])
print(str[6:])

# Question 3

name="javalanguage"
print(name.lower())
print(name.upper())
print(name.capitalize())
print(len(name))

# Question 4

sentence=input("Sen:")
print(sentence.count("a"))

# Question 5

email=input("Enter your email:")
special=email.find("@")
print("user_name:",email[:special])
print("domain_name:",email[special:])

