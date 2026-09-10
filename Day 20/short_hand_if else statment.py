# If Else used by short hand method
age=int(input("Enter your age:"))
result="You are eligible to vote" if age>=18 else "You are not eligible to vote"
print(result)

#
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
result="a is greater" if a>b else "a and b are equal" if a==b else "b is greater"
print(result)

#
num=int(input("Enter a number:"))
positive="Number is positive" if num>0 else "Number is zero" if num==0 else "Number is negative"
print(positive)

#
n=int(input("Enter a number:"))
even="Number is even" if n%2==0 else "Number is odd"
print(even)

#
marks=int(input("Enter your marks:"))
result="You are pass" if marks>=40 else "You are fail"
print(result)

#
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=int(input("Enter another number:"))
result = (
    "All are equal" if a == b == c
    else "A and B are equal and C is greatest" if a == b and c > a
    else "A and C are equal and B is greatest" if a == c and b > a
    else "B and C are equal and A is greatest" if b == c and a > b
    else "A is greatest" if a > b and a > c
    else "B is greatest" if b > a and b > c
    else "C is greatest"
)
print(result)

#
temperature=int(input("Enter the temperature:"))
result="Weather is hot" if temperature>=30 else "Weather is cold"
print(result)

#ATM
Balance=int(input("Enter your balance:"))
Withdrawal=int(input("Enter the amount to withdraw:"))
transaction="Transaction successful" if Withdrawal<=Balance else "Invalid withdrawal amount" if Withdrawal<=0 else "Insufficient balance"
print(transaction)

#Shooping Discount
Amount = int(input("Enter shopping amount: "))

discount = 20 / 100 * Amount if Amount >= 5000 else 10 / 100 * Amount if Amount >= 2000 else 0

FinalAmount = Amount - discount

print("Original Amount:", Amount)
print("Discount:", discount)
print("Final Amount:", FinalAmount)



