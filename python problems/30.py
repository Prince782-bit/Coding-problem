 # 9: count the frequency of char in a string.
# s = "hello"
# fre = {char: s.count(char) for char in set(s)}
# print(fre)



# # 10: revers words in a setence
# s = "hello python"
# rev = " ".join(s.split()[::-1])
# print(rev)


# 11: find common element in two list
# list1 = [1,2,3,4,5]
# list2 = [3,4,5,6,7]
# common = list(set(list1) & set(list2))
# print(common)



# # 12: find the most frequent element in a list
# lst = [1,2,3,4,3,3,3,3,2]
# most = max(set(lst), key=lst.count)
# print(most)



# # 13: find the first non repeating char
# s = "swiss"
# for char in s:
#     if s.count(char) == 1:
#         print(char)
#         break



# # 14: find the substring of a string
# s = "abc"
# sub = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
# print(sub)


# # 15: merge two sorted list
# list1 = [1,3,5]
# list2 = [2,4,6]
# merged = sorted(list1 + list2)
# print(merged)


# # 16: swap two number without a temporary variable
# a, b = 5, 10
# a, b = b, a
# print(a, b)


# # remove duplicates from the list
# lst = [1,2,2,3,3,4,4,5,6]
# unique = list(set(lst))
# print(unique)


# # flatten a nested list
# nested = [[1,2], [3,4], [5]]
# flat = [item for sublist in nested for item in sublist]
# print(flat)


# # List comprehension with condition :
# result = [x for x in range(10) if x%2 == 0]
# print(result)


# # Exception handling
# try:
#     x = 1/0
# except ZeroDivisionError as e:
#     print("Error:",e)



# # using xip to combine two lists
# names = ["a","b","c"]
# score = [90,80,70]
# combine = dict(zip(names,score))
# print(combine)



# # count vowel in string
# s = "hello vikas bhai"
# vowel = "AEUIOaeuio"
# count = sum(1 for char in s if char in vowel)
# print(count)


# # convert a string to title case
# s = "hello python"
# print(s.title())


# # find the largest and smallest number
# lst = [4,2,7,8,9,1]
# print("Max:",max(lst))
# print("Min:", min(lst))


# # check if a number is prime.
# num = 18
# if num > 1:
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             print("Not prime")
#             break
#     else:
#         print("prime")
# else:
#     print("Not prime")


# # find the gcd
# def gcd(a,b):
#     while b:
#         a,b = b,a%b
#         return a
# print(gcd(36,60))

# # find the lcm
# def lcm(a,b):
#     return abs(a*b)  
# print(lcm(12,18))



# # Convert celsius to fahrenheit: 0 celsius = 32 fahrenheit:
# celsius = int(input("Enter temperature in celsius: "))
# fahrenheit = (celsius * (9/5))+32
# print("The converted value is", fahrenheit, "Fahrenheit")



# # check if a number is positive, negative or 0:
# num = int(input("Enter a number here:"))
# if num > 0:
#     print("It is a positive number")
# elif num == 0:
#     print("It is zero")
# else:
#     print("It is a negative number")



# # Find largest among three number:
# num1 = int(input("Enter 1st number here: "))
# num2 = int(input("Enter 2st number here: "))
# num3 = int(input("Enter 3st number here: "))
# if (num1 > num2) and (num1 > num3):
#     print(num2, "is the largest number")
# elif (num2 > num1) and (num2 > num3):
#     print(num2, "is the largest number")
# else:
#     print(num3, "is the largest number")



# # check if a number is odd or even:
# num = int(input("Enter a number here: "))
# if num % 2 == 0:
#     print("It is an even number")
# else:
#     print("It is an odd number")



# # reverse string:
# str1 = "Where are you"
# str2 = " "
# for i in str1:
#     str2 = i + str2
# print(str1)
# print(str2)


# # convert string to list:
# str = "Where are you going"
# print(str.split())


# # max repeated char:
# str = "vikaasssssssssss"
# ch = {}
# for i in str:
#     if i in ch:
#         ch[i] += 1
#     else:
#         ch[i] = 1
# print(ch)
# max_char = max(ch,key=ch.get)
# print(max_char)


# # reverse string:
# s = "sky is the blue"
# l = s.split()
# l = l[::-1]
# l = " ".join(l)
# print(l)


# # lenght of string:
# str = input("Enter any anything: ")
# a = len(str)
# print("lenght of string:",a)


# # sort list:
# list = [3,1,6,4,22,45]
# list.sort()
# print(list)



# # find the second largest number:
# list = [3,5,1,8,2]
# list.sort()
# print(list)
# print(list[-2])


# # reverse list:
# my_list = [1,2,3,4,5,6]
# my_list.reverse()
# print(my_list)


# # 1: string palindrome or not
# def is_palindrome(s):
#     return s == s[::-1]
# print(is_palindrome("python"))
# print(is_palindrome("madam"))

