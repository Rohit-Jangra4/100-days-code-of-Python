# Break and Continue

# Queation 1
i=0 

while i<=10:
    if i==7:
        break
    print(i)
    i+=1

# Question 2
while True:
    num=int(input("Enter the number:"))

    if num==10:
        break

    print("you entered:",num)

# Question 3
while True:
    pin=input("Pin:")
    if pin=="5700":
        print("Access Granted")
        break
    print("wrong password try again.")

# Question 4
i=0 

while i<=101:
    if i==45:
        break
    print(i)
    i+=1

# Question 5
i=1
while i<=30:
    if i%2 != 0:
        i+=1
        continue
    print(i)
    i+=1

# Question 6
i=1
while i<=30:
    if i%3 == 0:
        i+=1
        continue
    print(i)
    i+=1