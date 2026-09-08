#1

num = int(input("enter your number:-"))
if num > 0:
    print("number is positive")
if num < 0:
    print("number is negetive")
else :
    print("number is zero")


#2

num1 = int(input("enter your number:-"))
if num1 > 0:
    print("number is positive")
    if num1 % 2 == 0:
        print("numver is even")
    else:
        print("number is odd")

elif num1 < 0:
    print("number is negetive")
    if num1 % 2 == 0:
        print("numver is even")
    else:
        print("number is odd")
else :
    print("number is zero")

#3

a=int(input("enete your first number:-"))
b=int(input("enter your second number:-"))
if a > b:
    print(f"the largest number is {a}")
else:
    print(f"the largest number is {b}")


#4

c=int(input("enter your first number"))
d=int(input("enter your secound number"))
e=int(input("enter your third number"))
if c>d>e:
    print(f"smallest number is{e}")
elif c>e>d:
    print(f"smallest number is{d}")
elif d>e>c:
    print(f"smallest number is{c}")
elif d>c>e:
    print(f"smallest number is{e}")
elif e>d>c:
    print(f"smallest number is{c}")
elif e>c>d:
    print(f"smallest number is{d}")

#5

if c>d>e:
    print(f"largest number is{c}")
elif c>e>d:
    print(f"largest number is{c}")
elif d>e>c:
    print(f"largest number is{d}")
elif d>c>e:
    print(f"largest number is{d}")
elif e>d>c:
    print(f"largest number is{e}")
elif e>c>d:
    print(f"largest number is:-{e}")

#6

num2=int(input("enter your number:-"))
if num2%5==0 and num2%11==0:
    print("number id divisible by 11 and 5")
elif num2%5==0:
    print("number is divisible by only 5")
elif num2%11==0:
    print("number is divisible by only 11")
else:
    print("divisible by neither")

#7

num3=int(input("enter your number:-"))
if num3%3==0 and num3%7==0:
    print("number id divisible by 3 and 7")
elif num3%3==0:
    print("number is divisible by only 3")
elif num3%7==0:
    print("number is divisible by only 7")
else:
    print("divisible by neither")

#8

marks=int(input("enter your marks"))
if marks > 100:
    print("invalid marks")
elif marks >= 40:
    print("pass")
elif marks > 0:
    print("fail")
elif marks < 0:
    print("invalid marks")

#9

marks1=int(input("input your marks"))
if marks1>100:
    print("invalid marks")
elif marks1>90:
    print("your grad is A")
elif marks1>80:
    print("your grad is B")
elif marks1>70:
    print("your grad is C")
elif marks1>60:
    print("your grad is D")
elif marks1>40:
    print("your grad is E")
elif marks1>0:
    print("you are fail")
else:
    print("invalid marks")

#10

age=int(input("enter your age"))
if age >18:
    print("can vote")
elif age > 0 :
    print("can't vote")
elif age <0:
    print("enter valide age")