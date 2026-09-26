#1

# wo=input("input your word:-")
# count=0
# count1=0
# count2=0
# count3=0
# count4=0

# for i in wo:
#     if i.isupper():
#         count+=1

#     elif i.islower():
#         count1+=1

#     elif i == " ":
#         count2+=1

#     elif i.isdigit():
#         count3+=1

#     else:
#         count4+=1
# print(f"upper case is {count}")
# print(f"lower is {count1}")
# print(f"space is {count2}")
# print(f"digits is {count3}")
# print(f"special character is {count4}")

# hig = max(count, count1, count3, count2, count4)

# if [count, count1, count3, count2, count4].count(hig) > 1:
#     print("Tie")
# elif count == hig:
#     print("Highest: Uppercase letters")
# elif count1 == hig:
#     print("Highest: Lowercase letters")
# elif count3 == hig:
#     print("Highest: Digits")
# elif count2 == hig:
#     print("Highest: Spaces")
# else:
#     print("Highest: Special characters")

#2

# fail =0
# pass1 = 0
# good = 0
# excellent = 0

# for i in range(10):
#     marks = int(input("enter your marks"))
#     if marks >100:
#         A = "ENTER valid marks"
#     elif marks > 75:
#         A = "EXCELLENT"
#         excellent+=1
#     elif marks > 50:
#         A = "GOOD"
#         good+=1
#     elif marks >35:
#         A = "PASS"
#         pass1+=1
#     else:
#         A = "FAIL"
#         fail+=1
#     print(A)

# print("Fail:", fail)
# print("Pass:", pass1)
# print("Good:", good)
# print("Excellent:", excellent)

#3 in dout

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# highest_score = 0
# highest_word = ""

# for word in words:
#     score = 0

#     for ch in word:
#         if ch.lower() in "aeiou":
#             score += 2

#         elif ch.isalpha():
#             score += 1

#         elif ch.isdigit():
#             score += 3

#         else:
#             score += 4

#     print(word, "=", score)

#     if score > highest_score:
#         highest_score = score
#         highest_word = word

# print("\nHighest scoring word:", highest_word)
# print("Highest score:", highest_score)

#4

# for i in range(1, 6):

#     password = input(f"Enter password for user {i}: ")

#     length = False
#     uppercase = False
#     lowercase = False
#     digit = False
#     special = False

#     if len(password) >= 8:
#         length = True

#     for ch in password:

#         if "A" <= ch <= "Z":
#             uppercase = True

#         elif "a" <= ch <= "z":
#             lowercase = True

#         elif "0" <= ch <= "9":
#             digit = True

#         else:
#             special = True

#     conditions = 0

#     if length:
#         conditions += 1

#     if uppercase:
#         conditions += 1

#     if lowercase:
#         conditions += 1

#     if digit:
#         conditions += 1

#     if special:
#         conditions += 1

#     if conditions == 5:
#         print("Strong")

#     elif conditions >= 3:
#         print("Medium")

#     else:
#         print("Weak")


#5

# sen = input("enter stetment:-")
# sen = sen.strip()

# word = sen.split()

# for wor in word:
#     print(wor)
#     if len(wor) > 6:
#         print("long")
#     elif len(wor) > 4:
#         print("medium")
#     elif len(wor) > 0:
#         print("short")

#6

# for i in range(1, 6):

#     num = input(f"Enter number {i}: ")

#     even = 0
#     odd = 0

#     for digit in str(num):

#         if int(digit) % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     print("Even digits:", even)
#     print("Odd digits:", odd)

#     if even > odd:
#         print("Even occurs more")
#     elif odd > even:
#         print("Odd occurs more")
#     else:
#         print("Equal")

#     print()

#7 dout

# text = input("Enter a string: ")

# checked = ""

# for ch in text:

#     if ch in checked:
#         continue

#     frequency = 0

#     for x in text:
#         if ch == x:
#             frequency += 1

