# Question 1

for i in range(1,21):
    print(i)

# Question 2

for i in range(1,51):
    if i%2==0:
        print(i)

# Question 3

num=int(input("Enter the number which table you get:"))

for i in range(1,11):
    print(num,"X","=",num*i)

# Question 4

total=0
for i in range(1,101):
    total=total+i

print("sum=",total)

# Question 5
str="romieo and juliet is good couple"
for i in str:
    print(i.count("a"or"e"or"i"or"o"or"u"))