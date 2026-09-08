#1

# a=int(input("input value of first side"))
# b=int(input("input value of secound side"))
# c=int(input("inpyt value of third side"))
# if a == b == c:
#     print("Equilateral")
# elif a == b != c:
#     print("Isosceles")
# elif a != b == c:
#     print("Isosceles")
# elif a != b != c:
#     print("Scalene")

#2

# acoutbal=int(input("enter balance of your account"))
# withdrawal_amount=int(input("enter withdrwal amount"))
# if withdrawal_amount <= 0:
#         if withdrawal_amount % 100 != 0:
#               if withdrawal_amount > acoutbal:
#                  if (acoutbal - withdrawal_amount) < 500:
#                     newbal=acoutbal-withdrawal_amount
# print(f"new balance is{newbal}")

#3

# username=input("enter usernme")
# pass1=input("input your password")
# if username == "admin" and pass1 == "12345":
#     print("login secusesfull")
# elif username != "admin":
#     print("user not found")
# elif pass1 != "12345":
#     print("pass word is incorct")

#4

# amount=int(input("enter your amount"))
# if amount < 500:
#         discount_percent = 0
# elif amount <= 999:
#         discount_percent = 5
# elif amount <= 1999:
#         discount_percent = 10
# elif amount <= 4999:
#         discount_percent = 15
# else:  # ₹5000 and above
#         discount_percent = 20

# discount_amount = (amount * discount_percent) / 100
# final_amount = amount - discount_amount

# print(f"Original amount    : ₹{amount}")
# print(f"Discount percentage: {discount_percent}%")
# print(f"Discount amount    : ₹{discount_amount}")
# print(f"Final amount       : ₹{final_amount}")

#5

# Input marks for 3 subjects
# sub1 = float(input("Enter marks for Subject 1: "))
# sub2 = float(input("Enter marks for Subject 2: "))
# sub3 = float(input("Enter marks for Subject 3: "))
# # Check if any subject mark is invalid (not between 0 and 100)
# if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
#     print("Invalid marks! Marks must be between 0 and 100.")
# # Check if student failed in any subject (below 35)
# elif sub1 < 35 or sub2 < 35 or sub3 < 35:
#     print("Result: FAIL (Failed in one or more subjects)")
# else:
#     # Calculate average
#     avg = (sub1 + sub2 + sub3) / 3
#     print(f"Average: {avg:.2f}")
#     # Determine Grade based on average
#     if avg >= 75:
#         print("Grade: Distinction")
#     elif avg >= 60:
#         print("Grade: First Class")
#     elif avg >= 50:
#         print("Grade: Second Class")
#     else:
#         print("Grade: Pass")

#6

# day = int(input("Enter Day: "))
# month = int(input("Enter Month: "))
# year = int(input("Enter Year: "))

# if month < 1 or month > 12:
#     print(f"{day:02d}/{month:02d}/{year} → Invalid (Month must be between 1 and 12)")
# else:

#     is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
#     if month == 2:
#         max_days = 29 if is_leap else 28
#     elif month in [4, 6, 9, 11]:
#         max_days = 30
#     else:
#         max_days = 31
#     if 1 <= day <= max_days:
#         print(f"{day:02d}/{month:02d}/{year} → Valid")
#     else:
#         print(f"{day:02d}/{month:02d}/{year} → Invalid")

#7

# hours = int(input("Enter Hours (0-23): "))
# minutes = int(input("Enter Minutes (0-59): "))
# seconds = int(input("Enter Seconds (0-59): "))

# if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
#     print(f"\n{hours:02d}:{minutes:02d}:{seconds:02d} → Valid time")
# else:
#     print(f"\n{hours:02d}:{minutes:02d}:{seconds:02d} → Invalid time")


#8

# name1 = input("Enter Name for Person 1: ")
# age1 = int(input(f"Enter Age for {name1}: "))

# name2 = input("Enter Name for Person 2: ")
# age2 = int(input(f"Enter Age for {name2}: "))


# name3 = input("Enter Name for Person 3: ")
# age3 = int(input(f"Enter Age for {name3}: "))

# print("\n--- Result ---")

# if age1 == age2 == age3:
#     print(f"All three ({name1}, {name2}, and {name3}) are of the same age.")

# elif age1 == age2 and age1 < age3:
#     print(f"{name1} and {name2} are the youngest.")

# elif age1 == age3 and age1 < age2:
#     print(f"{name1} and {name3} are the youngest.")

# elif age2 == age3 and age2 < age1:
#     print(f"{name2} and {name3} are the youngest.")

# elif age1 < age2 and age1 < age3:
#     print(f"{name1} is the youngest.")

# elif age2 < age1 and age2 < age3:
#     print(f"{name2} is the youngest.")

# else:
#     print(f"{name3} is the youngest.")

#9


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if (num2 < num1 < num3) or (num3 < num1 < num2):
#     second_largest = num1

# elif (num1 < num2 < num3) or (num3 < num2 < num1):
#     second_largest = num2

# else:
#     second_largest = num3

# print(f"\nThe second-largest number is: {second_largest}")

#10

age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))
income = float(input("Enter Family Income (₹): "))
attendance = float(input("Enter Attendance (%): "))


is_age_valid = 18 <= age <= 25
is_marks_valid = marks >= 85
is_attendance_valid = attendance >= 75
is_income_valid = income <= 300000


if is_age_valid and is_marks_valid and is_attendance_valid and is_income_valid:
    print("\nScholarship Approved")
else:
    print("\nScholarship Rejected")
    print("Reason:")
    
    if not is_age_valid:
        print("- Age must be between 18 and 25")
    if not is_marks_valid:
        print("- Marks below 85")
    if not is_attendance_valid:
        print("- Attendance below 75%")
    if not is_income_valid:
        print("- Family income above ₹300,000")