#     if frequency > 1:

#         if frequency == 2:
#             category = "Duplicate"

#         elif frequency <= 4:
#             category = "Repeated"

#         else:
#             category = "Highly Repeated"

#         print(ch, "=", frequency, "->", category)

#     checked += ch

#8

# total = 0
# p1=0
# p2=0
# p3=0
# p4=0
# for i in range(8):
#     price = int(input("enter price of product:-"))
#     if price > 5000:
#         print("Luxury")
#         p1+=1
#     elif price > 2000:
#         print("Premium")
#         p2+=1
#     elif price > 500:
#         print("Regular")
#         p3+=1
#     elif price > 0:
#         print("Budget")
#         p4+=1
#     total+=price
# print(f"total amount is {total}")
# print(f"luxury is {p1}")
# print(f"premium is {p2}")
# print(f"regular is {p3}")
# print(f"budget is {p4}")
# print(f"average product price {total/8}")

#9

# text = input("Enter a string: ")

# vowel = 0
# consonant = 0
# digit = 0
# special = 0

# for i in range(len(text)):

#     ch = text[i]

#     if i % 2 == 0:
#         position_type = "Even"
#     else:
#         position_type = "Odd"

#     # Check character type
#     if ch.lower() in "aeiou":
#         char_type = "Vowel"
#         vowel += 1

#     elif ch.isalpha():
#         char_type = "Consonant"
#         consonant += 1

#     elif ch.isdigit():
#         char_type = "Digit"
#         digit += 1

#     else:
#         char_type = "Special Character"
#         special += 1

#     print(ch, "| Position:", i, "|", position_type, "|", char_type)

#10 dout

# n = int(input("Enter n: "))

# for i in range(1, n + 1):

#     for j in range(1, i + 1):

#         if j % 3 == 0 and j % 5 == 0:
#             print("Z", end=" ")

#         elif j % 3 == 0:
#             print("X", end=" ")

#         elif j % 5 == 0:
#             print("Y", end=" ")

#         else:
#             print(j, end=" ")

#     print()

#11


for i in range(5):
    user=input(f"enter user name{i}")

    lengh=len(user)
    digit = 0
    under=0
    invalid = False

    if user[0].isalpha():
        first_character = True
    else:
        first_character = False

    for wr in user:
        if wr.isdigit():
            digit+=1
        elif wr == "_":
            under+=1
        elif wr.isalpha():
            pass
        else:
            invalid = True

        if invalid:
            result = "Invalid"
        elif lengh >= 8 and first_character and digit >= 1:
            result = "Valid"
        else:
            result= "Needs Improvement"

    print("lengh",lengh)
    print("digit",digit)
    print("underscore",under)
    print("result",result)
    print()   



#12

# sete=input("enter sentence:-")

# vowels = 0
# consonants = 0

# for i in sete:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         vowels+=1
#     else:
#         consonants+=1
#     print()
# print(f"vowel : {vowels}")
# print(f"conwsonants : {consonants}")

# if vowels > consonants:
#     print("gvowel win")
# elif consonants > vowels:
#     print("onsonant win")
# elif vowels == consonants:
#     print("draw")

#13

# for i in range(6):
#     unit=int(input("enter number of unit:-"))

#     if unit <= 100:
#         bill = unit*5
#     elif unit <= 200:
#         bill = (100*5) + (unit - 100)*7
#     elif unit <= 400:
#         bill = 1300 + (unit-200 )*10
#     else:
#         bill = 3200 + (unit - 400)*15
#     print("bill is",bill)

#14

# sen1=input("enter your sentanse: ")
# wor=sen1.split()

# for word in wor:

#     vowels = 0
#     consonants = 0

#     for ch in word:

#         if ch.lower() in "aeiou":
#             vowels += 1

#         elif ch.isalpha():
#             consonants += 1

#     if vowels > consonants:
#         result = "Vowel Heavy"

