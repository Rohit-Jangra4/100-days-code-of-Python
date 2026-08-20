# if elif else practice

# Question 1
integer=int(input("Enter the number:"))
if integer>0:
    print("+ve number")
elif integer==0:
    print("Zero number")
else:
    print("-ve number")

# Question 2

marks=int(input("Marks:"))

if marks>=90 and marks<100:
    print("Grade: A")
elif marks>=80 and marks<=89:
    print("Grade: B")
elif marks>=70 and marks<=79:
    print("Grade: C")
elif marks>=60 and marks<=69:
    print("Grade: D")
else:
    print("Grade: E")

# Question 3

Age=int(input("Age:"))

if Age<=13:
    print("Child")
elif Age>=14 and Age<=19:
    print("Teenager")
elif Age>=20 and Age<=59:
    print('Adult')
else:
    print("Senior citizen")

# Question 4

purchase_amnt=int(input("Amount:"))
if purchase_amnt>=5000:
    print("15% Discount and Total bill:", purchase_amnt-(15/100)*purchase_amnt)
elif purchase_amnt>=3000 and purchase_amnt<=4999:
    print("10% Discount and Total bill:",purchase_amnt-(10/100)*purchase_amnt)
elif purchase_amnt>=2000 and purchase_amnt<=2999:
    print("5% Discount and Total bill:",purchase_amnt-(5/100)*purchase_amnt)
else:
    print("No discount:",purchase_amnt)

# Question 5

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

if a>b and a>c:
    print("a is greatest.")
elif b>c:
    print("b is greatest.")
else:
    print("c is greatest.")