# 1st: Reverse string.
# str = "prince is a student."
# reverse = str[::-1]
# print(reverse)



# # 2nd: Palindrome is string.
# str = "madam"
# if str == str[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    


# # 3rd: COunt the frequency.
# num = [1,1,1,2,2,2,3,4,4,5,5,5,6,7]
# freq = {}
# for n in num:
#     freq[n] = freq.get(n,0)+1
# print(freq)



# # 4th: Find the factorial.
# def factorial(n):
#     return 1 if n == 0 else n * factorial(n-1)
# print(factorial(5))



# # 5th: Find the largest element in list.
# num = [1,32,445,67,78,34]
# largest = max(num)
# print(largest)




# # 6th: Remove duplicates from list.
# num = [2,2,1,1,3,4,5,5]
# unique = list(set(num))
# print(unique)



# # 7th: Fibonacci series.
# num = 8
# a,b = 0,1
# fib = []
# for _ in range(num):
#     fib.append(a)
#     a,b = b,a+b
# print(fib)




# # 8th: Find the second largest number.
# num = [23,445,56,778,67,56,34]
# nums = list(set(num))
# nums.sort()
# print(nums[-2])



# # 9th: COunt the vowels in string.
# str = "interview placement"
# vowels = "aeuio"
# count = sum(1 for ch in str if ch in vowels)
# print(count)



# # 10th: Find the missing number.
# nums = [1,3,5,6,7]
# n = 6
# missing = set(range(1,n+1)) - set(nums)
# print(missing)




# # 11th: Find the prime numbers in a range.
# primes = []
# for num in range(2,21):
#     for i in range(2, int(num ** 0.5)+1):
#         if num % i == 0:
#             break
#     else:
#         primes.append(num)
# print(primes)





# # 12th: Find the anagrams of a word from list.
# word = "listen"
# words = ["enlist","google","silent","inlets","stone"]
# anagrams = [w for w in words if sorted(w) == sorted(word)]
# print(anagrams)




# # 13th: Find the intersection.
# a = [1,2,3,4,5]
# b = [4,5,6,7,8]
# common = list(set(a) & set(b))
# print(common) 




# # 14th: Check armstrong number.
# num = 153
# s = sum(int(d) ** 3 for d in str(num))
# print(num == s)




# # 15th: Find all substring of a string.
# str = "abc"
# subs = [str[::j] for i in range(len(str)) 
#         for j in range(i+1, len(str) + 1)]
# print(subs)




# # 16th: Find first non-repeating char.
# s = "swiss"
# for ch in s:
#     if s.count(ch) == 1:
#         print(ch)
#         break





# # 17th: Sort dictionary by values.
# d = {"a":3, "b":1,"c":2}
# sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
# print(sorted_dict)



# # 18th: Flatten a nested list.
# nested = [[1,2],[3,4],[5]]
# flat = [x for sublist in nested for x in sublist]
# print(flat)



# # 19th: Find duplicate element in list.
# num = [1,2,3,2,4,5,3,2,2]
# duplicates = [x for x in set(num) if num.count(x) > 1]
# print(duplicates)



# # 20th: Two string are anagrams.
# def is_anaram(s1,s2):
#     return sorted(s1) == sorted(s2)
# print(is_anaram("listen","silent"))



# # 21th: Find the GCD.
# import math 
# a,b = 36,60
# print(math.gcd(a,b))





# # 22th: Find the LCM.
# import math
# a,b = 12,15
# lcm = abs(a*b)//math.gcd(a,b)
# print(lcm)



# # 23th: Find the largest word in sentence.
# sentence = "python placement interview preparation"
# words = sentence.split()
# largest = max(words, key=len)
# print(largest)




# # 24th: COunt digit and alphabets in a string.
# str = "skejng34t3n34jn"
# digits = sum(c.isdigit() for c in str)
# letters = sum(c.isalpha() for c in str)
# print(digits,letters)




# # 25th: Find all permutations of a string.
# from itertools import permutations
# s = "abc"
# perms = [" ".join(p) for p in permutations(s)]
# print(perms)






#1st: Reverse each word in a sentence.
# sentece = "python interview placement"
# rev = " ".join(word[::-1] for word in sentece.split())
# print(rev)



# # 2nd: Find common char between two string.
# s1 = "placement"
# s2 = "interview"
# common = set(s1) & set(s2)
# print(common)




# # 3rd: Swap two numbers.
# a,b = 5,10
# a,b = b,a
# print(a,b)



# # 4th: Check if string contains only digits.
# s1 = "12345"
# s2 = "123wrf456"
# print(s1.isdigit())
# print(s2.isdigit())




# # 5th: Find sum of digit of a number.
# num = 985
# digit_sum = sum(int(d) for d in str(num))
# print(digit_sum)


