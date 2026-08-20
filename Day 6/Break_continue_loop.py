# Break and Continue statement

# stop print after 5 

i=0 

while i<=10:
    if i==5:
        break
    print(i)
    i+=1

# skip number 5

i=0

while i<=10:
    if i==5:
        i+=1
        continue
    print(i)
    i+=1

# stop when user enter zero as input

while True:
    num=int(input("Enter the number:"))

    if num==0:
        break

    print("you entered:",num)

# print positive numbers only

i=0

while i<=10:
    if i%2 !=0:
        i+=1
        continue
    print(i)
    i+=1

# Password System 

while True:
    password=input("Password:")
    if password=="python123":
        print("Access Granted")
        break
    print("wrong password try again.")