#     elif consonants > vowels:
#         result = "Consonant Heavy"

#     else:
#         result = "Balanced"

#     print(word, "->", result)

#15

# even = 0
# odd = 0
# positive = 0
# negative = 0
# zero = 0

# largest = None

# for i in range(3):

#     for j in range(3):

#         num = int(input(f"Enter number [{i}][{j}]: "))

#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#         if num > 0:
#             positive += 1

#         elif num < 0:
#             negative += 1

#         else:
#             zero += 1

#         if largest is None or num > largest:
#             largest = num

# print("\n--- Result ---")
# print("Even count:", even)
# print("Odd count:", odd)
# print("Positive count:", positive)
# print("Negative count:", negative)
# print("Zero count:", zero)
# print("Largest number:", largest)

#16

# password = input("Enter password: ")

# uppercase = 0
# lowercase = 0
# digits = 0
# special = 0

# for ch in password:

#     if "A" <= ch <= "Z":
#         uppercase += 1

#     elif "a" <= ch <= "z":
#         lowercase += 1

#     elif "0" <= ch <= "9":
#         digits += 1

#     else:
#         special += 1

# total = len(password)

# upper_percent = (uppercase / total) * 100
# lower_percent = (lowercase / total) * 100
# digit_percent = (digits / total) * 100
# special_percent = (special / total) * 100

# print("\n--- Password Analysis ---")
# print("Uppercase:", uppercase, "=", upper_percent, "%")
# print("Lowercase:", lowercase, "=", lower_percent, "%")
# print("Digits:", digits, "=", digit_percent, "%")
# print("Special characters:", special, "=", special_percent, "%")

# highest = uppercase
# category = "Uppercase"

# if lowercase > highest:
#     highest = lowercase
#     category = "Lowercase"

# if digits > highest:
#     highest = digits
#     category = "Digits"

# if special > highest:
#     highest = special
#     category = "Special Characters"

# print("Dominating category:", category)

#17

# highest_marks = -1
# highest_student = ""

# for i in range(1, 6):

#     name = input(f"Enter name of student {i}: ")
#     marks = int(input("Enter marks: "))

#     if marks >= 90:
#         grade = "A"

#     elif marks >= 75:
#         grade = "B"

#     elif marks >= 60:
#         grade = "C"

#     elif marks >= 35:
#         grade = "D"

#     else:
#         grade = "F"

#     vowels = 0
#     consonants = 0

#     for ch in name:

#         if ch.lower() in "aeiou":
#             vowels += 1

#         elif ch.isalpha():
#             consonants += 1

#     characters = len(name)

#     if vowels > consonants:
#         name_result = "More vowels"

#     elif consonants > vowels:
#         name_result = "More consonants"

#     else:
#         name_result = "Equal"

#     print("\nName:", name)
#     print("Marks:", marks)
#     print("Grade:", grade)
#     print("Characters:", characters)
#     print("Vowels:", vowels)
#     print("Consonants:", consonants)
#     print("Name:", name_result)
#     print()

#     if marks > highest_marks:
#         highest_marks = marks
#         highest_student = name


# print("--- Final Result ---")
# print("Student with highest marks:", highest_student)
# print("Highest marks:", highest_marks)


#18

# balance = int(input("enter your balnce"))

# deposit_count = 0
# withdrawal_count = 0

# for i in range(2):
#     tranision=input("enter transion(deposit/withdrawal):-")
#     if tranision == "deposit":
#         amount=int(input("enter amount:-"))
#         balance+=amount
#         deposit_count+=1
#     elif tranision == "withdrawal":
#         amount=int(input("enter amount:-"))
#         if balance > amount:
#             balance-=amount
#             withdrawal_count+=1
#         elif balance < amount:
#             print("not enof balance")
#     elif balance <= 1000:
#         print("Low Balance")
#     else:
#         ("enter valid opration")
# print(f"total balance {balance}")
# print(f"total transion count {deposit_count+withdrawal_count}")
# print(f"deposit count:-{deposit_count}")
# print(f"withdrawal count:-{withdrawal_count}")

