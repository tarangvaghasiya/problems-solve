#1

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

#2

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,"X",j,"=",i*j)

#3

# for i in range(3):
#     for j in range(4):
#         print("*",end="")
#     print() 

#4

# for i in range(2):
#     for j in range(3):
#         print("(",i,",",j,")",end="")
#     print()

#5

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end="")
#     print()

#6

# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end="")
#     print()

#7

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#8

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#9

# for i in range(3):
#     for j in range(5):
#         print("*",end="")
#     print()


#10

# for i in range(4):
#     for j in range(1,5):
#         if j%2 == 0:
#             print(1,end="")
#         else:
#             print(0,end="")
#     print()

#11

# for i in range(3):
#     for j in range(1, 7):
#         if j % 2 == 0:
#             print(j, end=" ")
#     print()

#12

# N = int(input("enter a number :-"))

# for i in range(N):
#     for j in range(1, N + 1, 2):
#         print(j, end=" ")
#     print()

#13

# for i in range(1, 5):
#     for j in range(1, 5):
#         if (i + j) % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")
#     print()

#14

# N = int(input("enter a number:-"))

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if i == j:
#             print("Same", end=" ")
#         else:
#             print("Different", end=" ")
#     print()


#15

# for i in range(4):
#     for j in range(4):
#         if i == j:
#             print(1,end="")
#         else:
#             print(0,end="")

#     print()

#16

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i % j == 0:
#             print("X", end=" ")
#         else:
#             print("-", end=" ")
#     print()

#17

# N = int(input("enter a number:-"))

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if j % i == 0:
#             print(j, end=" ")
#     print()

#18

# N = int(input("enter a number:-"))

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if i + j > N:
#             print(i, j)

#19

# N = int(input("enter a number:-"))

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         product = i * j

#         if product % 2 == 0:
#             print(i, j, product)

#20

# N = int(input("enter a number :-"))

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if i == j:
#             print("SPECIAL", end=" ")
#         elif i + j == N:
#             print("PAIR", end=" ")
#         else:
#             print("NORMAL", end=" ")
#     print()

#21

# word = input("enter word:-")

# for ch in word:
#     for j in range(len(word)):
#         print(ch, end="")
#     print()

#22

# word = input("enter string:-")

# for ch in word:
#     for j in range(3):
#         print(ch,j)

#23

# word = "AB"

# for i in word:
#     for j in word:
#         if i == j:
#             print(i + "/" + j, "is Same")
#         else:
#             print(i + "/" + j, "is Different")

#24

# word1 = input("enter string:-")
# word2 = input("enter string:-")

# for i in word1:
#     for j in word2:
#         if i == j:
#             print(i,j)

#25

# word1 = input("enter string:-")
# word2 = input("enter string:-")
# count = 0

# for i in word1:
#     for j in word2:
#         if i == j:
#             count +=1

# print(count)

# #26 by ai

# s = input("Enter a string: ")
# for i in range(len(s)):
#     found = False
#     for k in range(i):
#         if s[i] == s[k]:
#             found = True
#     if found == False:
#         count = 0
#         for j in range(len(s)):
#             if s[i] == s[j]:
#                 count += 1
#         print(s[i], "=", count)

#27

# word = input("enter a string:-")

# for i in word:
#     if i in "aeiouAEIOU":
#         print(i,":- vovel")
#     else:
#         print(i,":- consonant")

#28

# word1 = input("enter word:-")
# word2 = input("enter word:-")
# for i in word1:
#     for j in word2:
#         if i == j:
#             print(i)
            
#29

# word = input("enter a word:-")
# for i in word:
#     for j in word:
#         print(i ,j)

#30

# word = input("enter a word:-")
# for i in word:
#     for j in word:
#         if i != j:
#             print(i ,j)


#31

# word = input("enter a word:-")
# for i in word:
#     for j in word:
#         if i == j:
#             print(i ,"/",j,":- same")
#         if i != j:
#             print(i ,"/",j,":- diffrent")

#32


# text = input("Enter a string: ")
# vowels = "AEIOUaeiou"

# for ch1 in text:
#     for ch2 in text:
#         first_vowel = False
#         second_consonant = True

#         for v in vowels:
#             if ch1 == v:
#                 first_vowel = True

#         for v in vowels:
#             if ch2 == v:
#                 second_consonant = False

#         if first_vowel and second_consonant:
#             print(ch1, "-", ch2)

#33

# text = input("Enter a string: ")
# for ch1 in text:
#     for ch2 in text:
#         if ch1.isupper() and ch2.isupper():
#             print(ch1, "-", ch2)
#         elif ch1.islower() and ch2.islower():
#             print(ch1, "-", ch2)

