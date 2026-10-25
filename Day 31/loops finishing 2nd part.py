#Exercise 26. Print full multiplication table (1 to 10)
# for i in range(1,11):
#     for j in range(1,11):
#         print(i * j,end=" ")
#     print()

# Exercise 27. List Cumulative Sum: Each element is the sum of all previous
# list = [1, 2, 3, 4]
# list2 =[]
# total = 0
# for num in list:
#     total = total + num
#     list2.append(total)
# print(f"List Cumulative Sum:{list2}")

# Exercise 28. Dictionary Filter: Extract pairs where value exceeds a threshold.
# scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
# passing_students = {}
# threshold = 75
# for name , score in scores.items():
#     if(score >= threshold):
#         passing_students[name] = score

# print(f"Passing Students: {passing_students}")

# Exercise 29. Find common elements (Intersection) using loop
# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]
# comman = []
# for item in list_a:
#     if item in list_b:
#         comman.append(item)
# print(comman)

#Exercise 30. Remove duplicates without set
# original = [1, 2, 2, 3, 4, 4, 4, 5]
# unique_list = []

# for num in original:
#     if num not in unique_list:
#         unique_list.append(num)

# print("Unique List:", unique_list)

# Exercise 31. Even/Odd Segregation: Move evens to front, odds to back
without_seggregate = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for item in without_seggregate:
    if(item % 2 == 0):
        even.append(item)
    else:
        odd.append(item)
print(even + odd)

# Exercise 32. List Rotation: Rotate elements left by k positions
nums = [1, 2, 3, 4, 5]
k = 2
for _ in range(k):
    first_elment = nums.pop(0)
    nums.append(first_elment)

print(f"Rotated list:{nums}")