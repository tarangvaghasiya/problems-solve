#1

# arr = [1,2,3,4,5]
# arr1= []
# for i in arr:
#     if i%2 != 0:
#         arr1.append(i)
# print(arr1)

#2

# arr = [1, 2, 2, 3, 3, 3]
# result = []

# for i in arr:
#     if i not in result:
#         result.append(i)

# print(result)

#3

# arr1 = [1, 2]
# arr2 = [3, 4]
# mix = []

# for i in arr1:
#     mix.append(i)

# for i in arr2:
#     mix.append(i)

# print(mix)

#4   by ai

# arr1 = [1, 2, 3, 4]
# arr2 = [3, 4, 5]

# result = []

# for num in arr1:
#     if num in arr2 and num not in result:
#         result.append(num)

# print(result)

#5

# arr = [1, 2, 3, 4]

# result = []

# if len(arr) > 0:
#     result.append(arr[3])
#     for i in range(0, len(arr)-1):
#         result.append(arr[i])
# print(result)

#6

# arr = [1, 2, 3, 4]
# result = []
# if len(arr) > 0:
#     for i in range(1, len(arr)):
#         result.append(arr[i])
#     result.append(arr[0])
# print(result)

#7

# arr = [1,2,3,4,5,6,7,8,9,10]
# av = 0
# total = 0
# for i in arr:
#     total += i
# av = total/len(arr)
# count = 0
# print(av)
# for j in arr:
#     if j > av:
#         count += 1
# print(count)

#8 by ai

# arr = [-5, -1, 3, 7, -2]

# largest_positive = None
# smallest_negative = None

# for num in arr:
#     if num > 0:
#         if largest_positive is None or num > largest_positive:
#             largest_positive = num

#     elif num < 0:
#         if smallest_negative is None or num < smallest_negative:
#             smallest_negative = num

# print("Largest positive =", largest_positive)
# print("Smallest negative =", smallest_negative)

#9

# arr = [0,1,0,1,1]
# cou0 = 0
# cou1 = 0
# for i in arr:
#     if i == 0:
#         cou0 +=1
#     elif i == 1:
#         cou1 +=1
#     else:
#         ("enter valid number")
#         break

# print(f"zeros :-{cou0}")
# print(f"ones :-{cou1}")

#10

# arr = [1,2,3,4,5,6,7,8,9,10]
# even = []
# odd = []
# for i in arr:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"even number loop :- {even}")
# print(f"odd number loop :-{odd}")