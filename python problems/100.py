# 1) Print Hello World
# print("Hello World")

# 2) Print Your Name
# name = "Prince"
# print(name)


# 3) Add Two Numbers
# a = 10
# b = 20
# print(a + b)


# 4) Subtract Two Numbers
# a = 20
# b = 5
# print(a - b)

# 5) Multiply Two Numbers
# a = 6
# b = 7
# print(a * b)

# 6) Divide Two Numbers
# a = 20
# b = 4
# print(a / b)

# 7) Find Remainder
# a = 17
# b = 5
# print(a % b)

# 8) Swap Two Numbers
# a = 5
# b = 10
# a, b = b, a
# print("a =", a)
# print("b =", b)


# 9) Swap Without Third Variable
# a = 3
# b = 7
# a = a + b
# b = a - b
# a = a - b
# print(a, b)


# 10) Find Square
# n = 6
# print(n * n)


# 11) Find Cube
# n = 4
# print(n ** 3)


# 12) Check Even or Odd
# n = 7
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# 13) Check Positive or Negative
# n = -8
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")



# 14) Find Greatest of Two Numbers
# a = 15
# b = 22
# if a > b:
#     print(a)
# else:
#     print(b)


# 15) Find Greatest of Three Numbers
# a = 12
# b = 45
# c = 30
# if a > b and a > c:
#     print(a)
# elif b > c:
#     print(b)
# else:
#     print(c)


# 16) Check Divisible by 5
# n = 25
# if n % 5 == 0:
#     print("Divisible")
# else:
#     print("Not Divisible")


# 17) Check Leap Year
# year = 2024
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not Leap Year")


# 18) Print Numbers 1 to 10
# for i in range(1, 11):
#     print(i)


# 19) Print Numbers 10 to 1
# for i in range(10, 0, -1):
#     print(i)


# 20) Sum of First 10 Natural Numbers
# total = 0
# for i in range(1, 11):
#     total += i
# print(total)
"""        """

# 21) Sum of N Natural Numbers
# n = 5
# total = 0
# for i in range(1, n + 1):
#     total += i
# print(total)


# 22) Find Factorial
# n = 5
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)


# 23) Print Multiplication Table
# n = 3
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


# 24) Count Digits in a Number
# n = 12345
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print(count)


# 25) Reverse a Number
# n = 1234
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 1
# print(rev)


# 26) Check Palindrome Number
# n = 121
# temp = n
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10
# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 27) Check Armstrong Number
# n = 153
# temp = n
# sum_val = 0
# while n > 0:
#     digit = n % 10
#     sum_val += digit ** 3
#     n //= 10
# if temp == sum_val:
#     print("Armstrong")
# else:
#     print("Not Armstrong")



# 28) Check Prime Number
# n = 13
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print("Prime")
# else:
#     print("Not Prime")



# 29) Print Prime Numbers from 1 to 20
# for n in range(2, 21):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         print(n)


# 30) Fibonacci Series
# a = 0
# b = 1
# for i in range(10):
#     print(a)
#     a, b = b, a + b

"""   """
# 31) Find Sum of Digits
# n = 1234
# sum_val = 0
# while n > 0:
#     digit = n % 10
#     sum_val += digit
#     n //= 10
# print(sum_val)


# 32) Product of Digits
# n = 123
# product = 1
# while n > 0:
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)


# 33) Check Perfect Number
# n = 6
# sum_val = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum_val += i
# if sum_val == n:
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")



# 34) Print ASCII Value
# ch = 'A'
# print(ord(ch))


# 35) Convert ASCII to Character
# n = 66
# print(chr(n))


# 36) Reverse a String
# s = "python"
# print(s[::-1])


# 37) Check Palindrome String
# s = "madam"
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")



# 38) Count Vowels in String
# s = "education"
# count = 0
# for ch in s:
#     if ch in "aeiouAEIOU":
#         count += 1
# print(count)


# 39) Count Consonants
# s = "python"
# count = 0
# for ch in s:
#     if ch.isalpha() and ch not in "aeiouAEIOU":
#         count += 1
# print(count)


# 40) Count Spaces
# s = "I love python"
# count = 0
# for ch in s:
#     if ch == " ":
#         count += 1
# print(count)


"""     """
# 41) Convert String to Uppercase
# s = "python"
# print(s.upper())


# 42) Convert String to Lowercase
# s = "PYTHON"
# print(s.lower())


# 43) Remove Spaces from String
# s = "i love python"
# print(s.replace(" ", ""))


# 44) Count Frequency of Character
# s = "banana"
# ch = "a"
# count = 0
# for i in s:
#     if i == ch:
#         count += 1
# print(count)



# 45) First Character of String
# s = "Python"
# print(s[0])


# 46) Last Character of String
# s = "Python"
# print(s[-1])



# 47) Find Length of String
# s = "Interview"
# print(len(s))


# 48) Check Anagram
# s1 = "listen"
# s2 = "silent"
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")



# 49) Replace Word in String
# s = "I like Java"
# print(s.replace("Java", "Python"))


# 50) Split String
# s = "python is easy"
# print(s.split())


"""             """ 
# 51) Join List into String
# words = ["I", "love", "Python"]
# print(" ".join(words))


# 52) Count Words in Strings 
# s = "I love learning python"
# words = s.split()
# print(len(words))


# 53) Find Largest Word
# s = "I love programming in python"
# words = s.split()
# largest = words[0]
# for word in words:
#     if len(word) > len(largest):
#         largest = word
# print(largest)



# 54) Capitalize First Letter
# s = "python"
# print(s.capitalize())



# 55) Title Case String
# s = "i love python"
# print(s.title())



# 56) Create a List
# numbers = [10, 20, 30, 40]
# print(numbers)



# 57) Access First Element of List
# numbers = [5, 10, 15]
# print(numbers[0])



# 58) Access Last Element of List
# numbers = [5, 10, 15]
# print(numbers[-1])


# 59) Add Element to List
# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)



# 60) Insert Element in List
# numbers = [1, 2, 4]
# numbers.insert(2, 3)
# print(numbers)


"""         """
# 61) Remove Element from List
# numbers = [1, 2, 3, 4]
# numbers.remove(3)
# print(numbers)



# 62) Pop Last Element
# numbers = [1, 2, 3]
# numbers.pop()
# print(numbers)



# 63) Find Maximum in List
# numbers = [10, 5, 30, 20]
# print(max(numbers))


# 64) Find Minimum in List
# numbers = [10, 5, 30, 20]
# print(min(numbers))



# 65) Sum of List Elements
# numbers = [1, 2, 3, 4]
# print(sum(numbers))


# 66) Find Average of List
# numbers = [10, 20, 30, 40]
# avg = sum(numbers) / len(numbers)
# print(avg)


# 67) Reverse a List
# numbers = [1, 2, 3, 4]
# print(numbers[::-1])


# 68) Sort a List Ascending
# numbers = [4, 1, 3, 2]
# numbers.sort()
# print(numbers)



# 69) Sort a List Descending
# numbers = [4, 1, 3, 2]
# numbers.sort(reverse=True)
# print(numbers)



# 70) Find Second Largest Number
# numbers = [10, 50, 30, 40]
# numbers.sort()
# print(numbers[-2])


"""          """
# 71) Remove Duplicates from List
# numbers = [1, 2, 2, 3, 4, 4]
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(unique)



# 72) Count Occurrences in List
# numbers = [1, 2, 2, 3, 2]
# print(numbers.count(2))



# 73) Merge Two Lists
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)



# 74) Find Common Elements
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# common = []
# for num in a:
#     if num in b:
#         common.append(num)
# print(common)



# 75) Check Element Exists in List
# numbers = [10, 20, 30]
# if 20 in numbers:
#     print("Found")
# else:
#     print("Not Found")



# 76) Find Index of Element
# numbers = [10, 20, 30]
# print(numbers.index(20))



# 77) Create Tuple
# t = (10, 20, 30)
# print(t)



# 78) Access Tuple Element
# t = (5, 10, 15)
# print(t[1])



# 79) Count Element in Tuple
# t = (1, 2, 2, 3)
# print(t.count(2))



# 80) Find Length of Tuple
# t = (1, 2, 3, 4, 5)
# print(len(t))


"""                 """
# 81) Create Dictionary
# student = {"name": "Prince", "age": 21}
# print(student)



# 82) Access Dictionary Value
# student = {"name": "Prince", "age": 21}
# print(student["name"])



# 83) Add Key-Value in Dictionary
# student = {"name": "Prince"}
# student["age"] = 21
# print(student)



# 84) Remove Key from Dictionary
# student = {"name": "Prince", "age": 21}
# del student["age"]
# print(student)



# 85) Print Dictionary Keys
# student = {"name": "Prince", "age": 21}
# print(student.keys())



# 86) Print Dictionary Values
# student = {"name": "Prince", "age": 21}
# print(student.values())



# 87) Loop Through Dictionary
# student = {"name": "Prince", "age": 21}
# for key, value in student.items():
#     print(key, value)



# 88) Count Character Frequency Using Dictionary
# s = "banana"
# freq = {}

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq)



# 89) Count Word Frequency
# s = "python is easy python is powerful"
# words = s.split()
# freq = {}

# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# print(freq)



# 90) Create Set
# s = {1, 2, 3, 4}
# print(s)


"""        """
# 91) Add Element to Set
# s = {1, 2, 3}
# s.add(4)
# print(s)



# 92) Remove Element from Set
# s = {1, 2, 3, 4}
# s.remove(3)
# print(s)



# 93) Union of Two Sets
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)



# 94) Intersection of Two Sets
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a & b)



# 95) Difference of Two Sets
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a - b)



# 96) Create a Function
# def greet():
#     print("Hello Python")
# greet()



# 97) Function with Parameters
# def add(a, b):
#     print(a + b)
# add(10, 20)



# 98) Function with Return Value
# def square(n):
#     return n * n
# print(square(6))



# 99) Recursive Factorial
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))



# 100) Lambda Function
# square = lambda x: x * x
# print(square(7))



# ✅ Tumne abhi kya cover kiya?
# In 100 problems me tumne ye topics cover kar liye:
# Variables
# Operators
# If-Else
# Loops
# Number Programs
# String Programs
# List Programs
# Tuple
# Dictionary
# Set
# Functions
# Recursion
# Lambda
# Ye fresher Python interview ke liye bahut strong base hai.
# 🎯 Best Next Step