# # 6th: Find all even number from a list.
# nums = [1,2,3,4,4,5,6,7,8]
# evens = [n for n in nums if n%2 == 0]
# print(evens)



# # 7th: Count occurrence of each char in str.
# str = "interview"
# freq = {ch: str.count(ch) for ch in set(str)}
# print(freq)



# # 8th: Reverse a number.
# num = 12345
# rev = int(str(num)[::-1])
# print(rev)




# # 9th: Find all average of number.
# nums = [10,20,30,40,50]
# avg = sum(nums)/len(nums)
# print(avg)




# # 10th: Find most frequent element.
# num = [1,2,2,3,3,4,4,4,5,6,7]
# most = max(set(num), key=num.count)
# print(most)




# # 11th: Capitalize first letter of each word.
# s = "python data analysis interview"
# title = " ".join(word.capitalize() for word in s.split())
# print(title)




# # 12th: Find the common element in three list.
# a = [1,2,3,4]
# b = [2,3,4,5]
# c = [0,2,3,7]
# common = list(set(a) & set(b) & set(c))
# print(common)



# # 13th: Remove all whitespace.
# s = "  data analysis     interview"
# clean = "".join(s.split())
# print(clean)




# # 14th: count words in a sentence.
# sentence = "python interview question and answer"
# count = len(sentence.split())
# print(count)





# # 15th: string palindrome.
# def is_palindrome(str):
#     return str == str[::-1]
# print(is_palindrome("madam"))

# str = input("Enter the string: ")
# if str == str[::-1]:
#     print("yes")
# else:
#     print("No")



# # 16th: count vowel in string.
# def s_count(str):
#     vowels = "aeuio"
#     count = 0
#     for i in str:
#         if i in vowels:
#             count += 1
#     return count
# print(s_count("prince"))

# str = input("Enter the string: ")
# for i in str:
#     if i in "aeiou":
#         print(i, end=" ")



# # 17th: common letter in two string.
# def common_l():
#     str1 = "kamni"
#     str2 = "prince"
#     s1 = set(str1)
#     s2 = set(str2)
#     common = s1 & s2
#     print(common)
# common_l()




# # 18th: Access the element of the list.
# num = [1,2,3,4,5,6]
# x = num[3]
# print("Third element: ",x)



# # 19th: list comprehension.
# x = [i for i in range(100)]
# print(x)

# s = [i for i in range(10) if i>5]
# print(s)



# # 20th : access by slice
# list = ["kanpur","pulhrayan","lucknow","bhopal","indore"]
# print(list)
# print(list[0:])
# print(list[0::2])
# print(list[3])
# print(list[3], list[4])




# # 21th: Pre define variable
# num1 = 30
# num2 = 40
# sum = num1 + num2
# print("The sum of the provided two number is",sum)



# # 22th: with user-input
# num1 = float(input("Enter a number here: "))
# num2 = float(input("Enter another number here :"))
# sum = num1 + num2
# print("The sum of the provided two number is", sum)



# # 23th: Using exponentiation 
# num1 = int(input("Enter a number here: "))
# sr = num1 ** (1/2)
# print("The square of the given number is :",sr)



# # 24th: using module
# import math
# num = int(input("Enter a number here: "))
# sr = math.sqrt(num)
# print("The square root of the given number is ",sr)



# # 25th: area of the triangle
# height = float(input("Enter the base of the triangle: "))
# base = float(input("Enter the base of the triangle: "))
# area = (0.5)*base*height
# print("The area of the triangle is :",area)



# # 26th: to swap two variable
# x = 13
# y = 12
# temp = x
# print("The value of temp variable is ", temp)
# x = y
# print("The value to temp x is ", x)
# y = temp
# print("The value of y is ",y)

# # next method
# x = 12
# y = 13
# x,y = y,x
# print("The value of x is ", x)
# print("The value of y is ", y)




# # 27th: to check leap year
# year = int(input("Enter a year: "))
# if (year%400 == 0) and (year % 100 == 0):
#     print(year, "is a leap year")
# elif (year % 4 == 0) and (year % 100 != 0):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")



# # 28th: generate random number
# import random
# num = random.randint(1,10)
# print(num)




# # 29th : convert kilometers to miles= 1km: 0.621371mile
# km  = float(input("Enter your value in kms: "))
# miles = (0.621371)*km
# print(km, "kms will be", miles,"miles")





# # 30th : Convert celsius to fahrenheit : 0 celsius = 32 fahrenheit
# celsius = int(input("Enter temperature in celsius: "))
# fahrenheit = (celsius * (9/5)) + 32
# print("The converted value is",fahrenheit,"Fahrenheit")