#19

# sentence = input("Enter a sentence: ")

# has_digit = False
# has_dot = False
# has_at = False
# password_like = False
# repeated_special = False

# special_count = 0
# previous_special = ""

# for ch in sentence:

#     if ch.isdigit():
#         has_digit = True

#     if ch == ".":
#         has_dot = True

#     if ch == "@":
#         has_at = True

#     if not ch.isalnum() and ch != " ":

#         special_count += 1

#         if ch == previous_special:
#             repeated_special = True

#         previous_special = ch

#     else:
#         previous_special = ""


# if has_digit and has_at and len(sentence) >= 8:
#     password_like = True

# if password_like or repeated_special:
#     classification = "Suspicious"

# elif has_digit or has_dot or has_at:
#     classification = "Review"

# else:
#     classification = "Safe"



# print("Contains digits:", has_digit)
# print("Contains URL-like '.' :", has_dot)
# print("Contains '@':", has_at)
# print("Password-like:", password_like)
# print("Repeated special characters:", repeated_special)
# print("Security Classification:", classification)

#21


# conq=0
# conq1=0
# conq2=0
# conq3=0
# discount = 0
# total_dis=0
# for i in range(10):
#     price=int(input("enter price of product:-"))
#     if price >= 5000:
#         discount = price * 20 / 100
#         conq3 += 1

#     elif price >= 3000:
#         discount = price * 15 / 100
#         conq2 += 1

#     elif price >= 1000:
#         discount = price * 10 / 100
#         conq1 += 1

#     else:
#         discount = 0
#         conq += 1
#     total_dis+=discount
#     final_price= price-discount

#     print("Original Price:", price)
#     print("Discount:", discount)
#     print("Final Price:", final_price)
#     print()
# print("20% Discount Products:", conq3)
# print("15% Discount Products:", conq2)
# print("10% Discount Products:", conq1)
# print("No Discount Products:", conq)
# print("Total Discount: ₹", total_discount)

#22 dout

#23

# junior = 0
# mid = 0
# senior = 0
# executive = 0

# total_salary = 0

# for i in range(1, 9):

#     salary = float(input(f"Enter salary of employee {i}: "))

#     total_salary += salary

#     if salary < 25000:
#         junior += 1
#         category = "Junior"

#     elif salary <= 50000:
#         mid += 1
#         category = "Mid"

#     elif salary <= 100000:
#         senior += 1
#         category = "Senior"

#     else:
#         executive += 1
#         category = "Executive"

#     print("Category:", category)


# average_salary = total_salary / 8

# print("\n--- Final Result ---")
# print("Junior:", junior)
# print("Mid:", mid)
# print("Senior:", senior)
# print("Executive:", executive)
# print("Average Salary: ₹", average_salary)

#24 dout

# sentence = input("Enter a sentence: ")
# secret = input("Enter secret word: ")

# count = 0
# first_position = -1

# for i in range(len(sentence) - len(secret) + 1):

#     match = True

#     for j in range(len(secret)):

#         if sentence[i + j] != secret[j]:
#             match = False
#             break

#     if match:
#         count += 1

#         if first_position == -1:
#             first_position = i


# if count > 0:
#     print("Secret word found")
#     print("Starting position:", first_position)
#     print("Number of occurrences:", count)

# else:
#     print("Secret word not found")

#25

# n = int(input("Enter n: "))

# for i in range(1, n + 1):

#     for j in range(1, i + 1):

#         if j % 3 == 0 and j % 5 == 0:
#             print("F", end=" ")

#         elif j % 3 == 0:
#             print("T", end=" ")

#         elif j % 2 == 0:
#             print("E", end=" ")