# 101) Reverse a String Without Slicing
# s = "python"
# rev = "
# for ch in s:
#     rev = ch + rev
# print(rev)


# nohtyp
# 102) Find Maximum Without max()

# numbers = [10, 45, 7, 99, 23]
# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print(largest)
# Output:

# 99
# 103) Find Minimum Without min()

# numbers = [10, 45, 7, 99, 23]
# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# print(smallest)
# Output:

# 7
# 104) Sum List Without sum()

# numbers = [1, 2, 3, 4, 5]
# total = 0

# for num in numbers:
#     total += num

# print(total)
# Output:

# 15
# 105) Average Without sum()

# numbers = [10, 20, 30, 40]
# total = 0

# for num in numbers:
#     total += num

# avg = total / len(numbers)
# print(avg)
# Output:

# 25.0
# 106) Manual Count of String Length
# Python
# s = "interview"
# count = 0

# for ch in s:
#     count += 1

# print(count)
# Output:
# Python
# 9
# 107) Count Uppercase Letters
# Python
# s = "PyThOn"
# count = 0

# for ch in s:
#     if ch.isupper():
#         count += 1

# print(count)
# Output:
# Python
# 3
# 108) Count Lowercase Letters
# Python
# s = "PyThOn"
# count = 0

# for ch in s:
#     if ch.islower():
#         count += 1

# print(count)
# Output:
# Python
# 3
# 109) Count Digits in String
# Python
# s = "abc123xyz45"
# count = 0

# for ch in s:
#     if ch.isdigit():
#         count += 1

# print(count)
# Output:
# Python
# 5
# 110) Count Alphabets in String
# Python
# s = "abc123xyz45"
# count = 0

# for ch in s:
#     if ch.isalpha():
#         count += 1

# print(count)
# Output:
# Python
# 6
# 111) Remove All Digits From String
# Python
# s = "py3th0n123"
# result = ""

# for ch in s:
#     if not ch.isdigit():
#         result += ch

# print(result)
# Output:
# Python
# python
# 112) Remove All Alphabets From String
# Python
# s = "py3th0n123"
# result = ""

# for ch in s:
#     if not ch.isalpha():
#         result += ch

# print(result)
# Output:
# Python
# 30123
# 113) Print Each Character on New Line
# Python
# s = "python"

# for ch in s:
#     print(ch)
# Output:
# Python
# p
# y
# t
# h
# o
# n
# 114) Count Occurrence of Each Character
# Python
# s = "apple"

# for ch in s:
#     print(ch, "=", s.count(ch))
# Output:
# Python
# a = 1
# p = 2
# p = 2
# l = 1
# e = 1
# 115) First Non-Repeating Character
# Python
# s = "aabbcde"

# for ch in s:
#     if s.count(ch) == 1:
#         print(ch)
#         break
# Output:
# Python
# c
# 116) First Repeating Character
# Python
# s = "abccde"
# seen = ""

# for ch in s:
#     if ch in seen:
#         print(ch)
#         break
#     seen += ch
# Output:
# Python
# c
# 117) Remove Duplicate Characters From String
# Python
# s = "programming"
# result = ""

# for ch in s:
#     if ch not in result:
#         result += ch

# print(result)
# Output:
# Python
# progamin
# 118) Check String Starts With Vowel
# Python
# s = "apple"

# if s[0].lower() in "aeiou":
#     print("Starts with vowel")
# else:
#     print("Does not start with vowel")
# Output:
# Python
# Starts with vowel
# 119) Check String Ends With Digit
# Python
# s = "python9"

# if s[-1].isdigit():
#     print("Ends with digit")
# else:
#     print("Does not end with digit")
# Output:
# Python
# Ends with digit
# 120) Count Special Characters
# Python
# s = "py@th#on!123"
# count = 0

# for ch in s:
#     if not ch.isalnum():
#         count += 1

# print(count)
# Output:
# Python
# 3
# 121) Reverse Words in Sentence
# Python
# s = "I love python"
# words = s.split()
# rev_words = words[::-1]

# print(" ".join(rev_words))
# Output:
# Python
# python love I
# 122) Reverse Each Word in Sentence
# Python
# s = "I love python"
# words = s.split()
# result = []

# for word in words:
#     result.append(word[::-1])

# print(" ".join(result))
# Output:
# Python
# I evol nohtyp
# 123) Find Smallest Word in Sentence
# Python
# s = "I love programming in python"
# words = s.split()
# smallest = words[0]

# for word in words:
#     if len(word) < len(smallest):
#         smallest = word

# print(smallest)
# Output:
# Python
# I
# 124) Count Number of Words Starting With Vowel
# Python
# s = "apple is orange and umbrella"
# words = s.split()
# count = 0

# for word in words:
#     if word[0].lower() in "aeiou":
#         count += 1

# print(count)
# Output:
# Python
# 5
# 125) Check If Two Strings Are Rotations
# Python
# s1 = "abcd"
# s2 = "cdab"

# if len(s1) == len(s2) and s2 in (s1 + s1):
#     print("Rotation")
# else:
#     print("Not Rotation")
# Output:
# Python
# Rotation
# 126) Manual List Reverse Without [::-1]
# Python
# numbers = [1, 2, 3, 4]
# rev = []

# for i in range(len(numbers)-1, -1, -1):
#     rev.append(numbers[i])

# print(rev)
# Output:
# Python
# [4, 3, 2, 1]
# 127) Manual Sort Ascending (Bubble Sort)
# Python
# numbers = [5, 2, 8, 1, 3]

# for i in range(len(numbers)):
#     for j in range(len(numbers)-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# print(numbers)
# Output:
# Python
# [1, 2, 3, 5, 8]
# 128) Manual Sort Descending
# Python
# numbers = [5, 2, 8, 1, 3]

# for i in range(len(numbers)):
#     for j in range(len(numbers)-1):
#         if numbers[j] < numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# print(numbers)
# Output:
# Python
# [8, 5, 3, 2, 1]
# 129) Find Second Smallest Number
# Python
# numbers = [10, 5, 8, 2, 15]
# numbers.sort()
# print(numbers[1])
# Output:
# Python
# 5
# 130) Find Third Largest Number
# Python
# numbers = [10, 50, 20, 80, 40]
# numbers.sort(reverse=True)
# print(numbers[2])
# Output:
# Python
# 40
# 131) Check If List Is Sorted
# Python
# numbers = [1, 2, 3, 4]
# is_sorted = True

# for i in range(len(numbers)-1):
#     if numbers[i] > numbers[i+1]:
#         is_sorted = False
#         break

# print(is_sorted)
# Output:
# Python
# True
# 132) Move All Zeros to End
# Python
# numbers = [1, 0, 2, 0, 3, 4, 0]
# result = []

# for num in numbers:
#     if num != 0:
#         result.append(num)

# for num in numbers:
#     if num == 0:
#         result.append(num)

# print(result)
# Output:
# Python
# [1, 2, 3, 4, 0, 0, 0]
# 133) Move All Even Numbers First
# Python
# numbers = [1, 2, 3, 4, 5, 6]
# result = []

# for num in numbers:
#     if num % 2 == 0:
#         result.append(num)

# for num in numbers:
#     if num % 2 != 0:
#         result.append(num)

# print(result)
# Output:
# Python
# [2, 4, 6, 1, 3, 5]
# 134) Find Missing Number in 1 to N
# Python
# numbers = [1, 2, 3, 5]
# n = 5
# expected = n * (n + 1) // 2
# actual = 0

# for num in numbers:
#     actual += num

# print(expected - actual)
# Output:
# Python
# 4
# 135) Find Duplicate Number in List
# Python
# numbers = [1, 2, 3, 4, 2, 5]
# seen = []

# for num in numbers:
#     if num in seen:
#         print(num)
#         break
#     seen.append(num)
# Output:
# Python
# 2
# 136) Print All Duplicate Elements
# Python
# numbers = [1, 2, 3, 2, 4, 5, 1]
# duplicates = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print(duplicates)
# Output:
# Python
# [1, 2]
# 137) Find Unique Elements Only
# Python
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique = []

# for num in numbers:
#     if numbers.count(num) == 1:
#         unique.append(num)

# print(unique)
# Output:
# Python
# [1, 3, 5]
# 138) Separate Positive and Negative Numbers
# Python
# numbers = [2, -3, 5, -1, 0, 7, -6]
# positive = []
# negative = []

# for num in numbers:
#     if num >= 0:
#         positive.append(num)
#     else:
#         negative.append(num)

# print("Positive:", positive)
# print("Negative:", negative)
# Output:
# Python
# Positive: [2, 5, 0, 7]
# Negative: [-3, -1, -6]
# 139) Find Pair With Given Sum
# Python
# numbers = [2, 4, 3, 5, 7]
# target = 9

# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], numbers[j])
#             break
# Output:
# Python
# 2 7
# 4 5
# 140) Rotate List Left by 1
# Python
# numbers = [1, 2, 3, 4, 5]
# rotated = numbers[1:] + [numbers[0]]
# print(rotated)
# Output:
# Python
# [2, 3, 4, 5, 1]
# 141) Rotate List Right by 1
# Python
# numbers = [1, 2, 3, 4, 5]
# rotated = [numbers[-1]] + numbers[:-1]
# print(rotated)
# Output:
# Python
# [5, 1, 2, 3, 4]
# 142) Flatten a 2D List
# Python
# matrix = [[1, 2], [3, 4], [5, 6]]
# flat = []

# for row in matrix:
#     for num in row:
#         flat.append(num)

# print(flat)
# Output:
# Python
# [1, 2, 3, 4, 5, 6]
# 143) Sum of All Elements in 2D List
# Python
# matrix = [[1, 2], [3, 4], [5, 6]]
# total = 0

# for row in matrix:
#     for num in row:
#         total += num

# print(total)
# Output:
# Python
# 21
# 144) Find Largest in 2D List
# Python
# matrix = [[1, 2], [8, 4], [5, 6]]
# largest = matrix[0][0]

# for row in matrix:
#     for num in row:
#         if num > largest:
#             largest = num

# print(largest)
# Output:
# Python
# 8
# 145) Matrix Addition
# Python
# a = [[1, 2], [3, 4]]
# b = [[5, 6], [7, 8]]
# result = []

# for i in range(len(a)):
#     row = []
#     for j in range(len(a[0])):
#         row.append(a[i][j] + b[i][j])
#     result.append(row)

# print(result)
# Output:
# Python
# [[6, 8], [10, 12]]
# 146) Matrix Subtraction
# Python
# a = [[5, 6], [7, 8]]
# b = [[1, 2], [3, 4]]
# result = []

