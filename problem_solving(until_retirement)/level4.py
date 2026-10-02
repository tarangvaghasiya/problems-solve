#1
 
# str1 = input("enter string:- ")
# print(f"length of string is {len(str1)}")

#2

# str1 = input("enter string:-")
# for i in str1:
#     print(i,end=" ")

#3

# str1 = input("enter string:-").lower()
# v=0
# c=0
# for i in str1:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         v+=1
#     else:
#         c+=1
# print(f"vowels are {v}")

#4

# str1 = input("enter string:-").lower()
# v=0
# c=0
# c1=""
# for i in str1:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         v+=1
#     else:
#         c+=1
#         c1=i
#         print(c1,end=" ")
# print(c)

#5

# str1=input("enter string:-")
# print(f"lower case:-{str1.lower()}")
# print(f"uppercase :-{str1.upper()}")

#6


# str1=input("enter string:-")
# print(f"lower case:-{str1.lower()}")
# print(f"uppercase :-{str1.upper()}")

#7

# str1 = input("Enter string:- ")
# reverse = ""
# i = 0
# while i < len(str1):
#     reverse = str1[i] + reverse
#     i += 1
# print(reverse)

#8

# str1 = input("enter string:-")
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

#9

# str1 = input("enter string:-")
# count=0
# for i in str1:
#     if i == "a" or i == "A":
#         count+=1
# print(f"{count} times a in string")

#10

str1 = input("Enter string: ")
i = 0
result = ""
while i < len(str1):
    if str1[i] != " ":
        result = result + str1[i]
    i = i + 1
print(result)