#34


# text = input("Enter a string: ")

# for ch1 in text:
#     for ch2 in text:
#         difference = ord(ch1) - ord(ch2)

#         if difference < 0:
#             difference = -difference

#         print(ch1, ch2, "->", difference)

#35


# text = input("Enter a string: ")

# for ch1 in text:
#     for ch2 in text:
#         if ord(ch1) > ord(ch2):
#             print(ch1, ch2, "->", "decreasing")
#         elif ord(ch1) == ord(ch2):
#             print(ch1, ch2, "->", "same")
#         else:
#             print(ch1, ch2, "->", "increasing")


#36

# sent = input("enter a sentens:-").split(" ")
# for i in sent:
#     for j in sent:
#         print(i,j)
        
#37

# sent = input("enter a sentens:-").split(" ")
# for i in sent:
#     for j in sent:
#         if len(i) == len(j) and i != j:
#             print(i,j)

#38

# sent = input("enter a sentens:-").split(" ")
# for i in sent:
#     for j in sent:
#         if i[0] == j[0] and i != j:
#             print(i,j)

#39

# sent = input("enter a sentens:-").split(" ")
# for i in sent:
#     for j in sent:
#         if i[len(i)-1] == j[len(j) - 1] and i != j:
#             print(i,j)

#40


# text = input("Enter words: ")
# words = text.split()

# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         found = False

#         for ch1 in words[i]:
#             for ch2 in words[j]:
#                 if ch1 == ch2:
#                     found = True

#         if found:
#             print(words[i], words[j])

#41

# sentence = "I love Python code"
# words = sentence.split()

# for i in range(len(words)):
#     for j in range(len(words)):
#         difference = abs(len(words[i]) - len(words[j]))

#         print(words[i], "/", words[j], "=", difference)

#42

# sentence = "I love Python programming"
# words = sentence.split()

# longest = words[0]
# shortest = words[0]

# for i in range(len(words)):
#     for j in range(len(words)):
#         if len(words[i]) > len(longest):
#             longest = words[i]

#         if len(words[j]) < len(shortest):
#             shortest = words[j]

# print("Longest =", longest)
# print("Shortest =", shortest)

#43

# n  = int(input("enter n number:-"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#44

# n = int(input("enter n number:-"))

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#45

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i * j, end=" ")
#     print()

#46

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     for j in range(1, 2 * i):
#         if j % 2 == 0:
#             print(j, end=" ")
#     print()

#47

# n = int(input("enter n number :-"))
# for i in range(0,n):
#     for j in range(i):
#         print(j,end="")
#     print()

#48

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

#49

# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     print(i, "->", end=" ")

#     for j in range(1, i + 1):
#         if i % j == 0:
#             print(j, end=" ")

#     print()

#50 by ai

# n = int(input("Enter N: "))

# for i in range(2, n + 1):
#     prime = True

#     for j in range(2, i):
#         if i % j == 0:
#             prime = False

#     if prime:
#         print(i, end=" ")

#51

# n = int(input("Enter N: "))

# for i in range(2, n + 1):
#     prime = True

#     for j in range(2, i):
#         if i % j == 0:
#             prime = False

#     if prime:
#         print(i, end="->")

#         for j in range(1, i + 1):
#             if i % j == 0:
#                 print(j, end="," if j < i else "")

#         print(end="; " if i < n else "")

#53

# a = int(input("Enter A: "))
# b = int(input("Enter B: "))

# for i in range(1, a + 1):
#     if a % i == 0 and b % i == 0:
#         print(i, end=" ")

#54

# a = int(input("Enter A: "))
# b = int(input("Enter B: "))
# limit = int(input("Enter limit: "))

# for i in range(1, limit + 1):
#     if i % a == 0 and i % b == 0:
#         print(i, end=" ")

#55


# n = int(input("Enter N: "))

# greatest = 0
# a = 0
# b = 0

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         product = i * j

#         if product > greatest:
#             greatest = product
#             a = i
#             b = j

# print("Pair =", a, b)
# print("Product =", greatest)

#56

# n = int(input("Enter N: "))
# target = int(input("Enter target: "))

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i + j == target:
#             print(i, j)

#57

# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

#58

# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

#59

# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, end="")
#     print()

#60

# n = int(input("Enter N: "))

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

#61

# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(i):
#         print("*", end="")
#     print()

#62

# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(1, 2 * i):
#         print(k, end="")
#     print()


#63

# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print(i, end="")
#     print()

#64