#         else:
#             print("O", end=" ")

#     print()

#26
# Poor = 0
# average = 0
# good =0
# excellent=0
# outstanding=0
# typ=""
# rat1=0

# for i in range(10):
#     rat = int(input("enter ratings of movie(0-10):-"))
#     if rat>9:
#         outstanding +=1
#         typ="outstanding"
#         rat1+=rat
#     elif rat > 7:
#         excellent+=1
#         typ="excellent"
#         rat1+=rat
#     elif rat > 5:
#         good += 1
#         typ="good"
#         rat1+=rat
#     elif rat > 3:
#         average+=1
#         typ="average"
#         rat1+=rat
#     elif rat > 0:
#         Poor+=1
#         typ="poor"
#     print(f"movie is {typ}")
# print(f"poor:{Poor}")
# print(f"average:{average}")
# print(f"good:{good}")
# print(f"excellent:{excellent}")
# print(f"outstanding:{outstanding}")


#27 in dout by ai

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# for i in range(len(words)):
#     already_checked = False

#     for k in range(i):
#         if words[i] == words[k]:
#             already_checked = True

#     if already_checked == False:
#         count = 0

#         for j in range(len(words)):
#             if words[i] == words[j]:
#                 count += 1

#         if count > 1:
#             print(words[i], ":", count)

#28
# high =0
# high1=False
# num123=0
# for i in range(1, 11):

#     num = input(f"Enter number {i}: ")

#     even = 0
#     odd = 0

#     for digit in str(num):

#         if int(digit) % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     print("Even digits:", even)
#     print("Odd digits:", odd)


#     if even > odd:
#         print("Even occurs more")
#     elif odd > even:
#         print("Odd occurs more")
#     else:
#         print("Equal")
       
#     print()

#     if even > high:
#         high=even
#         high1=True
#         num123=num
# print("highest even:",high)
# print(f"heighest event number is {num123}")

#29 in dout

# for i in range(5):
#     email = input("Enter email: ")

#     at_count = 0
#     at_position = -1

#     for j in range(len(email)):
#         if email[j] == "@":
#             at_count += 1
#             at_position = j

#     if " " in email:
#         print("Invalid")

#     elif at_count != 1:
#         print("Invalid")

#     elif at_position == 0:
#         print("Invalid")

#     elif at_position == len(email) - 1:
#         print("Invalid")

#     else:
#         domain = email[at_position + 1:]

#         dot_found = False

#         for ch in domain:
#             if ch == ".":
#                 dot_found = True
#                 break

#         if dot_found:
#             print("Valid")
#         else:
#             print("Invalid")

#30

# s = input("Enter a string: ")

# same = 0
# different = 0
# both_vowels = 0
# both_digits = 0

# vowels = "aeiouAEIOU"

# for i in range(len(s)):
#     for j in range(i + 1, len(s)):

#         # Same characters
#         if s[i] == s[j]:
#             same += 1
#         else:
#             different += 1

#         if s[i] in vowels and s[j] in vowels:
#             both_vowels += 1

#         if s[i].isdigit() and s[j].isdigit():
#             both_digits += 1

# print("Same characters:", same)
# print("Different characters:", different)
# print("Both vowels:", both_vowels)
# print("Both digits:", both_digits)

#31


# passed = 0
# failed = 0
# highest = 0
# lowest = 100

# for student in range(1, 6):
#     total = 0
#     is_pass = True

#     print("\nStudent", student)

#     for subject in range(1, 6):
#         marks = int(input("Enter marks for subject " + str(subject) + ": "))

#         total = total + marks

#         if marks < 35:
#             is_pass = False

#     percentage = total / 5

#     if not is_pass:
#         grade = "F"
#         failed = failed + 1
#     else:
#         passed = passed + 1

