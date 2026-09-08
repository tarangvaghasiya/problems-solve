#1

# year=int(input("enter year number"))
# if year%4 == 0:
#     print("year is a leap year")
# elif year%4 != 0:
#     print("year is not leap year")
# else:
#     print("enter valid year")

#2

asd=input("inptul:-")
if "A" < asd < "Z":
    print("Uppercase")
elif "a" < asd < "z":
    print("lowercase")
elif -9999999 < int(asd) < 99999999:
    print("digit")
else:
    print("special cherecter")
