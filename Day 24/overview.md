# Memory managment and refernce counting:
# x ─────┐
       ├──> [1, 2, 3]
# y ─────┘
# It gives us one more refernce because it make one temporarily one refernce of x.
# z=[6,7,8]
# t=z
# print(id(z))
# print(id(t))
# print(z)
# print(t)
# Both x and y refer to the same integer object.
# Some examples or mutable and imutable like.
# Immutable: int, float, str, tuple
# Mutable: list, dict, set

# Concept	Simple meaning
# Reference -->	A variable points to an object
# id() --> Shows an object's identity
# getrefcount() --> Shows references to an object
# Mutable	Object can be changed
# Immutable	Object cannot be changed
# == -->	Same value?
# is -->	Same object?
# b = a	Same object
# b = a[:]	New list copy