# for i in range(len(a)):
#     row = []
#     for j in range(len(a[0])):
#         row.append(a[i][j] - b[i][j])
#     result.append(row)

# print(result)
# Output:
# Python
# [[4, 4], [4, 4]]
# 147) Diagonal Sum of Matrix
# Python
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# diag_sum = 0

# for i in range(len(matrix)):
#     diag_sum += matrix[i][i]

# print(diag_sum)
# Output:
# Python
# 15
# 148) Print Main Diagonal Elements
# Python
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# for i in range(len(matrix)):
#     print(matrix[i][i])
# Output:
# Python
# 1
# 5
# 9
# 149) Find Transpose of Matrix
# Python
# matrix = [[1, 2, 3],
#           [4, 5, 6]]

# transpose = []

# for i in range(len(matrix[0])):
#     row = []
#     for j in range(len(matrix)):
#         row.append(matrix[j][i])
#     transpose.append(row)

# print(transpose)
# Output:
# Python
# [[1, 4], [2, 5], [3, 6]]
# 150) Check If Matrix Is Square
# Python
# matrix = [[1, 2], [3, 4]]

# if len(matrix) == len(matrix[0]):
#     print("Square Matrix")
# else:
#     print("Not Square Matrix")
# Output:
# Python
# Square Matrix
# 151) Count Even Numbers in List
# Python
# numbers = [1, 2, 3, 4, 5, 6]
# count = 0

# for num in numbers:
#     if num % 2 == 0:
#         count += 1

# print(count)
# Output:
# Python
# 3
# 152) Count Odd Numbers in List
# Python
# numbers = [1, 2, 3, 4, 5, 6]
# count = 0

# for num in numbers:
#     if num % 2 != 0:
#         count += 1

# print(count)
# Output:
# Python
# 3
# 153) Find All Even Numbers
# Python
# numbers = [1, 2, 3, 4, 5, 6]
# evens = []

# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)

# print(evens)
# Output:
# Python
# [2, 4, 6]
# 154) Find All Odd Numbers
# Python
# numbers = [1, 2, 3, 4, 5, 6]
# odds = []

# for num in numbers:
#     if num % 2 != 0:
#         odds.append(num)

# print(odds)
# Output:
# Python
# [1, 3, 5]
# 155) Count Numbers Greater Than 10
# Python
# numbers = [5, 12, 7, 15, 3, 20]
# count = 0

# for num in numbers:
#     if num > 10:
#         count += 1

# print(count)
# Output:
# Python
# 3
# 156) Multiply All Elements in List
# Python
# numbers = [1, 2, 3, 4]
# product = 1

# for num in numbers:
#     product *= num

# print(product)
# Output:
# Python
# 24
# 157) Find Difference Between Max and Min
# Python
# numbers = [10, 3, 25, 7, 18]
# print(max(numbers) - min(numbers))
# Output:
# Python
# 22
# 158) Print List in Reverse Order Using Loop
# Python
# numbers = [10, 20, 30, 40]

# for i in range(len(numbers)-1, -1, -1):
#     print(numbers[i])
# Output:
# Python
# 40
# 30
# 20
# 10
# 159) Create List of Squares
# Python
# numbers = [1, 2, 3, 4, 5]
# squares = []

# for num in numbers:
#     squares.append(num * num)

# print(squares)
# Output:
# Python
# [1, 4, 9, 16, 25]
# 160) Create List of Cubes
# Python
# numbers = [1, 2, 3, 4]
# cubes = []

# for num in numbers:
#     cubes.append(num ** 3)

# print(cubes)
# Output:
# Python
# [1, 8, 27, 64]
# 161) Convert List of Strings to Uppercase
# Python
# words = ["python", "java", "sql"]
# result = []

# for word in words:
#     result.append(word.upper())

# print(result)
# Output:
# Python
# ['PYTHON', 'JAVA', 'SQL']
# 162) Find Longest String in List
# Python
# words = ["cat", "elephant", "dog", "python"]
# longest = words[0]

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print(longest)
# Output:
# Python
# elephant
# 163) Count Strings Longer Than 5
# Python
# words = ["cat", "elephant", "dog", "python"]
# count = 0

# for word in words:
#     if len(word) > 5:
#         count += 1

# print(count)
# Output:
# Python
# 2
# 164) Find Common Characters in Two Strings
# Python
# s1 = "apple"
# s2 = "grape"
# common = ""

# for ch in s1:
#     if ch in s2 and ch not in common:
#         common += ch

# print(common)
# Output:
# Python
# ape
# 165) Count Matching Characters at Same Position
# Python
# s1 = "python"
# s2 = "pytabc"
# count = 0

# for i in range(len(s1)):
#     if s1[i] == s2[i]:
#         count += 1

# print(count)
# Output:
# Python
# 3
# **166) Replace All Vowels With * **
# Python
# s = "education"
# result = ""

# for ch in s:
#     if ch.lower() in "aeiou":
#         result += "*"
#     else:
#         result += ch

# print(result)
# Output:
# Python
# *d*c*t**n
# 167) Remove Consecutive Duplicate Characters
# Python
# s = "aaabbccdaa"
# result = s[0]

# for i in range(1, len(s)):
#     if s[i] != s[i-1]:
#         result += s[i]

# print(result)
# Output:
# Python
# abcda
# 168) String Compression (Basic)
# Python
# s = "aaabbc"
# result = ""
# count = 1

# for i in range(1, len(s)):
#     if s[i] == s[i-1]:
#         count += 1
#     else:
#         result += s[i-1] + str(count)
#         count = 1

# result += s[-1] + str(count)
# print(result)
# Output:
# Python
# a3b2c1
# 169) Expand Compressed String
# Python
# s = "a3b2c1"
# result = ""

# for i in range(0, len(s), 2):
#     result += s[i] * int(s[i+1])

# print(result)
# Output:
# Python
# aaabbc
# 170) Check Balanced Parentheses (Simple)
# Python
# s = "(()())"
# count = 0
# balanced = True

# for ch in s:
#     if ch == "(":
#         count += 1
#     else:
#         count -= 1
#     if count < 0:
#         balanced = False
#         break

# if count != 0:
#     balanced = False

# print(balanced)
# Output:
# Python
# True
# 171) Find Number of Pairs in List
# Python
# numbers = [1, 2, 2, 3, 3, 3, 4, 4]
# pairs = 0
# checked = []

# for num in numbers:
#     if num not in checked:
#         pairs += numbers.count(num) // 2
#         checked.append(num)

# print(pairs)
# Output:
# Python
# 3
# 172) Check If All Elements Are Same
# Python
# numbers = [5, 5, 5, 5]
# same = True

# for num in numbers:
#     if num != numbers[0]:
#         same = False
#         break

# print(same)
# Output:
# Python
# True
# 173) Find Majority Element
# Python
# numbers = [2, 2, 1, 2, 3, 2, 2]
# majority = None

# for num in numbers:
#     if numbers.count(num) > len(numbers) // 2:
#         majority = num
#         break

# print(majority)
# Output:
# Python
# 2
# 174) Count Frequency of List Elements
# Python
# numbers = [1, 2, 2, 3, 1, 4, 2]
# freq = {}

# for num in numbers:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# print(freq)
# Output:
# Python
# {1: 2, 2: 3, 3: 1, 4: 1}
# 175) Find Least Frequent Element
# Python
# numbers = [1, 2, 2, 3, 3, 3, 4]
# least = numbers[0]

# for num in numbers:
#     if numbers.count(num) < numbers.count(least):
#         least = num

# print(least)
# Output:
# Python
# 1
# 176) Find Most Frequent Element
# Python
# numbers = [1, 2, 2, 3, 3, 3, 4]
# most = numbers[0]

# for num in numbers:
#     if numbers.count(num) > numbers.count(most):
#         most = num

# print(most)
# Output:
# Python
# 3
# 177) Convert Decimal to Binary
# Python
# n = 10
# binary = ""

# while n > 0:
#     binary = str(n % 2) + binary
#     n //= 2

# print(binary)
# Output:
# Python
# 1010
# 178) Convert Binary to Decimal
# Python
# binary = "1010"
# decimal = 0
# power = 0

# for i in range(len(binary)-1, -1, -1):
#     decimal += int(binary[i]) * (2 ** power)
#     power += 1

# print(decimal)
# Output:
# Python
# 10
# 179) Check If Number Is Power of 2
# Python
# n = 16

# while n % 2 == 0 and n > 1:
#     n //= 2

# if n == 1:
#     print("Power of 2")
# else:
#     print("Not Power of 2")
# Output:
# Python
# Power of 2
# 180) Find GCD of Two Numbers
# Python
# a = 24
# b = 36

# while b != 0:
#     a, b = b, a % b

# print(a)
# Output:
# Python
# 12
# 181) Find LCM of Two Numbers
# Python
# a = 12
# b = 18
# x = a
# y = b

# while b != 0:
#     a, b = b, a % b

# gcd = a
# lcm = (x * y) // gcd
# print(lcm)
# Output:
# Python
# 36
# 182) Check Co-Prime Numbers
# Python
# a = 8
# b = 15

# x = a
# y = b

# while y != 0:
#     x, y = y, x % y

# if x == 1:
#     print("Co-prime")
# else:
#     print("Not Co-prime")
# Output:
# Python
# Co-prime
# 183) Find Factors of a Number
# Python
# n = 12

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)
# Output:
# Python
# 1
# 2
# 3
# 4
# 6
# 12
# 184) Count Factors of a Number
# Python
# n = 12
# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1

# print(count)
# Output:
# Python
# 6
# 185) Check Harshad Number
# Python
# n = 18
# temp = n
# digit_sum = 0

# while temp > 0:
#     digit_sum += temp % 10
#     temp //= 10

# if n % digit_sum == 0:
#     print("Harshad Number")
# else:
#     print("Not Harshad Number")
# Output:
# Python
# Harshad Number
# 186) Find Power Without pow()
# Python
# base = 2
# exp = 5
# result = 1

# for i in range(exp):
#     result *= base

# print(result)
# Output:
# Python
# 32
# 187) Count Trailing Zeros in Number
# Python
# n = 12000
# count = 0

# while n % 10 == 0:
#     count += 1
#     n //= 10

# print(count)
# Output:
# Python
# 3
# 188) Find Largest Digit in Number
# Python
# n = 58329
# largest = 0

# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         largest = digit
#     n //= 10

# print(largest)
# Output:
# Python
# 9
# 189) Find Smallest Digit in Number
# Python
# n = 58329
# smallest = 9

# while n > 0:
#     digit = n % 10
#     if digit < smallest:
#         smallest = digit
#     n //= 10

# print(smallest)
# Output:
# Python
# 2
# 190) Check Duck Number
# Python
# n = "1023"

# if "0" in n[1:]:
#     print("Duck Number")
# else:
#     print("Not Duck Number")
# Output:
# Python
# Duck Number
# 191) Check Spy Number
# Python
# n = 123
# sum_val = 0
# product = 1

# while n > 0:
#     digit = n % 10
#     sum_val += digit
#     product *= digit
#     n //= 10

# if sum_val == product:
#     print("Spy Number")
# else:
#     print("Not Spy Number")
# Output:
# Python
# Spy Number
# 192) Check Neon Number
# Python
# n = 9
# square = n * n
# digit_sum = 0

# while square > 0:
#     digit_sum += square % 10
#     square //= 10

# if digit_sum == n:
#     print("Neon Number")
# else:
#     print("Not Neon Number")
# Output:
# Python
# Neon Number
# 193) Check Automorphic Number
# Python
# n = 25
# square = n * n

# if str(square).endswith(str(n)):
#     print("Automorphic")
# else:
#     print("Not Automorphic")
# Output:
# Python
# Automorphic
# 194) Check Sunny Number
# Python
# n = 8
# root = int((n + 1) ** 0.5)

# if root * root == n + 1:
#     print("Sunny Number")
# else:
#     print("Not Sunny Number")
# Output:
# Python
# Sunny Number
# 195) Check Disarium Number
# Python
# n = 135
# temp = str(n)
# sum_val = 0

# for i in range(len(temp)):
#     sum_val += int(temp[i]) ** (i + 1)

# if sum_val == n:
#     print("Disarium Number")
# else:
#     print("Not Disarium Number")
# Output:
# Python
# Disarium Number
# 196) Check Peterson Number
# Python
# n = 145
# temp = n
# sum_val = 0

# while temp > 0:
#     digit = temp % 10
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
#     sum_val += fact
#     temp //= 10

# if sum_val == n:
#     print("Peterson Number")
# else:
#     print("Not Peterson Number")
# Output:
# Python
# Peterson Number
# 197) Find Sum of Even Digits
# Python
# n = 123456
# sum_even = 0

# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:
#         sum_even += digit
#     n //= 10

# print(sum_even)
# Output:
# Python
# 12
# 198) Find Sum of Odd Digits
# Python
# n = 123456
# sum_odd = 0

# while n > 0:
#     digit = n % 10
#     if digit % 2 != 0:
#         sum_odd += digit
#     n //= 10

# print(sum_odd)
# Output:
# Python
# 9
# 199) Interchange First and Last Digit
# Python
# n = "12345"
# result = n[-1] + n[1:-1] + n[0]
# print(result)
# Output:
# Python
# 52341
# 200) Check If Number Contains Digit 7
# Python
# n = 17245

# if "7" in str(n):
#     print("Contains 7")
# else:
#     print("Does not contain 7")
# Output:
# Python
# Contains 7
# ✅ Ab tumhare paas 1 to 200 ho gaye
# Tumne ab tak cover kar liya:
# Basic Python
# Conditions
# Loops
# Strings
# Lists
# Tuples
# Dictionaries
# Sets
# Functions
# Recursion
# Number Logic
# Matrix Basics
# Interview Logic Questions
# Manual Operations
# Real fresher-level coding patterns
# 🎯 Honest Interview Verdict
# Agar tum 1 to 200 ko:
# khud likh sakte ho,
# explain kar sakte ho,
# thoda modify kar sakte ho,
# to tum fresher Python interview me kaafi strong ho.
# Lekin ab jo next level hai 201 to 300, wahi tumhe “average candidate” se “selected candidate” bana sakta hai.
# Usme aayega:
# harder string logic
# nested list logic
# tricky interview questions
# function-based coding
# manual built-ins
# mini problem-solving patterns
# Agar

 







# Bilkul — ab 201 to 300 me main fresher interview ke liye important topics ko maximum cover karunga.
# Focus rahega:
# Core Python only
# No libraries
# Interview-important
# Unique
# Code + Output
# Non-stop
# ⚠️ Note: Kuch questions 200 ke aas-paas wale concepts ka next-level interview version honge — ye intentional hai, kyunki interview me wahi twist karke poocha jata hai.
# 201) Find Largest Number Without Using sort()
# Python
# numbers = [12, 45, 7, 89, 23]
# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print(largest)
# Output:
# Python
# 89
# 202) Find Smallest Number Without Using sort()
# Python
# numbers = [12, 45, 7, 89, 23]
# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# print(smallest)
# Output:
# Python
# 7
# 203) Find Second Largest Without sort()
# Python
# numbers = [10, 50, 20, 80, 40]
# largest = second = float('-inf')

# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num

# print(second)
# Output:
# Python
# 50
# 204) Find Second Smallest Without sort()
# Python
# numbers = [10, 50, 20, 80, 40]
# smallest = second = float('inf')

# for num in numbers:
#     if num < smallest:
#         second = smallest
#         smallest = num
#     elif num < second and num != smallest:
#         second = num

# print(second)
# Output:
# Python
# 20
# 205) Find Third Largest Without sort()
# Python
# numbers = [10, 50, 20, 80, 40]
# first = second = third = float('-inf')

# for num in numbers:
#     if num > first:
#         third = second
#         second = first
#         first = num
#     elif num > second and num != first:
#         third = second
#         second = num
#     elif num > third and num != second and num != first:
#         third = num

# print(third)
# Output:
# Python
# 40
# 206) Manual List Copy
# Python
# numbers = [1, 2, 3, 4]
# copied = []

# for num in numbers:
#     copied.append(num)

# print(copied)
# Output:
# Python
# [1, 2, 3, 4]
# 207) Manual List Concatenation
# Python
# a = [1, 2, 3]
# b = [4, 5, 6]
# result = []

# for num in a:
#     result.append(num)

# for num in b:
#     result.append(num)

# print(result)
# Output:
# Python
# [1, 2, 3, 4, 5, 6]
# 208) Find Intersection Without Set
# Python
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# result = []

# for num in a:
#     if num in b and num not in result:
#         result.append(num)

# print(result)
# Output:
# Python
# [3, 4]
# 209) Find Union Without Set
# Python
# a = [1, 2, 3]
# b = [3, 4, 5]
# result = []

# for num in a:
#     if num not in result:
#         result.append(num)

# for num in b:
#     if num not in result:
#         result.append(num)

# print(result)
# Output:
# Python
# [1, 2, 3, 4, 5]
# 210) Find Difference of Two Lists
# Python
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# result = []

# for num in a:
#     if num not in b:
#         result.append(num)

# print(result)
# Output:
# Python
# [1, 2]
# 211) Check If Two Lists Are Equal
# Python
# a = [1, 2, 3]
# b = [1, 2, 3]

# if a == b:
#     print("Equal")
# else:
#     print("Not Equal")
# Output:
# Python
# Equal
# 212) Find Common Elements Count
# Python
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# count = 0

# for num in a:
#     if num in b:
#         count += 1

# print(count)
# Output:
# Python
# 2
# 213) Remove Element by Index
# Python
# numbers = [10, 20, 30, 40]
# index = 2
# result = []

# for i in range(len(numbers)):
#     if i != index:
#         result.append(numbers[i])

# print(result)
# Output:
# Python
# [10, 20, 40]
# 214) Insert Element at Specific Position Manually
# Python
# numbers = [10, 20, 40, 50]
# pos = 2
# value = 30
# result = []

# for i in range(len(numbers)):
#     if i == pos:
#         result.append(value)
#     result.append(numbers[i])

# print(result)
# Output:
# Python
# [10, 20, 30, 40, 50]
# 215) Split List into Even and Odd Lists
# Python
# numbers = [1, 2, 3, 4, 5, 6]
# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even:", even)
# print("Odd:", odd)
# Output:
# Python
# Even: [2, 4, 6]
# Odd: [1, 3, 5]
# 216) Find Sum of Even Numbers in List
# Python
# numbers = [1, 2, 3, 4, 5, 6]
# total = 0

# for num in numbers:
#     if num % 2 == 0:
#         total += num

# print(total)
# Output:
# Python
# 12
# 217) Find Sum of Odd Numbers in List
# Python
# numbers = [1, 2, 3, 4, 5, 6]
# total = 0

# for num in numbers:
#     if num % 2 != 0:
#         total += num

# print(total)
# Output:
# Python
# 9
# 218) Find Product of Even Numbers
# Python
# numbers = [1, 2, 3, 4, 5]
# product = 1

# for num in numbers:
#     if num % 2 == 0:
#         product *= num

# print(product)
# Output:
# Python
# 8
# 219) Find Product of Odd Numbers
# Python
# numbers = [1, 2, 3, 4, 5]
# product = 1

# for num in numbers:
#     if num % 2 != 0:
#         product *= num

# print(product)
# Output:
# Python
# 15
# 220) Reverse Only Even Numbers in List
# Python
# numbers = [1, 2, 3, 4, 5, 6]
# evens = []

# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)

# evens = evens[::-1]
# result = []
# j = 0

# for num in numbers:
#     if num % 2 == 0:
#         result.append(evens[j])
#         j += 1
#     else:
#         result.append(num)

# print(result)
# Output:
# Python
# [1, 6, 3, 4, 5, 2]
# 221) Count Duplicate Elements in List
# Python
# numbers = [1, 2, 2, 3, 3, 3, 4]
# count = 0
# seen = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in seen:
#         count += 1
#         seen.append(num)

# print(count)
# Output:
# Python
# 2
# 222) Find First Duplicate Element
# Python
# numbers = [1, 2, 3, 2, 4, 5]
# seen = []

# for num in numbers:
#     if num in seen:
#         print(num)
#         break
#     seen.append(num)
# Output:
# Python
# 2
# 223) Find Last Duplicate Element
# Python
# numbers = [1, 2, 3, 2, 4, 5, 1]
# last = None

# for num in numbers:
#     if numbers.count(num) > 1:
#         last = num