#         if percentage >= 90:
#             grade = "A+"
#         elif percentage >= 80:
#             grade = "A"
#         elif percentage >= 70:
#             grade = "B"
#         elif percentage >= 60:
#             grade = "C"
#         elif percentage >= 50:
#             grade = "D"
#         else:
#             grade = "E"

#     if percentage > highest:
#         highest = percentage

#     if percentage < lowest:
#         lowest = percentage

#     print("Total:", total)
#     print("Percentage:", percentage, "%")
#     print("Grade:", grade)

# print("Passed students:", passed)
# print("Failed students:", failed)
# print("Highest percentage:", highest, "%")
# print("Lowest percentage:", lowest, "%")

#32

# password = input("Enter secret password: ")

# for attempt in range(1, 6):
#     entered = input("Enter password attempt " + str(attempt) + ": ")

#     matching = 0

#     if len(password) == len(entered):
#         for i in range(len(password)):
#             if password[i] == entered[i]:
#                 matching = matching + 1
#     else:
#         limit = min(len(password), len(entered))

#         for i in range(limit):
#             if password[i] == entered[i]:
#                 matching = matching + 1

#     print("Matching characters:", matching)

#     if len(password) == len(entered) and matching == len(password):
#         print("Correct")
#     else:
#         print("Incorrect")

#33 by ai

# n = int(input("Enter n: "))

# for row in range(1, n + 1):
#     for num in range(1, row + 1):

#         count = 0

#         if num >= 2:
#             for i in range(1, num + 1):
#                 if num % i == 0:
#                     count += 1

#         if count == 2:
#             print("P", end=" ")
#         elif num % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")

#     print()


#35

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):

#         prime = True

#         if j < 2:
#             prime = False
#         else:
#             for k in range(2, j):
#                 if j % k == 0:
#                     prime = False
#                     break


#         if prime:
#             print("P", end=" ")
#         elif j % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")

#     print()

#36


# total=0
# rav=0
# for i in range(1,6):
#     print("coustmer",i)
#     for j in range(3):
#         price=int(input("enter price:-"))
#         total+=price
#     if total >= 2000:
#         dis=(total*0.2)
#     elif total >= 1000:
#         dis=(total*0.1)
#     else:
#         dis=0

#     total-=dis

#     mam = input("you are mamber:-")
#     if mam == "yes":
#         dis=(total*0.05)
#     else :
#         dis = 0

#     total-=dis
#     print(f"your total bill is {total}₹")
#     rav+=total
# print(f"total ravenue of restaurant is {rav}₹")

#37

# word = input("Enter a word: ")

# for i in range(len(word)):
#     for j in range(i + 1):
#         print(word[j], end="")
#     print()

# print("revers string")

# for i in range(len(word) - 1, -1, -1):
#     for j in range(i + 1):
#         print(word[j], end="")
#     print()

#38

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# for i in range(len(words)):
#     frequency = 0

#     already_checked = False

#     for k in range(i):
#         if words[k] == words[i]:
#             already_checked = True

#     if already_checked == False:

#         for j in range(len(words)):
#             if words[i] == words[j]:
#                 frequency += 1

#         if frequency >= 2:

#             print("Word:", words[i])
#             print("Frequency:", frequency)

#             if frequency == 2:
#                 print("Repeated")
#             elif frequency <= 4:
#                 print("Frequently Repeated")
#             else:
#                 print("Highly Repeated")

#             print()

#39

# for i in range (1,9):
#     print(f"passanger{i}")
#     age = int(input("enter your age:-"))
#     dis = int(input("enter distance you want to cover:-"))
#     price=10*dis
#     if age > 60:
#         dis = price*0.3
#         price-=dis
#     elif age <12:
#         if age > 5:
#             dis = price*.5
#             price-=dis
#     elif age < 5:
#         price=0
#         price-=dis
#     else:
#         price=price
    
#     print(f"you travel {dis}km and your ticket price {price}₹")

#40

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# if len(str1) != len(str2):
#     print("Not Mirror Compatible")
# else:
#     mirror = True

