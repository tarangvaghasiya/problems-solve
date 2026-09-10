#1

# year=int(input("enter year number"))
# if year%4 == 0:
#     print("year is a leap year")
# elif year%4 != 0:
#     print("year is not leap year")
# else:
#     print("enter valid year")

#2

# asd=input("inptul:-")
# if "A" <= asd <= "Z":
#     print("Uppercase")
# elif "a" <= asd <= "z":
#     print("lowercase")
# elif asd in "@#$%&*!":
#     print("Special character")
# elif 0<= int(asd) <= 9:
#     print("degit")
# else:
#     print("enter valid value")

#3

# asd1 = input("input:-").lower()
# if asd1 == "a" or asd1 == "e" or asd1 =="i" or asd1 =="o" or asd1 =="u":
#     print("vowel")
# elif asd1 =="b" or asd1 =="c" or asd1 =="d" or asd1 =="f" or asd1 =="g" or asd1 =="h" or asd1 =="j"or asd1 =="k" or asd1 =="l" or asd1 =="m" or asd1 =="n" or asd1 =="p" or asd1 =="r" or asd1 =="s" or asd1 =="t" or asd1 =="v" or asd1 =="w" or asd1 =="x" or asd1 =="y" or asd1 =="z":
#     print("Consonant")
# else:
#     print("invalid input")

#4

# cost_price=int(input("enter cost price:-"))
# selling_price=int(input("enter selling price:-"))
# if selling_price > cost_price:
#     profit=selling_price - cost_price
#     print("profit is:-",profit)
# elif cost_price> selling_price:
#     loss=cost_price-selling_price
#     print("loss is:-",loss)
# elif cost_price == selling_price:
#     print("no profit no loss")

#5

# cost=int(input("enter cost price:-"))
# selling=int(input("enter selling price:-"))
# profit = selling - cost
# loss1 = cost - selling
# if cost < selling:
#     print(f"profit is:-{profit}")
# elif cost > selling:
#     print(f"loss is :-{loss1}")

#6

# unit=int(input("enter number of unit:-"))

# if unit <= 100:
#     bill = unit*5
# elif unit <= 200:
#     bill = (100*5) + (unit - 100)*7
# else:
#     bill = (100*5)+(100*7)+(unit-200)*10

# print("bill is",bill)

#7

a=int(input("enter your first number"))

b=int(input("enter your second number"))

print("1.addition\n2.subtaration\n3.multiplication\n4.division\n5.flor division\n choose your opretion")

aop=int(input("eneter your opretion number"))

if aop == 1:

    print(a+b)

elif aop == 2:

    print(a-b)

elif aop == 3:

    print(a*b)

elif aop == 4:

    print(a/b)

elif aop == 5:

    print(a//b)
else:
    print("you choose other number")

#8

# tem=int(input("enter tempreture"))
# if tem > 35:
#     print("hot")
# elif tem > 26:
#     print("normal")
# elif tem > 16:
#     print("cold")
# elif tem > 0:
#     print("very cold")
# elif tem < 0:
#     print("freezing")

#9

# num=int(input("enter number"))
# if num < 0:
#     print("your number is negetive")
# elif num <10:
#     print("Number is between 0 and 10")
# elif num <50:
#     print("Number is between 11 and 50")
# elif num <100:
#     print("Number is between 51 and 100")
# elif num > 100:
#     print("Number is above 100")

#10

# e,f,g=map(int,input("enter triangle sides value").split())
# if (e + f > g) and (e + g > f) and (f + g > e):
#         print("Valid triangle")
# else:
#         print("Invalid triangle")