# print(last)
# Output:
# Python
# 1
# 224) Find First Unique Element
# Python
# numbers = [2, 2, 3, 4, 4, 5]
# for num in numbers:
#     if numbers.count(num) == 1:
#         print(num)
#         break
# Output:
# Python
# 3
# 225) Find Last Unique Element
# Python
# numbers = [2, 2, 3, 4, 4, 5]
# last = None

# for num in numbers:
#     if numbers.count(num) == 1:
#         last = num

# print(last)
# Output:
# Python
# 5
# 226) Remove All Occurrences of an Element
# Python
# numbers = [1, 2, 3, 2, 4, 2, 5]
# target = 2
# result = []

# for num in numbers:
#     if num != target:
#         result.append(num)

# print(result)
# Output:
# Python
# [1, 3, 4, 5]
# 227) Replace All Occurrences of an Element
# Python
# numbers = [1, 2, 3, 2, 4, 2]
# result = []

# for num in numbers:
#     if num == 2:
#         result.append(99)
#     else:
#         result.append(num)

# print(result)
# Output:
# Python
# [1, 99, 3, 99, 4, 99]
# 228) Count Frequency Without Dictionary
# Python
# numbers = [1, 2, 2, 3, 1]
# printed = []

# for num in numbers:
#     if num not in printed:
#         print(num, "=", numbers.count(num))
#         printed.append(num)
# Output:
# Python
# 1 = 2
# 2 = 2
# 3 = 1
# 229) Manual Remove Duplicates Preserving Order
# Python
# numbers = [4, 2, 4, 1, 2, 3]
# result = []

# for num in numbers:
#     if num not in result:
#         result.append(num)

# print(result)
# Output:
# Python
# [4, 2, 1, 3]
# 230) Find Element Appearing Only Once
# Python
# numbers = [4, 1, 2, 1, 2]
# for num in numbers:
#     if numbers.count(num) == 1:
#         print(num)
#         break
# Output:
# Python
# 4
# 231) Manual String Copy
# Python
# s = "python"
# copied = ""

# for ch in s:
#     copied += ch

# print(copied)
# Output:
# Python
# python
# 232) Manual String Concatenation
# Python
# s1 = "Hello"
# s2 = "World"
# result = ""

# for ch in s1:
#     result += ch

# result += " "

# for ch in s2:
#     result += ch

# print(result)
# Output:
# Python
# Hello World
# 233) Find Middle Character of String
# Python
# s = "python"
# mid = len(s) // 2
# print(s[mid])
# Output:
# Python
# h
# 234) Find Middle Two Characters (Even Length)
# Python
# s = "python"
# mid = len(s) // 2
# print(s[mid-1:mid+1])
# Output:
# Python
# th
# 235) Remove First Character From String
# Python
# s = "python"
# print(s[1:])
# Output:
# Python
# ython
# 236) Remove Last Character From String
# Python
# s = "python"
# print(s[:-1])
# Output:
# Python
# pytho
# 237) Remove First and Last Character
# Python
# s = "python"
# print(s[1:-1])
# Output:
# Python
# ytho
# 238) Swap First and Last Character of String
# Python
# s = "python"
# result = s[-1] + s[1:-1] + s[0]
# print(result)
# Output:
# Python
# nythop
# 239) Count Words Without split()
# Python
# s = "I love python programming"
# count = 1

# for ch in s:
#     if ch == " ":
#         count += 1

# print(count)
# Output:
# Python
# 4
# 240) Manual Split Without split()
# Python
# s = "I love python"
# word = ""
# result = []

# for ch in s:
#     if ch != " ":
#         word += ch
#     else:
#         result.append(word)
#         word = ""

# result.append(word)
# print(result)
# Output:
# Python
# ['I', 'love', 'python']
# 241) Manual Join Without join()
# Python
# words = ["I", "love", "python"]
# result = ""

# for i in range(len(words)):
#     result += words[i]
#     if i != len(words) - 1:
#         result += " "

# print(result)
# Output:
# Python
# I love python
# 242) Remove Extra Spaces
# Python
# s = "I   love    python"
# words = s.split()
# print(" ".join(words))
# Output:
# Python
# I love python
# 243) Count Occurrence of Each Word
# Python
# s = "python is easy python is fun"
# words = s.split()
# printed = []

# for word in words:
#     if word not in printed:
#         print(word, "=", words.count(word))
#         printed.append(word)
# Output:
# Python
# python = 2
# is = 2
# easy = 1
# fun = 1
# 244) Find Longest Word Without max()
# Python
# s = "python is very powerful language"
# words = s.split()
# longest = words[0]

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print(longest)
# Output:
# Python
# powerful
# 245) Find Shortest Word Without min()
# Python
# s = "python is very powerful language"
# words = s.split()
# shortest = words[0]

# for word in words:
#     if len(word) < len(shortest):
#         shortest = word

# print(shortest)
# Output:
# Python
# is
# 246) Reverse Sentence Without Reversing Words
# Python
# s = "python is easy"
# result = ""

# for i in range(len(s)-1, -1, -1):
#     result += s[i]

# print(result)
# Output:
# Python
# ysae si nohtyp
# 247) Find Number of Lines in Multi-line String
# Python
# s = "Python\nJava\nSQL"
# count = 1

# for ch in s:
#     if ch == "\n":
#         count += 1

# print(count)
# Output:
# Python
# 3
# 248) Toggle Case Manually
# Python
# s = "PyThOn"
# result = ""

# for ch in s:
#     if ch.isupper():
#         result += ch.lower()
#     else:
#         result += ch.upper()

# print(result)
# Output:
# Python
# pYtHoN
# 249) Check Pangram
# Python
# s = "the quick brown fox jumps over the lazy dog"
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# is_pangram = True

# for ch in alphabet:
#     if ch not in s:
#         is_pangram = False
#         break

# print(is_pangram)
# Output:
# Python
# True
# 250) Find Duplicate Characters in String
# Python
# s = "programming"
# duplicates = ""

# for ch in s:
#     if s.count(ch) > 1 and ch not in duplicates:
#         duplicates += ch

# print(duplicates)
# Output:
# Python
# rgm
# 251) Find Unique Characters in String
# Python
# s = "programming"
# unique = ""

# for ch in s:
#     if s.count(ch) == 1:
#         unique += ch

# print(unique)
# Output:
# Python
# poain
# 252) Remove Character From String
# Python
# s = "python"
# target = "t"
# result = ""

# for ch in s:
#     if ch != target:
#         result += ch

# print(result)
# Output:
# Python
# pyhon
# 253) Replace Character in String
# Python
# s = "banana"
# result = ""

# for ch in s:
#     if ch == "a":
#         result += "@"
#     else:
#         result += ch

# print(result)
# Output:
# Python
# b@n@n@
# 254) Find Index of Character Without index()
# Python
# s = "python"
# target = "h"

# for i in range(len(s)):
#     if s[i] == target:
#         print(i)
#         break
# Output:
# Python
# 3
# 255) Count Consecutive Vowels
# Python
# s = "beautiful"
# count = 0

# for i in range(len(s)-1):
#     if s[i] in "aeiou" and s[i+1] in "aeiou":
#         count += 1

# print(count)
# Output:
# Python
# 3
# 256) Check If String Contains Only Digits
# Python
# s = "12345"

# if s.isdigit():
#     print("Only Digits")
# else:
#     print("Not Only Digits")
# Output:
# Python
# Only Digits
# 257) Check If String Contains Only Alphabets
# Python
# s = "Python"

# if s.isalpha():
#     print("Only Alphabets")
# else:
#     print("Not Only Alphabets")
# Output:
# Python
# Only Alphabets
# 258) Check If String Contains Only Alphanumeric
# Python
# s = "Python123"

# if s.isalnum():
#     print("Alphanumeric")
# else:
#     print("Not Alphanumeric")
# Output:
# Python
# Alphanumeric
# 259) Find All Indices of a Character
# Python
# s = "banana"
# target = "a"

# for i in range(len(s)):
#     if s[i] == target:
#         print(i)
# Output:
# Python
# 1
# 3
# 5
# 260) Count Substring Occurrence
# Python
# s = "abababa"
# sub = "aba"
# count = 0

# for i in range(len(s) - len(sub) + 1):
#     if s[i:i+len(sub)] == sub:
#         count += 1

# print(count)
# Output:
# Python
# 3
# 261) Check If One String Is Substring of Another
# Python
# s1 = "python programming"
# s2 = "program"

# if s2 in s1:
#     print("Substring Found")
# else:
#     print("Not Found")
# Output:
# Python
# Substring Found
# 262) Manual Startswith
# Python
# s = "python"
# prefix = "py"

# if s[:len(prefix)] == prefix:
#     print("Starts With")
# else:
#     print("Does Not Start With")
# Output:
# Python
# Starts With
# 263) Manual Endswith
# Python
# s = "python"
# suffix = "on"

# if s[-len(suffix):] == suffix:
#     print("Ends With")
# else:
#     print("Does Not End With")
# Output:
# Python
# Ends With
# 264) Reverse Digits of Number as List
# Python
# n = 12345
# digits = []

# while n > 0:
#     digits.append(n % 10)
#     n //= 10

# print(digits)
# Output:
# Python
# [5, 4, 3, 2, 1]
# 265) Convert Number to List of Digits
# Python
# n = 12345
# digits = []

# for ch in str(n):
#     digits.append(int(ch))

# print(digits)
# Output:
# Python
# [1, 2, 3, 4, 5]
# 266) Count Even Digits in Number
# Python
# n = 123456
# count = 0

# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:
#         count += 1
#     n //= 10

# print(count)
# Output:
# Python
# 3
# 267) Count Odd Digits in Number
# Python
# n = 123456
# count = 0

# while n > 0:
#     digit = n % 10
#     if digit % 2 != 0:
#         count += 1
#     n //= 10

# print(count)
# Output:
# Python
# 3
# 268) Find Frequency of Each Digit in Number
# Python
# n = "1223334444"

# for digit in "0123456789":
#     if digit in n:
#         print(digit, "=", n.count(digit))
# Output:
# Python
# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 4
# 269) Remove Zeros From Number
# Python
# n = "102030405"
# result = ""

# for ch in n:
#     if ch != "0":
#         result += ch

# print(result)
# Output:
# Python
# 12345
# 270) Check If Number Is Increasing Digits
# Python
# n = "123489"
# is_increasing = True

# for i in range(len(n)-1):
#     if n[i] >= n[i+1]:
#         is_increasing = False
#         break

# print(is_increasing)
# Output:
# Python
# True
# 271) Check If Number Is Decreasing Digits
# Python
# n = "97531"
# is_decreasing = True

