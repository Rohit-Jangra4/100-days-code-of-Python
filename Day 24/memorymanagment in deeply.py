# Memory managment and refernce counting:
import sys
x= [1,2,3]
print((sys.getrefcount(x)))
y=x
print(sys.getrefcount(y))
#2. Variables and Objects
z=[6,7,8]
t=z
print(id(z))
print(id(t))
print(z)
print(t)
#3. Mutable vs Immutable
# Immutable intgers, strings, and tuples are immutable. Lists and dictionaries are mutable.
x= 10
x=x+x
print(x)

# mutable part
numbers=[1,2,3]
numbers.append(4)
print(numbers)

#4. Copying vs Referencing
a= [1,2,3]
b=a
b.append(4)
print(a)
print(b)

x=[5,6,7]
y= x[:]
y.append(8)
print(x)
print(y)

#== vs is
a= [1,2,3]
b= [1,2,3]
print(a==b) # True
print(a is b) # False