#     for i in range(len(str1)):
#         if str1[i] != str2[len(str2) - 1 - i]:
#             mirror = False
#             break

#     if mirror:
#         print("Mirror Compatible")
#     else:
#         print("Not Mirror Compatible")

#41

# for i in range(1,8):
#     present = 0
#     absent = 0
#     print(f"student{i}")
#     for j in range(1,6):
#         attendence=input(f"student in day{j} is p/a:-")
#         if attendence == "p":
#             present+=1
#         else:
#             absent+=1
       
#     aper = (present/5)*100
#     print(f"your atendence is {aper}%")
#     if aper > 90:
#         print("Excellent")
#     elif aper > 75:
#         print("Good")
#     else:
#         print("warning")

#42


# msum=0
# ssum=0
# meven=0
# seven=0
# for i in range(1,5):
#     for j in range(1,5):
#         in1=int(input(f"enter number({i},{j})"))
#         if i == j:
#             msum+=in1
#             if in1%2 == 0:
#                 meven+=1
#         elif i+j == 5:
#             ssum+=in1
#             if in1%2 == 0:
#                 seven+=1
# print(f"sum of total number in main diogonal:-{msum}") 
# print(f"sum of total number in secondry diogonal:-{ssum}")
# print(f"sum of total even number in main diogonal:-{meven}")
# print(f"sum of total even number in main diogonal:-{seven}")


#43

# word = input("Enter a word: ")

# password = ""

# for ch in word:

#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             password += "@"

#         if ch.lower() not in "aeiou":
#             password += ch.lower()

#     if ch.isdigit():
#         password += "#"

#     if ch == " ":
#         password += "_"

#     if not ch.isalpha() and not ch.isdigit() and ch != " ":
#         password += "!"

# print("Transformed result:", password)


#44

# balance = int(input("enter you bank balnce:-"))
# total_deposits = 0
# total_withdrawals = 0

# n = int(input("Enter number of transactions: "))

# for i in range(n):
#     transaction = input("Enter D for Deposit or W for Withdrawal: ")
#     amount = int(input("Enter amount: "))

#     if transaction == "D":
#         balance = balance + amount
#         total_deposits = total_deposits + amount

#     elif transaction == "W":
#         balance = balance - amount
#         total_withdrawals = total_withdrawals + amount

#     if balance < 0:
#         print("Balance:", balance, "Overdraft")

#     elif balance < 500:
#         print("Balance:", balance, "Low Balance")

#     else:
#         print("Balance:", balance, "Normal")

# print("Total Deposits:", total_deposits)
# print("Total Withdrawals:", total_withdrawals)
# print("Final Balance:", balance)

#45 by ai

# word1 = input("Enter first word: ")
# word2 = input("Enter second word: ")

# result = ""

# if len(word1) < len(word2):
#     length = len(word1)
# else:
#     length = len(word2)

# for i in range(length):
#     if word1[i] == word2[i]:
#         result = result + "S"
#     else:
#         result = result + "D"

# print("Result:", result)

# if len(word1) > len(word2):
#     print("Extra characters:", word1[length:])

# elif len(word2) > len(word1):
#     print("Extra characters:", word2[length:])

#46

# n = int(input("Enter n: "))

# for i in range(n):
#     for j in range(n):

#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end="")

#         elif (i + j) % 2 == 0:
#             print("E", end="")

#         else:
#             print("O", end="")

#     print()


#47


# available = 0
# low = 0
# critical = 0
# out =0
# hq=0
# hp=""
# for i in range (1,9):
#     pn=input(f"enter name of product{i}:-")
#     qn=int(input("enter quantities:-"))
#     if qn > 20:
#         print(f"{pn} is Available quantit")
#         available+=1
#     elif qn > 5:
#         print(f"{pn}  is in low quantity")
#         low+=1
#     elif qn > 0:
#         print(f"{pn} is in Critical quantit")
#         critical+=1
#     else:
#         print(f"out of stock")
#         out+=1
#     if qn > hq:
#         hp = pn


