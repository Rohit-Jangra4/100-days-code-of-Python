# Arthimati Operators

# Addition (+)

a=45
b=67
print("Result:",a+b) # output = 112

# Subtraction (-)

x=89
y=56
print("Subtraction:",x-y) #output = 33

# Multiplication (*)

w=56
z=45
print("Multiplication:",w*z) # output = 2520

# Division (/)

t=45
s=9
print("Division:",t/s) #output = 5

# Modulus (%)

r=56
k=34
print("Modulus:",r%k) #output = 22

# Floor Division (//) 

g=10
h=3
print("Floor division:",g//h) #output = 3

#        Claculator 

a=int(input("A:"))
b=int(input("B:"))
function=input("Enter in this operation (+,*,-,/):")
# Addition
if function == '+':
    print("Addition is:",a+b)
elif function == '-':
    print("Subtraction is:",a-b)
elif function == '*':
    print("Multiplication is:",a*b)
elif function == '/':
    print("Division is:",a/b)
else:
    print("Function is Invalid!")