# #  OR

# s = input("Enter the string: ")
# if s == s[::-1]:
#     print("yes")
# else:
#     print("No")



# # 2: generate random password in string
# import random
# import string
# def gen(length):
#     pas = " ".join(random.choices(string.ascii_letters + string.digits, k = length))
#     return pas
# print(gen(4))


# # 3: count number of vowels in string.
# def s_count(string):
#     vowels = "aeiouAEUIO"
#     count = 0
#     for i in string:
#         if i in vowels:
#             count += 1 
#     return count
# print(s_count("vikas"))

# OR

# str = input("Enter the string:")
# for i in str:
#     if i in "aeuioAEUIO":
#         print(i, end=" ")



# # 4: reverse the string
# str1 = "where are you"
# str2 = " "
# for i in str1:
#     str2 = i + str2
# print(str1)
# print(str2)



# # 5: convert string to list
# str = "where are you going"
# print(str.split(" "))


# # 6: find the max repeated char
# str = "viskasssssssssssssssaaaaaaaaaaa"
# ch = {}
# for i in str:
#     if i in ch:
#         ch[i] += 1
#     else:
#         ch[i] = 1
# print(ch)
# max_char = max(ch, key=ch.get)
# print(max_char)



# # 7: 
# str = "the sky is blue"
# l = str.split()
# l = l[::-1]
# l = " ".join(l)
# print(l)



# # 8: common letter between two string.
# def common_letter():
#     str1 = input("Enter the 1st string: ")
#     str2 = input("Enter 2nd string: ")
#     s1 = set(str1)
#     s2 = set(str2)
#     l = s1 & s2
#     print(l)
# common_letter()




# # 9: count the freuncy of words in string
# def freq():
#     str = input("Enter the string: ")
#     l1 = str.split()
#     d = {}
#     for i in l1:
#         if i not in d.keys():
#             d[i] = 0
#         d[i] = d[i]+1
#     print(d)
# freq()




# # 10: length of string
# s = input("Enter the string: ")
# a = len(s)
# print("Length of string: ",a)



# # 11: sort the list
# list = [3,5,1,8,2]
# list.sort()
# print(list)



# import pyjokes
# # print("Printing Jokes...")
# joke  = pyjokes.get_joke()
# print(joke)



# # 12: write a python program to print poem "Twinkle Twinkle Little Start"
# print('''✨ Twinkle, Twinkle, Little Star ✨

# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark;
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often through my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.
#       ''')


# # 13: Use REPL and print the table of 5 unsing it.
# for i in range(1,11):
#     print(f"5 x {i} = {5 * i}")



# 14: write a program to print the contents of a directory using the 
# os module, search online for the function which does that.
# import os
# directory_path = "/"
# contents = os.listdir(directory_path)
# for item in contents:
#     print(item)



# # 15: write a program to add two numbers.
# a = 1 
# b = 5
# print(a + b)


# # 16: Find remainder when a number is divided by z.
# a = 34
# b = 5
# print("Remainder:",a % b)


# # 17: check the type of variable assigned using int(input()) function.
# a = int(input("Enter the value of a :"))
# print(type(a))


# 18: use comparison operator to find out wheather a given variable a 
# given variable a is greater than "b" or not. take a = 34 and b = 80.
# a = int(input("Enter number a:"))
# b = int(input("Enter number b:"))
# print("A is greater than b is:", a>b)


# # 19: find an average of two number entered by the user.
# a = int(input("Enter number 1:"))
# b = int(input("Enter number 2:"))
# print("The average of these two numbers is:",(a+b)/2)


# # 20: calculate the square of a number entered by the user.
# a = int(input("Enter your number:"))
# print("The square of the number is:", a ** 2)


# 21: create two variables. one to store your birth year and another
#  one to store current year. Now calculate your age using these two variables 
# birth_year = 2002
# current_year = 2025
# age = current_year - birth_year
# print("Your age is:",age)


# 22: Store your first, middle and last name in three different variables 
# and then print your full name using these variables
# first = "Prince"
# middle = "ydu"
# last = "vanshi"
# print("Full name is:",first+" "+middle+last)


# 23: You have a football field that is 92 meter long and 48.8 meter wide. Find out total
#    area using python and print it
# lenght = 92
# width = 48.8
# area = lenght * width
# print("Total area of football field is:",area)


# 24: You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?
# num_packets = 9
# cost_per_packet = 1.49
# total_cost = num_packets * cost_per_packet
# money_paid = 20
# cash_back = money_paid - total_cost
# print("cash back:",cash_back)


# 25: You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
# length = 5.5
# area = length ** 2
# cost = area * 500
# print("Total cost for bathroom tiles replacement is:",cost)



# # 26: print binary representation of number 10
# num = 10
# print("Binary of number 10 is:",format(num,"b"))