# print(f"in available catgory product is {available}")
# print(f"in critical catgory product is {critical}")
# print(f"in low catgory product is {low}")
# print(f"in out of stock catgory product is {out}")
# print(f"highest quantity product is {hp}")

#48

# for i in range(10):
#     username = input("Enter username: ")

#     letters = 0
#     digits = 0
#     underscore = 0
#     spaces = 0
#     special = 0

#     for ch in username:
#         if ch.isalpha():
#             letters += 1
#         elif ch.isdigit():
#             digits += 1
#         elif ch == "_":
#             underscore += 1
#         elif ch == " ":
#             spaces += 1
#         else:
#             special += 1

#     length = len(username)

#     print("Letters:", letters)
#     print("Digits:", digits)
#     print("Underscore:", underscore)
#     print("Spaces:", spaces)
#     print("Special characters:", special)
#     print("Length:", length)

#     if spaces > 0 or special > 0 or length < 5 or length > 15:
#         print("Invalid")
#     elif underscore > 0:
#         print("Acceptable")
#     else:
#         print("Clean")


#49 by ai

# sentences = []

# for i in range(10):
#     sentence = input("Enter sentence " + str(i + 1) + ": ")
#     sentences.append(sentence)

# word = input("Enter search word: ")

# total = 0

# for i in range(10):
#     sentence = sentences[i].lower()
#     search_word = word.lower()

#     words = sentence.split()
#     occurrences = 0

#     for j in range(len(words)):
#         if words[j] == search_word:
#             occurrences += 1

#     if occurrences > 0:
#         print("Sentence", i + 1, "->", occurrences, "time(s)")
#         total += occurrences

# print("Total occurrences:", total)

#50

# total_v = 0
# total_c = 0
# total_d = 0
# total_s = 0

# high_score = -1
# high_vowels = -1
# high_digits = -1

# for i in range(10):

#     text = input("Enter text: ")

#     v = 0
#     c = 0
#     d = 0
#     s = 0
#     score = 0

#     for ch in text:

#         if ch.lower() in "aeiou":
#             v += 1
#             score += 2

#         elif ch.isalpha():
#             c += 1
#             score += 1

#         elif ch.isdigit():
#             d += 1
#             score += 3

#         elif ch == " ":
#             pass

#         else:
#             s += 1
#             score += 4

#     longest = ""
#     for word in text.split():
#         if len(word) > len(longest):
#             longest = word

#     repeated = 0
#     for j in range(len(text)):
#         for k in range(j):
#             if text[j] == text[k]:
#                 repeated += 1
#                 break

#     print("Vowels:", v, "Consonants:", c, "Digits:", d)
#     print("Special:", s, "Longest:", longest)
#     print("Repeated:", repeated, "Score:", score)

#     if score > high_score:
#         high_score = score
#         high_score_text = text

#     if v > high_vowels:
#         high_vowels = v
#         high_vowels_text = text

#     if d > high_digits:
#         high_digits = d
#         high_digits_text = text

#     total_v += v
#     total_c += c
#     total_d += d
#     total_s += s


# print("\n--- FINAL REPORT ---")
# print("Highest Score:", high_score_text)
# print("Most Vowels:", high_vowels_text)
# print("Most Digits:", high_digits_text)

# print("Total Vowels:", total_v)
# print("Total Consonants:", total_c)
# print("Total Digits:", total_d)
# print("Total Special:", total_s)

# if total_v + total_c > total_d and total_v + total_c > total_s:
#     print("Text Heavy")
# elif total_d > total_v + total_c and total_d > total_s:
#     print("Number Heavy")
# elif total_s > total_v + total_c and total_s > total_d:
#     print("Special Character Heavy")
# else:
#     print("Balanced")