# for i in range(len(n)-1):
#     if n[i] <= n[i+1]:
#         is_decreasing = False
#         break

# print(is_decreasing)
# Output:
# Python
# True
# 272) Find Difference Between Sum of Even and Odd Digits
# Python
# n = 123456
# even_sum = 0
# odd_sum = 0

# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:
#         even_sum += digit
#     else:
#         odd_sum += digit
#     n //= 10

# print(even_sum - odd_sum)
# Output:
# Python
# 3
# 273) Find Position of Largest Digit
# Python
# n = "58329"
# largest = max(n)
# print(n.index(largest))
# Output:
# Python
# 1
# 274) Find Position of Smallest Digit
# Python
# n = "58329"
# smallest = min(n)
# print(n.index(smallest))
# Output:
# Python
# 4
# 275) Count Number of Zeros in Number
# Python
# n = "100200300"
# count = 0

# for ch in n:
#     if ch == "0":
#         count += 1

# print(count)
# Output:
# Python
# 6
# 276) Find All Factors as List
# Python
# n = 12
# factors = []

# for i in range(1, n + 1):
#     if n % i == 0:
#         factors.append(i)

# print(factors)
# Output:
# Python
# [1, 2, 3, 4, 6, 12]
# 277) Sum of All Factors
# Python
# n = 12
# total = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i

# print(total)
# Output:
# Python
# 28
# 278) Product of All Factors
# Python
# n = 6
# product = 1

# for i in range(1, n + 1):
#     if n % i == 0:
#         product *= i

# print(product)
# Output:
# Python
# 36
# 279) Check If Number Is Composite
# Python
# n = 9
# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1

# if count > 2:
#     print("Composite")
# else:
#     print("Not Composite")
# Output:
# Python
# Composite
# 280) Print Composite Numbers from 1 to 20
# Python
# for n in range(2, 21):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count > 2:
#         print(n)
# Output:
# Python
# 4
# 6
# 8
# 9
# 10
# 12
# 14
# 15
# 16
# 18
# 20
# 281) Print Perfect Numbers from 1 to 100
# Python
# for n in range(1, 101):
#     total = 0
#     for i in range(1, n):
#         if n % i == 0:
#             total += i
#     if total == n:
#         print(n)
# Output:
# Python
# 6
# 28
# 282) Print Armstrong Numbers from 1 to 500
# Python
# for n in range(1, 501):
#     temp = n
#     total = 0
#     digits = len(str(n))

#     while temp > 0:
#         digit = temp % 10
#         total += digit ** digits
#         temp //= 10

#     if total == n:
#         print(n)
# Output:
# Python
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 153
# 370
# 371
# 407
# 283) Print Palindrome Numbers from 1 to 100
# Python
# for n in range(1, 101):
#     if str(n) == str(n)[::-1]:
#         print(n)
# Output:
# Python
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 11
# 22
# 33
# 44
# 55
# 66
# 77
# 88
# 99
# 284) Print Fibonacci Numbers Less Than 100
# Python
# a = 0
# b = 1

# while a < 100:
#     print(a)
#     a, b = b, a + b
# Output:
# Python
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 285) Find Nth Fibonacci Number
# Python
# n = 7
# a = 0
# b = 1

# for i in range(n):
#     a, b = b, a + b

# print(a)
# Output:
# Python
# 13
# 286) Check If Number Is Fibonacci
# Python
# n = 21
# a = 0
# b = 1
# found = False

# while a <= n:
#     if a == n:
#         found = True
#         break
#     a, b = b, a + b

# print(found)
# Output:
# Python
# True
# 287) Print Alternate Characters in String
# Python
# s = "python"

# for i in range(0, len(s), 2):
#     print(s[i])
# Output:
# Python
# p
# t
# o
# 288) Print Characters at Odd Index
# Python
# s = "python"

# for i in range(1, len(s), 2):
#     print(s[i])
# Output:
# Python
# y
# h
# n
# 289) Merge Two Strings Alternately
# Python
# s1 = "abc"
# s2 = "123"
# result = ""

# for i in range(len(s1)):
#     result += s1[i] + s2[i]

# print(result)
# Output:
# Python
# a1b2c3
# 290) Interleave Two Unequal Strings
# Python
# s1 = "abcd"
# s2 = "12"
# result = ""
# length = max(len(s1), len(s2))

# for i in range(length):
#     if i < len(s1):
#         result += s1[i]
#     if i < len(s2):
#         result += s2[i]

# print(result)
# Output:
# Python
# a1b2cd
# 291) Check If Two Strings Differ by One Character
# Python
# s1 = "cat"
# s2 = "cut"
# count = 0

# for i in range(len(s1)):
#     if s1[i] != s2[i]:
#         count += 1

# if count == 1:
#     print("Yes")
# else:
#     print("No")
# Output:
# Python
# Yes
# 292) Find Hamming Distance
# Python
# s1 = "karolin"
# s2 = "kathrin"
# count = 0

# for i in range(len(s1)):
#     if s1[i] != s2[i]:
#         count += 1

# print(count)
# Output:
# Python
# 3
# 293) Check If Two Strings Are One Rotation Apart
# Python
# s1 = "abcd"
# s2 = "dabc"

# if s2 in (s1 + s1):
#     print("Yes")
# else:
#     print("No")
# Output:
# Python
# Yes
# 294) Find All Prefixes of String
# Python
# s = "python"

# for i in range(1, len(s)+1):
#     print(s[:i])
# Output:
# Python
# p
# py
# pyt
# pyth
# pytho
# python
# 295) Find All Suffixes of String
# Python
# s = "python"

# for i in range(len(s)):
#     print(s[i:])
# Output:
# Python
# python
# ython
# thon
# hon
# on
# n
# 296) Check If String Is Symmetrical
# Python
# s = "abab"
# mid = len(s) // 2

# if s[:mid] == s[mid:]:
#     print("Symmetrical")
# else:
#     print("Not Symmetrical")
# Output:
# Python
# Symmetrical
# 297) Reverse Number Without Using String
# Python
# n = 12345
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10

# print(rev)
# Output:
# Python
# 54321
# 298) Check If Number Is Palindrome Without String
# Python
# n = 121
# temp = n
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# Output:
# Python
# Palindrome
# 299) Find Sum of Squares of Digits
# Python
# n = 123
# total = 0

# while n > 0:
#     digit = n % 10
#     total += digit * digit
#     n //= 10

# print(total)
# Output:
# Python
# 14
# 300) Check Happy Number
# Python
# n = 19
# seen = []

# while n != 1 and n not in seen:
#     seen.append(n)
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total += digit * digit
#         n //= 10
#     n = total

# if n == 1:
#     print("Happy Number")
# else:
#     print("Not Happy Number")
# Output:
# Python
# Happy Number
# ✅ Ab 1 se 300 complete ho gaye
# Ab tumne fresher Python interview ke liye bahut bada core area cover kar liya hai:
# Tumne cover kiya:
# Variables
# Operators
# If-Else
# Loops
# Numbers
# Strings
# Lists
# Tuples
# Dictionary
# Set
# Functions
# Recursion
# Lambda
# Manual built-in logic
# Frequency problems
# Matrix basics
# String interv







# Perfect. Ab hum real interview mode me jayenge.
# Ye wale questions function based, interviewer style, aur placement-focused honge.
# Top 100 Most Asked Python Interview Coding Questions
# (301 to 400)
# Rules:
# Only Python core
# No libraries
# Function based
# Code + Output
# Freshers interview focused
# 301) Function to Reverse a String
# Python
# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("python"))
# Output:
# Python
# nohtyp
# 302) Function to Check Palindrome String
# Python
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))
# print(is_palindrome("python"))
# Output:
# Python
# True
# False
# 303) Function to Count Vowels
# Python
# def count_vowels(s):
#     count = 0
#     for ch in s.lower():
#         if ch in "aeiou":
#             count += 1
#     return count

# print(count_vowels("Education"))
# Output:
# Python
# 5
# 304) Function to Count Consonants
# Python
# def count_consonants(s):
#     count = 0
#     for ch in s.lower():
#         if ch.isalpha() and ch not in "aeiou":
#             count += 1
#     return count

# print(count_consonants("Education"))
# Output:
# Python
# 4
# 305) Function to Find Factorial
# Python
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# print(factorial(5))
# Output:
# Python
# 120
# 306) Function to Check Prime Number
# Python
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(7))
# print(is_prime(10))
# Output:
# Python
# True
# False
# 307) Function to Print Prime Numbers in Range
# Python
# def primes_in_range(start, end):
#     for n in range(start, end + 1):
#         if n > 1:
#             prime = True
#             for i in range(2, n):
#                 if n % i == 0:
#                     prime = False
#                     break
#             if prime:
#                 print(n)

# primes_in_range(1, 20)
# Output:
# Python
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 308) Function to Find Sum of Digits
# Python
# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total

# print(sum_of_digits(1234))
# Output:
# Python
# 10
# 309) Function to Reverse a Number
# Python
# def reverse_number(n):
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n //= 10
#     return rev

# print(reverse_number(12345))
# Output:
# Python
# 54321
# 310) Function to Check Palindrome Number
# Python
# def is_palindrome_number(n):
#     temp = n
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n //= 10
#     return temp == rev

# print(is_palindrome_number(121))
# print(is_palindrome_number(123))
# Output:
# Python
# True
# False
# 311) Function to Find Largest Element in List
# Python
# def find_largest(lst):
#     largest = lst[0]
#     for num in lst:
#         if num > largest:
#             largest = num
#     return largest

# print(find_largest([10, 45, 2, 89, 33]))
# Output:
# Python
# 89
# 312) Function to Find Smallest Element in List
# Python
# def find_smallest(lst):
#     smallest = lst[0]
#     for num in lst:
#         if num < smallest:
#             smallest = num
#     return smallest

# print(find_smallest([10, 45, 2, 89, 33]))
# Output:
# Python
# 2
# 313) Function to Find Second Largest
# Python
# def second_largest(lst):
#     first = second = float('-inf')
#     for num in lst:
#         if num > first:
#             second = first
#             first = num
#         elif num > second and num != first:
#             second = num
#     return second

# print(second_largest([10, 20, 50, 40, 30]))
# Output:
# Python
# 40
# 314) Function to Find Second Smallest
# Python
# def second_smallest(lst):
#     first = second = float('inf')
#     for num in lst:
#         if num < first:
#             second = first
#             first = num
#         elif num < second and num != first:
#             second = num
#     return second

