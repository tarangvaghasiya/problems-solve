#1

# arr = [1, 2, 3]

# double = []

# for i in range(len(arr)):
#     double.append(arr[i]*2)

# print(double)

#2

# arr = [1, 2, 3]

# double = []

# for i in range(len(arr)):
#     double.append(arr[i]**2)

# print(double)

#3

# arr = [1, 2, 3]

# revers = []

# for i in range(len(arr)-1,-1,-1):
#     revers.append(arr[i])

# print(revers)

#4

# arr = [1, 2, 3]

# copy = []

# for i in range(len(arr)):
#     copy.append(arr[i])

# print(copy)

#5

# arr = [1, 2, 3]
# value = 2

# found = False

# for i in arr:
#     if i == value:
#         found = True

# print(found)

#6

# arr = [10, 30,40,0]
# value = 20

# index = -1

# for i in range(len(arr)):
#     if arr[i] == value:
#         index = i
#         break
# if index >= 0:
#     print(index)
# else:
#     print(-1)

#7

# arr = [1, 2, 3,2,2]
# value = 2
# coun = 0


# found = False

# for i in arr:
#     if i == value:
#         found = True
#         coun +=1

# print(coun)

#8

# arr = [1, 2, 2, 3]

# inc = True

# for i in range(1, len(arr)):
#     if arr[i] < arr[i - 1]:
#         inc = False

# print(inc)

#9

# arr = [10, 5, 8, 20]

# largest = arr[0]
# second = arr[0]

# for i in range(len(arr)):
#     if arr[i] > largest:
#         second = largest
#         largest = arr[i]
#     elif arr[i] > second and arr[i] != largest:
#         second = arr[i]

# print(second)

#10

# arr = [10, 5, 8, 20]

# smallest = arr[0]
# second = arr[0]

# for i in range(len(arr)):
#     if arr[i] < smallest:
#         second = smallest
#         smallest = arr[i]
#     elif arr[i] < second and arr[i] != smallest:
#         second = arr[i]

# print(f"second smallest is :-{second}")
# print(f"smallest is :-{smallest}")