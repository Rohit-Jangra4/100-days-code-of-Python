#  Basically give the argument to code means:

def name(fname,mname="Jhon",lname="whatson"):
    print("Hello,",fname,mname,lname)

name("Ammy")

def value(a=56,b=67):
    perimeter=2*(a+b)
    print(f"Perimeter of {a} and {b} is:{perimeter}")

value(456,4650)

def average(*num):
    sum=0
    for i in num:
        sum+=i
    print("Average is,",sum / len(num))

average(34,56,67,8,9,89)

def name(**name):
    print("Hello,",name["fname"],name["mname"],name["lname"])

name(fname="jack",mname="sparrow",lname="pirates")

def name(fname,mname,lname):
    return (fname + " " + mname + " " + lname + " ")

print(name("jack","Rohit","Hacker"))