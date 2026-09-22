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


# print("\n--- Character Category Count ---")
# print("Vowels:", vowel)
# print("Consonants:", consonant)
# print("Digits:", digit)
# print("Special Characters:", special)

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


# for i in range(5):
#     user=input(f"enter user name{i}")

#     lengh=len(user)
#     digit = 0
#     under=0
#     invalid = False

#     if user[0].isalpha():
#         first_character = True
#     else:
#         first_character = False

#     for wr in user:
#         if wr.isdigit():
#             digit+=1
#         elif wr == "_":
#             under+=1
#         elif wr.isalpha():
#             pass
#         else:
#             invalid = True

#         if invalid:
#             result = "Invalid"
#         elif lengh >= 8 and first_character and digit >= 1:
#             result = "Valid"
#         else:
#             result= "Needs Improvement"

#         print("lengh",lengh)
#         print("digit",digit)
#         print("underscore",under)
#         print("result",result)
#         print()



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


# print("\n--- Security Analysis ---")
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
high =0
high1=False
num123=0
for i in range(1, 11):

    num = input(f"Enter number {i}: ")

    even = 0
    odd = 0

    for digit in str(num):

        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even digits:", even)
    print("Odd digits:", odd)


    if even > odd:
        print("Even occurs more")
    elif odd > even:
        print("Odd occurs more")
    else:
        print("Equal")
       
    print()

    if even > high:
        high=even
        high1=True
    if high1:
        num123=num
print("highest even:",high)
print(f"heighest event number is {num123}")