# print(second_smallest([10, 20, 50, 40, 30]))
# Output:
# Python
# 20
# 315) Function to Remove Duplicates From List
# Python
# def remove_duplicates(lst):
#     result = []
#     for num in lst:
#         if num not in result:
#             result.append(num)
#     return result

# print(remove_duplicates([1, 2, 2, 3, 1, 4]))
# Output:
# Python
# [1, 2, 3, 4]
# 316) Function to Count Frequency of Each Element
# Python
# def frequency_count(lst):
#     counted = []
#     for num in lst:
#         if num not in counted:
#             print(num, "=", lst.count(num))
#             counted.append(num)

# frequency_count([1, 2, 2, 3, 1, 4])
# Output:
# Python
# 1 = 2
# 2 = 2
# 3 = 1
# 4 = 1
# 317) Function to Find Sum of List
# Python
# def list_sum(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total

# print(list_sum([10, 20, 30, 40]))
# Output:
# Python
# 100
# 318) Function to Find Product of List
# Python
# def list_product(lst):
#     product = 1
#     for num in lst:
#         product *= num
#     return product

# print(list_product([1, 2, 3, 4]))
# Output:
# Python
# 24
# 319) Function to Count Even Numbers in List
# Python
# def count_even(lst):
#     count = 0
#     for num in lst:
#         if num % 2 == 0:
#             count += 1
#     return count

# print(count_even([1, 2, 3, 4, 5, 6]))
# Output:
# Python
# 3
# 320) Function to Count Odd Numbers in List
# Python
# def count_odd(lst):
#     count = 0
#     for num in lst:
#         if num % 2 != 0:
#             count += 1
#     return count

# print(count_odd([1, 2, 3, 4, 5, 6]))
# Output:
# Python
# 3
# 321) Function to Find Common Elements Between Two Lists
# Python
# def common_elements(a, b):
#     result = []
#     for num in a:
#         if num in b and num not in result:
#             result.append(num)
#     return result

# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
# Output:
# Python
# [3, 4]
# 322) Function to Merge Two Lists
# Python
# def merge_lists(a, b):
#     result = []
#     for num in a:
#         result.append(num)
#     for num in b:
#         result.append(num)
#     return result

# print(merge_lists([1, 2], [3, 4]))
# Output:
# Python
# [1, 2, 3, 4]
# 323) Function to Find Missing Number
# Python
# def find_missing(lst):
#     n = len(lst) + 1
#     expected = n * (n + 1) // 2
#     actual = sum(lst)
#     return expected - actual

# print(find_missing([1, 2, 3, 5]))
# Output:
# Python
# 4
# 324) Function to Find Maximum Difference
# Python
# def max_difference(lst):
#     return max(lst) - min(lst)

# print(max_difference([10, 3, 50, 6]))
# Output:
# Python
# 47
# 325) Function to Reverse a List
# Python
# def reverse_list(lst):
#     return lst[::-1]

# print(reverse_list([1, 2, 3, 4]))
# Output:
# Python
# [4, 3, 2, 1]
# 326) Function to Check If List Is Sorted
# Python
# def is_sorted(lst):
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i + 1]:
#             return False
#     return True

# print(is_sorted([1, 2, 3, 4]))
# print(is_sorted([1, 5, 3, 4]))
# Output:
# Python
# True
# False
# 327) Function to Find First Non-Repeating Element
# Python
# def first_non_repeating(lst):
#     for num in lst:
#         if lst.count(num) == 1:
#             return num

# print(first_non_repeating([2, 2, 3, 4, 4, 5]))
# Output:
# Python
# 3
# 328) Function to Find First Repeating Element
# Python
# def first_repeating(lst):
#     seen = []
#     for num in lst:
#         if num in seen:
#             return num
#         seen.append(num)

# print(first_repeating([1, 2, 3, 2, 4]))
# Output:
# Python
# 2
# 329) Function to Swap First and Last Element
# Python
# def swap_first_last(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst

# print(swap_first_last([10, 20, 30, 40]))
# Output:
# Python
# [40, 20, 30, 10]
# 330) Function to Find Length Without len()
# Python
# def manual_length(data):
#     count = 0
#     for _ in data:
#         count += 1
#     return count

# print(manual_length("python"))
# print(manual_length([1, 2, 3, 4]))
# Output:
# Python
# 6
# 4
# 331) Function to Count Words in a String
# Python
# def count_words(s):
#     return len(s.split())

# print(count_words("I love python programming"))
# Output:
# Python
# 4
# 332) Function to Find Longest Word
# Python
# def longest_word(s):
#     words = s.split()
#     longest = words[0]
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest

# print(longest_word("python is very powerful language"))
# Output:
# Python
# powerful
# 333) Function to Find Shortest Word
# Python
# def shortest_word(s):
#     words = s.split()
#     shortest = words[0]
#     for word in words:
#         if len(word) < len(shortest):
#             shortest = word
#     return shortest

# print(shortest_word("python is very powerful language"))
# Output:
# Python
# is
# 334) Function to Count Character Frequency
# Python
# def char_frequency(s):
#     counted = []
#     for ch in s:
#         if ch not in counted:
#             print(ch, "=", s.count(ch))
#             counted.append(ch)

# char_frequency("banana")
# Output:
# Python
# b = 1
# a = 3
# n = 2
# 335) Function to Find First Non-Repeating Character
# Python
# def first_non_repeating_char(s):
#     for ch in s:
#         if s.count(ch) == 1:
#             return ch

# print(first_non_repeating_char("aabbcdde"))
# Output:
# Python
# c
# 336) Function to Find First Repeating Character
# Python
# def first_repeating_char(s):
#     seen = ""
#     for ch in s:
#         if ch in seen:
#             return ch
#         seen += ch

# print(first_repeating_char("abcaef"))
# Output:
# Python
# a
# 337) Function to Remove Spaces From String
# Python
# def remove_spaces(s):
#     result = ""
#     for ch in s:
#         if ch != " ":
#             result += ch
#     return result

# print(remove_spaces("I love python"))
# Output:
# Python
# Ilovepython
# 338) Function to Replace Spaces With Hyphen
# Python
# def replace_spaces(s):
#     return s.replace(" ", "-")

# print(replace_spaces("I love python"))
# Output:
# Python
# I-love-python
# 339) Function to Toggle Case
# Python
# def toggle_case(s):
#     result = ""
#     for ch in s:
#         if ch.isupper():
#             result += ch.lower()
#         else:
#             result += ch.upper()
#     return result

# print(toggle_case("PyThOn"))
# Output:
# Python
# pYtHoN
# 340) Function to Check Anagram
# Python
# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)

# print(is_anagram("listen", "silent"))
# print(is_anagram("hello", "world"))
# Output:
# Python
# True
# False
# 341) Function to Count Uppercase Letters
# Python
# def count_uppercase(s):
#     count = 0
#     for ch in s:
#         if ch.isupper():
#             count += 1
#     return count

# print(count_uppercase("PyThOn"))
# Output:
# Python
# 3
# 342) Function to Count Lowercase Letters
# Python
# def count_lowercase(s):
#     count = 0
#     for ch in s:
#         if ch.islower():
#             count += 1
#     return count

# print(count_lowercase("PyThOn"))
# Output:
# Python
# 3
# 343) Function to Count Digits in String
# Python
# def count_digits(s):
#     count = 0
#     for ch in s:
#         if ch.isdigit():
#             count += 1
#     return count

# print(count_digits("Python1234"))
# Output:
# Python
# 4
# 344) Function to Extract Digits From String
# Python
# def extract_digits(s):
#     result = ""
#     for ch in s:
#         if ch.isdigit():
#             result += ch
#     return result

# print(extract_digits("ab12cd34"))
# Output:
# Python
# 1234
# 345) Function to Find ASCII Value of Character
# Python
# def ascii_value(ch):
#     return ord(ch)

# print(ascii_value("A"))
# Output:
# Python
# 65
# 346) Function to Convert ASCII to Character
# Python
# def char_from_ascii(num):
#     return chr(num)

# print(char_from_ascii(97))
# Output:
# Python
# a
# 347) Function to Count Occurrence of a Substring
# Python
# def count_substring(s, sub):
#     count = 0
#     for i in range(len(s) - len(sub) + 1):
#         if s[i:i+len(sub)] == sub:
#             count += 1
#     return count

# print(count_substring("abababa", "aba"))
# Output:
# Python
# 3
# 348) Function to Check Startswith
# Python
# def starts_with(s, prefix):
#     return s[:len(prefix)] == prefix

# print(starts_with("python", "py"))
# Output:
# Python
# True
# 349) Function to Check Endswith
# Python
# def ends_with(s, suffix):
#     return s[-len(suffix):] == suffix

# print(ends_with("python", "on"))
# Output:
# Python
# True
# 350) Function to Reverse Words in Sentence
# Python
# def reverse_words(sentence):
#     words = sentence.split()
#     return " ".join(words[::-1])

# print(reverse_words("I love python"))
# Output:
# Python
# python love I
# 351) Function to Check Armstrong Number
# Python
# def is_armstrong(n):
#     temp = n
#     total = 0
#     digits = len(str(n))

#     while temp > 0:
#         digit = temp % 10
#         total += digit ** digits
#         temp //= 10

#     return total == n

# print(is_armstrong(153))
# print(is_armstrong(123))
# Output:
# Python
# True
# False
# 352) Function to Check Perfect Number
# Python
# def is_perfect(n):
#     total = 0
#     for i in range(1, n):
#         if n % i == 0:
#             total += i
#     return total == n

# print(is_perfect(6))
# print(is_perfect(10))
# Output:
# Python
# True
# False
# 353) Function to Find GCD
# Python
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# print(gcd(12, 18))
# Output:
# Python
# 6
# 354) Function to Find LCM
# Python
# def lcm(a, b):
#     greater = max(a, b)
#     while True:
#         if greater % a == 0 and greater % b == 0:
#             return greater
#         greater += 1

# print(lcm(12, 18))
# Output:
# Python
# 36
# 355) Function to Generate Fibonacci Series
# Python
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a)
#         a, b = b, a + b

# fibonacci(7)
# Output:
# Python
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 356) Function to Find Nth Fibonacci Number
# Python
# def nth_fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# print(nth_fibonacci(7))
# Output:
# Python
# 13
# 357) Function to Check Leap Year
# Python
# def is_leap(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# print(is_leap(2024))
# print(is_leap(2023))
# Output:
# Python
# True
# False
# 358) Function to Find Table of a Number
# Python
# def multiplication_table(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)

