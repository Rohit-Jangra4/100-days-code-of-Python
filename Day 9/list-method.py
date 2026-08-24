# list method in python 

# list.sorted
lis=[1,2,34,5,5,7,5,78,9,67,678,67]
print(lis)
lis.sort()
print(lis)

colors=["purple","pink","Black","yellow","green"]
print(colors)
colors.sort()
print(colors)

# l.reversed
list=[23,5,654,45,345,7,678,3534,53]
print(list)
list.reverse()
print(list)

# lis.index
list1=["Rohit","vansh","nishant","chirag","naman"]
print(list1)
print(list1.index("nishant"))

# list.count
list2=[1,4,3,2,52,5,6,43,2,6,43,2,6,43,9]
print(list2)
print(list2.count(2))

# copy
list3=["violet","green","red","skyblue","black"]
print(list3)
new_list=list3.copy()
print(new_list)

# insert
list4=["violet","green","red","skyblue","black"]
list4.insert(2,"Rohit Jangra")
print(list4)

# extended method
colours=["Red","Orange"]
ext=["Green","Black"]
colours.extend(ext)
print(colours)

# Concating two list 
language=["Java","Python","C++","C"]
language_2=["PHP","Javascript","R"]
concatanate=language+language_2
print(concatanate)
