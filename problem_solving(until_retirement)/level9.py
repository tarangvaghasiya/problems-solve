#1

# n = int(input("enter n number:-"))

# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()

#2

# n = int(input("enter N number:-"))
# for i in range(n+1):
#     for j in range(i):
#         print("*",end="")
#     print() 

#3

# n = int(input("enter N number:-"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print() 

#4

# n = int(input("enter N number:-"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print() 

#5

# n = int(input("enter number of table"))
# for i in range(1,n+1):
#     for j in range(1,11):
#         print(f"{i} X {j} = {i*j}")
#     print()

#6

# arr = [[1, 2, 3], [4, 5, 6],[10,20,30]]

# result = []

# for row in arr:
#     total = 0
#     for num in row:
#         total = total + num
#     result.append(total)

# print(result)

#7

# n = int(input("enter number:-"))

# i = 1
# found = False

# while i * i <= n:
#     if i * i == n:
#         found = True
#     i = i + 1

# print(found)

#8

# n = int(input("enter Your number:-"))
# temp = n
# total = 0
# while temp > 0:
#     digit = temp % 10
#     total = total + digit * digit * digit
#     temp = temp // 10
# print(total == n)

#9

# arr = ["hi", "hello", "a","tarang vagahsiya"]
# result = []
# for word in arr:
#     result.append(len(word))
# print(result)

#10

# arr = ["hi", "hello", "a","tarang vagahsiya"]
# lg = ""
# for word in arr:
#     if len(word) > len(lg):
#         lg = word
    
# print(lg)