# multiplication_table(5)
# Output:
# Python
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
# 359) Function to Check Even or Odd
# Python
# def even_or_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     return "Odd"

# print(even_or_odd(8))
# print(even_or_odd(7))
# Output:
# Python
# Even
# Odd
# 360) Function to Find Positive, Negative or Zero
# Python
# def number_type(n):
#     if n > 0:
#         return "Positive"
#     elif n < 0:
#         return "Negative"
#     else:
#         return "Zero"

# print(number_type(10))
# print(number_type(-5))
# print(number_type(0))
# Output:
# Python
# Positive
# Negative
# Zero
# 361) Function to Find Sum of Natural Numbers
# Python
# def sum_natural(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total

# print(sum_natural(10))
# Output:
# Python
# 55
# 362) Function to Find Cube of a Number
# Python
# def cube(n):
#     return n ** 3

# print(cube(4))
# Output:
# Python
# 64
# 363) Function to Find Square of a Number
# Python
# def square(n):
#     return n ** 2

# print(square(9))
# Output:
# Python
# 81
# 364) Function to Swap Two Numbers
# Python
# def swap(a, b):
#     a, b = b, a
#     return a, b

# print(swap(10, 20))
# Output:
# Python
# (20, 10)
# 365) Function to Find Average of List
# Python
# def average(lst):
#     return sum(lst) / len(lst)

# print(average([10, 20, 30, 40]))
# Output:
# Python
# 25.0
# 366) Function to Count Positive Numbers in List
# Python
# def count_positive(lst):
#     count = 0
#     for num in lst:
#         if num > 0:
#             count += 1
#     return count

# print(count_positive([1, -2, 3, -4, 5]))
# Output:
# Python
# 3
# 367) Function to Count Negative Numbers in List
# Python
# def count_negative(lst):
#     count = 0
#     for num in lst:
#         if num < 0:
#             count += 1
#     return count

# print(count_negative([1, -2, 3, -4, 5]))
# Output:
# Python
# 2
# 368) Function to Find Sum of Positive Numbers
# Python
# def sum_positive(lst):
#     total = 0
#     for num in lst:
#         if num > 0:
#             total += num
#     return total

# print(sum_positive([1, -2, 3, -4, 5]))
# Output:
# Python
# 9
# 369) Function to Find Sum of Negative Numbers
# Python
# def sum_negative(lst):
#     total = 0
#     for num in lst:
#         if num < 0:
#             total += num
#     return total

# print(sum_negative([1, -2, 3, -4, 5]))
# Output:
# Python
# -6
# 370) Function to Check If Number Is Fibonacci
# Python
# def is_fibonacci(n):
#     a, b = 0, 1
#     while a <= n:
#         if a == n:
#             return True
#         a, b = b, a + b
#     return False

# print(is_fibonacci(21))
# print(is_fibonacci(22))
# Output:
# Python
# True
# False
# 371) Function to Find All Factors
# Python
# def all_factors(n):
#     factors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)
#     return factors

# print(all_factors(12))
# Output:
# Python
# [1, 2, 3, 4, 6, 12]
# 372) Function to Count Factors
# Python
# def count_factors(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     return count

# print(count_factors(12))
# Output:
# Python
# 6
# 373) Function to Check Composite Number
# Python
# def is_composite(n):
#     if n < 2:
#         return False
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     return count > 2

# print(is_composite(9))
# print(is_composite(7))
# Output:
# Python
# True
# False
# 374) Function to Find Sum of Even Numbers in Range
# Python
# def sum_even_range(start, end):
#     total = 0
#     for i in range(start, end + 1):
#         if i % 2 == 0:
#             total += i
#     return total

# print(sum_even_range(1, 10))
# Output:
# Python
# 30
# 375) Function to Find Sum of Odd Numbers in Range
# Python
# def sum_odd_range(start, end):
#     total = 0
#     for i in range(start, end + 1):
#         if i % 2 != 0:
#             total += i
#     return total

# print(sum_odd_range(1, 10))
# Output:
# Python
# 25
# 376) Function to Count Even Digits
# Python
# def count_even_digits(n):
#     count = 0
#     while n > 0:
#         digit = n % 10
#         if digit % 2 == 0:
#             count += 1
#         n //= 10
#     return count

# print(count_even_digits(123456))
# Output:
# Python
# 3
# 377) Function to Count Odd Digits
# Python
# def count_odd_digits(n):
#     count = 0
#     while n > 0:
#         digit = n % 10
#         if digit % 2 != 0:
#             count += 1
#         n //= 10
#     return count

# print(count_odd_digits(123456))
# Output:
# Python
# 3
# 378) Function to Find Largest Digit
# Python
# def largest_digit(n):
#     largest = 0
#     while n > 0:
#         digit = n % 10
#         if digit > largest:
#             largest = digit
#         n //= 10
#     return largest

# print(largest_digit(58329))
# Output:
# Python
# 9
# 379) Function to Find Smallest Digit
# Python
# def smallest_digit(n):
#     smallest = 9
#     while n > 0:
#         digit = n % 10
#         if digit < smallest:
#             smallest = digit
#         n //= 10
#     return smallest

# print(smallest_digit(58329))
# Output:
# Python
# 2
# 380) Function to Count Zeros in Number
# Python
# def count_zeros(n):
#     count = 0
#     for ch in str(n):
#         if ch == "0":
#             count += 1
#     return count

# print(count_zeros(100200300))
# Output:
# Python
# 6
# 381) Function to Merge Two Strings Alternately
# Python
# def merge_alternate(s1, s2):
#     result = ""
#     for i in range(len(s1)):
#         result += s1[i] + s2[i]
#     return result

# print(merge_alternate("abc", "123"))
# Output:
# Python
# a1b2c3
# 382) Function to Check If String Contains Only Digits
# Python
# def only_digits(s):
#     return s.isdigit()

# print(only_digits("12345"))
# print(only_digits("123a"))
# Output:
# Python
# True
# False
# 383) Function to Check If String Contains Only Alphabets
# Python
# def only_alpha(s):
#     return s.isalpha()

# print(only_alpha("Python"))
# print(only_alpha("Python123"))
# Output:
# Python
# True
# False
# 384) Function to Check If String Contains Only Alphanumeric
# Python
# def only_alnum(s):
#     return s.isalnum()

# print(only_alnum("Python123"))
# print(only_alnum("Python 123"))
# Output:
# Python
# True
# False
# 385) Function to Find Index of Character
# Python
# def find_index(s, target):
#     for i in range(len(s)):
#         if s[i] == target:
#             return i

# print(find_index("python", "h"))
# Output:
# Python
# 3
# 386) Function to Find All Indices of Character
# Python
# def all_indices(s, target):
#     result = []
#     for i in range(len(s)):
#         if s[i] == target:
#             result.append(i)
#     return result

# print(all_indices("banana", "a"))
# Output:
# Python
# [1, 3, 5]
# 387) Function to Remove Character From String
# Python
# def remove_char(s, target):
#     result = ""
#     for ch in s:
#         if ch != target:
#             result += ch
#     return result

# print(remove_char("python", "t"))
# Output:
# Python
# pyhon
# # 388) Function to Replace Character
# Function to Replace Character in String
# Python
# def replace_char(s, old, new):
#     result = ""
#     for ch in s:
#         if ch == old:
#             result += new
#         else:
#             result += ch
#     return result

# print(replace_char("banana", "a", "@"))
# Output:
# Python
# b@n@n@
# 389) Function to Find Middle Character
# Python
# def middle_char(s):
#     mid = len(s) // 2
#     return s[mid]

# print(middle_char("python"))
# Output:
# Python
# h
# 390) Function to Find Middle Two Characters
# Python
# def middle_two(s):
#     mid = len(s) // 2
#     return s[mid-1:mid+1]

# print(middle_two("python"))
# Output:
# Python
# th
# 391) Function to Swap First and Last Character
# Python
# def swap_first_last_char(s):
#     return s[-1] + s[1:-1] + s[0]

# print(swap_first_last_char("python"))
# Output:
# Python
# nythop
# 392) Function to Find Duplicate Characters
# Python
# def duplicate_chars(s):
#     result = ""
#     for ch in s:
#         if s.count(ch) > 1 and ch not in result:
#             result += ch
#     return result

# print(duplicate_chars("programming"))
# Output:
# Python
# rgm
# 393) Function to Find Unique Characters
# Python
# def unique_chars(s):
#     result = ""
#     for ch in s:
#         if s.count(ch) == 1:
#             result += ch
#     return result

# print(unique_chars("programming"))
# Output:
# Python
# poain
# 394) Function to Check Pangram
# Python
# def is_pangram(s):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     s = s.lower()
#     for ch in alphabet:
#         if ch not in s:
#             return False
#     return True

# print(is_pangram("the quick brown fox jumps over the lazy dog"))
# Output:
# Python
# True
# 395) Function to Count Lines in Multi-line String
# Python
# def count_lines(s):
#     count = 1
#     for ch in s:
#         if ch == "\n":
#             count += 1
#     return count

# print(count_lines("Python\nJava\nSQL"))
# Output:
# Python
# 3
# 396) Function to Find Hamming Distance
# Python
# def hamming_distance(s1, s2):
#     count = 0
#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             count += 1
#     return count

# print(hamming_distance("karolin", "kathrin"))
# Output:
# Python
# 3
# 397) Function to Check One Rotation
# Python
# def is_rotation(s1, s2):
#     return s2 in (s1 + s1)

# print(is_rotation("abcd", "dabc"))
# print(is_rotation("abcd", "acbd"))
# Output:
# Python
# True
# False
# 398) Function toFind All Prefixes
# Python
# def all_prefixes(s):
#     for i in range(1, len(s)+1):
#         print(s[:i])

# all_prefixes("python")
# Output:
# Python
# p
# py
# pyt
# pyth
# pytho
# python
# 399) Function to Find All Suffixes
# Python
# def all_suffixes(s):
#     for i in range(len(s)):
#         print(s[i:])

# all_suffixes("python")
# Output:
# Python
# python
# ython
# thon
# hon
# on
# n
# 400) Function to Check Symmetrical String
# Python
# def is_symmetrical(s):
#     mid = len(s) // 2
#     return s[:mid] == s[mid:]

# print(is_symmetrical("abab"))
# print(is_symmetrical("abcd"))
# Output:
# Python
# True
# False 