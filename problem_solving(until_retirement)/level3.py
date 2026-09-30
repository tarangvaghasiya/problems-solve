#1
 
# n = str(input("enter number"))
# count=0
# for i in n:
#     count+=1
# print(count)

#2

# n = int(input("Enter number: "))

# sum = 0

# for digit in str(n):
#     sum = sum + int(digit)

# print("Sum of digits:", sum)

#3

# n = int(input("Enter number: "))

# mul = 1

# for digit in str(n):
#     mul = mul * int(digit)

# print("multipication of digits:", mul)

#4

# number = int(input("Enter a number: "))

# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10

# print("Reverse:", reverse)

#5

# str1 = input("enter number:-")
# i = 0
# j = len(str1) - 1
# flag = True
# while i < j :
#     if str1[i] == str1[j]:
#         i+=1
#         j-=1 
#     else:
#         flag = "false"
#         i=j
# if flag == True:
#     print("string is palandrom")
# else:
#     print("string is not palendrom")

#6

# n = int(input("Enter number: "))

# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count = count + 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")

#7

# n = int(input("Enter N: "))

# for num in range(2, n + 1):
#     count = 0

#     for i in range(1, num + 1):
#         if num % i == 0:
#             count = count + 1

#     if count == 2:
#         print(num, end=" ")

#9

# a = int(input("enter number:-"))
# b = int(input("enter number:-"))

# gcd = 1

# for i in range(1, a + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i

# print(gcd)

#10

# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# if a > b:
#     start = a
# else:
#     start = b
# lcm = 0
# i = 1
# while i<=a*b:
#     if i % a == 0 and i % b == 0 and lcm == 0:
#         lcm = i
#     i+=1

# print("LCM =", lcm)