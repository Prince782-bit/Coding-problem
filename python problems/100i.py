
# check number is even or odd:
# num = 7
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")




# Swap two variables without using a third variable:
# a,b = 5,10
# a,b, = b,a

# print("a =",a)
# print("b =",b)




# reverse a string:
# text = "python"
# reversed_text = text[::-1]
# print(reversed_text)



# Find the factorial of a number :
# num = 5
# factorial = 1
# for i in range(1,num + 1):
#     factorial *= i
# print("Factorial:", factorial)




# Find the largest in a list:
# numbers = [10,5,20,8]
# largest = max(numbers)
# print("Largest number:", largest)




# Check if a string is a palindrome:
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))
# print(is_palindrome("vikas"))




# Count the numbers of vowels in a string :
# text = "hello, world"
# vowels = "aeiouAEUIO"
# count = sum(1 for char in text if char in vowels)
# print("Numbers of vowels:", count)



# Find the sum of digits of a numers:
# num = 1234
# sum_digits = sum(int(digit) for digit in str(num))
# print("Sum of digits:", sum_digits)


# Generate fibonacci series(first 5 numbers):
# n = 10
# a,b = 0, 1
# for _ in range(n):
#     print(a,end=" ")
#     a,b = b, a+b




# Remove duplicates from a list:
# numbers = [1,2,2,3,4,4,4,5]
# unique_numbers = list(set(numbers))
# print(unique_numbers)



# Find the second largest number in a list:
# def second_largest(lst):
#     unique_lst = list(set(lst))
#     unique_lst.sort()
#     return unique_lst[-2] if len(unique_lst) > 1 else None
# print(second_largest([10,20,4,45,99,99]))



# Find the GCD of twonumbers :
# import math

# def find_gcd(a,b):
#     return math.gcd(a,b)
# print(find_gcd(54,24))



# Find the lcm of two numbers :
# import math
# def find_lcm(a,b):
#     return abs(a*b) // math.gcd(a,b)
# print(find_lcm(12,15))



# Check if a number is an armstrong :
# def is_armstrong(n):
#     num_str = str(n)
#     power = len(num_str)
#     return n == sum(int(digit) ** power for digit in num_str)

# print(is_armstrong(153))
# print(is_armstrong(123))




# Convert celsius to fahrenheit:
# def celsius_to_fahrenhei(c):
#     return (c*9/5) + 32

# print(celsius_to_fahrenhei(0))
# print(celsius_to_fahrenhei(100))





# countth freuency of worlds in a string :
# from collections import Counter

# def word_frequency(s):
#     words = s.split()
#     return dict(Counter(words))
# print(word_frequency("hello world hello python"))





# find the intersection of two lists :
# def list_intersection(list1,list2):
#     return list(set(list1) & set(list2))
# print(list_intersection([1,2,3,4], [3,4,5,6]))



# Reverse a number:
# def reverse_number(n):
#     return int(str(n)[::-1])
# print(reverse_number(12345))




# Check if a given year is a leap yeap:
# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# print(is_leap_year(2024))
# print(is_leap_year(1900))




# find the missing number in an array :
# def find_missing_numbe(lst, n):
#     return sum(range(1,n+1)) - sum(lst)

# print(find_missing_numbe([1,2,4,5,6], 6))






# Find the sum of even and odd numbers in list:
# def sum_even_odd(list):
#     even_sum = sum(x for x in list if x % 2 == 0)
#     odd_sum = sum(x for x in list if x % 2 != 0)
#     return even_sum, odd_sum
# print(sum_even_odd([1,2,3,4,5,6]))




# Remove duplicates from a list :
# def remove_duplicates(lst):
#     return list(set(lst))

# print(remove_duplicates([1,2,2,3,4,4,5]))




# Merge two sorted list :
# def merge_sorted_list(list1, list2):
#     return sorted(list1 + list2)
# print(merge_sorted_list([1,2,5],[2,4,6]))



# Find the first non-repeating char in a string :
# def first_non_repeating_char(s):
#     for char in s:
#         if s.count(char) == 1:
#             return char
#     return None
# print(first_non_repeating_char("swiss"))




# Check if two string are anagrams:
# def are_angrams(str1, str2):
#     return sorted(str1) == sorted(str2)
# print(are_angrams("Listen", "silent"))
# print(are_angrams("hell", "world"))




# Find common element between two lists:
# def common_elements(list1, list2):
#     return list(set(list1) & set(list2))

# print(common_elements([1,2,3,4],[3,4,5,6]))





# Find the intersection of two sets :
# def set_intersection(set1, set2):
#     return set1.intersection(set2)
# print(set_intersection({1,2,3},{2,3,4}))



# Check if a string is a pangram:
# import string
# def is_pangram(str):
#     return 
# set(string.ascii_lowercase).issubset(set(str.lower()))
# print(is_pangram("The uick bron for jumps over the lazy dog"))



# find the most frequent elemet in a list :
# from collections import Counter
# def most_frequent(lst):
#     return Counter(lst).most_common(1)[0][0]
# print(most_frequent([1,2,2,3,3,3,4,4,4,4,4]))


# generate a random password :
# import random
# import string

# def generate_password(length = 8):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return "".join (random.choice(characters) for _ in range(length))
# print(generate_password(12))




# Check if a given numbers is a perfect number;
# def is_perfect(n):
#     return sum(i for i in range(1,n) if n % i == 0) == n
# print(is_perfect(6))
# print(is_perfect(28))




# find the HCF of a list of numbers:
# import math
# from functools import reduce

# def find_hcf(lst):
#     return reduce(math.gcd,lst)
# print(find_hcf([12,18,24]))





# Find the smallest and largest numbers in a list:
# def min_max(lst):
#     return min(lst), max(lst)
# print(min_max([3,1,8,6,10]))




# Find ths sum of prime numbers in a list:
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def sum_of_primes(lst):
#     return sum(n for n in lst if is_prime(n))
# print(sum_of_primes([1,2,3,4,5,6,7,8,9,10]))






# find the maximum subarray sum :
# def max_subarray_sum(arr):
#     max_sum = float('-inf')
#     current_sum = 0
#     for num in arr:
#         current_sum = max(num, current_sum+num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum
# print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))





# Count the number of words in a sentence:
# def worl_count(sentence):
#     return len(sentence.split())
# print(worl_count("Hello world! welcome to python programmin."))





# find the nth fibonacci numbers(recursive):
# def fibonacci(n):
#     if n <= 0:
#         return "invalid input"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(7))






# find the nth fibonacci number(iterative) :
# def fibonacci(n):
#     a,b =0,1
#     for _ in range(n - 1):
#         a,b = b, a+b
#     return a
# print(fibonacci(7))






# Convert a string to title case:
# def to_title_case(s):
#     return s.title()
# print(to_title_case("hello world! this is python."))






# Find the length of the longest worl in a sentence:
# def longest_word_length(sentence):
#     return max(len(word) for word in sentence.split())
# print(longest_word_length("python is an amazing programming language"))




# print a right angle triangle pattern :
# def triangle_pattern(n):
#     for i in range(1, n+1):
#         print("*" * i)
# triangle_pattern(5)





# print a pyramid pattern :
# def pyraid_patttern(n):
#     for i in range(n):
#         print(" " * (n-i-1)+ "* " *(i + 1))
# pyraid_patttern(5)




# find the sum of the first n natural numbers:
# def sum_natural_numbers(n):
#     return n * (n+1) // 2
# print(sum_natural_numbers(10))






# Convert a decimal number to binary :
# def decimal_to_binary(n):
#     return bin(n)[2:]
# print(decimal_to_binary(10))




# convert a binary numbers to decimal numbers:
# def binary_to_decimal(b):
#     return int(b,2)
# print(binary_to_decimal("1010"))





# Convert a number to roman numbers:
# # Find the prime number in a range:
# def primes_in_range(start,end):
#     primes = []
#     for num in range(start, end + 1):
#         if num > 1 and all (num % i != 0 for i in range(2, int(num ** 0.5)+1)):
#             primes.append(num)
#     return primes
# print(primes_in_range(10,50))






# Count the occurence of each character in strnig :
# from collections import Counter
# def char_count(s):
#     return dict(Counter(s))
# print(char_count("hello world"))






# Check if a list is sorted(ascending order) :
# def is_sorted(lst):
#     return lst == sorted(lst)
# print(is_sorted([1,2,3,4,5]))
# print(is_sorted([5,3,2,1]))





# Convert a list of tuple into a dictionary :
# def list_to_dict(tuple):
#     return dict(tuple)
# print(list_to_dict([("a", 1), ("b", 2), ("c", 3)]))




# flatten a nested list :
# def flattern_list(nested_list):
#     return [item for sublist in nested_list for item in sublist]
# print(flattern_list([[1,2],[3,4],[5,6]]))



# Convert to dict to list of tuple :
# def dict_to_list(d):
#     return list(d.items())
# print(dict_to_list({"a": 1, "b":2, "c":3}))





# Remove all whitespace from a string :
# def remove_whitespace(s):
#     return "".join(s.split())
# print(remove_whitespace("  hello     world  !   "))




# Generate a list of even numbers in a range :
# def even_numbes(start, end):
#     return [x for x in range(start, end + 1) if x % 2 == 0]
# print(even_numbes(1,10))




# find the intersection of two sets:
# def set_intersection(set1, set2):
#     return set1 & set2
# print(set_intersection({1,2,3},{2,3,4}))




# # Convert a tuple to a string:
# def tuple_to_string(t):
#     return "".join(t)
# print(tuple_to_string(('h','e','l','l','o')))





# Count the number of uppercase and lowercase letters in a string:
# def count_case(s):
#     upper = sum(1 for char in s if char.isupper())
#     lower = sum(1 for char in s if char.islower())
#     return upper, lower
# print(count_case("Hello World"))





# Convert a string to a list of char:
# def string_to_list(s):
#     return list(s)
# print(string_to_list("Hello"))




# Find the sum of the square of the first N natural numbers:
# def sum_of_square(n):
#     return sum(x ** 2 for x in range(1, n+1))
# print(sum_of_square(5))




# find the sum of the cube of the first N natural number:
# def sum_of_cube(n):
#     return sum(x ** 3 for x in range(1, n+1))
# print(sum_of_cube(5))




# Reversea tuple:
# def reverse_tuple(t):
#     return t[::-1]
# print(reverse_tuple((1,2,3,4,5)))




# Remove vowels from a string :
# def remove_vowels(s):
#     return "".join(char for char in s if char.lower() not in "aeiuo")
# print(remove_vowels("Hello World"))




# Convert a list of integer to a single interger :
# def list_to_int(list):
#     return int("".join(map(str, list)))
# print(list_to_int([1,2,3,4,5]))




# find the ASCII Value of a char:
# def char_to_ascii(char):
#     return ord(char)
# print(char_to_ascii('A'))




# Convert ASXII value to char:
# def ascii_to_char(value):
#     return chr(value)
# print(ascii_to_char(65))





# find the maximum and minimum ASCII value in a string :
# def max_min_ascii(s):
#     return max(ord(char) for char in s), min(ord(char) for char in s)
# print(max_min_ascii("Hello"))





# Convert a list to a comma-separated string:
# def list_to_csv(lst):
#     return ", ".join(map(str, lst))
# print(list_to_csv([1,2,3,4,5]))




# Convert a string to a dict of char freuencies:
# from collections import Counter
# def string_to_fre_dict(s):
#     return dict(Counter(s))
# print(string_to_fre_dict("banana"))





# Convert a dict to a json string:
# import json
# def dict_to_json(d):
#     return json.dumps(d)
# print(dict_to_json({"name":"alice", "age":25}))




# Replace a world in a string:
# def replace_world(s,old,new):
#     return s.replace(old, new)
# print(replace_world("Hello world", "workd", "python"))




# Convert a string to camel case:
# def to_camel_case(s):
#     words = s.split()
#     return words[0].lower() + "".join(word.capitalize() for word in words[1:])
# print(to_camel_case("hello world python"))





# Check if a string is a valid email address:
# import re
# def is_valid_email(email):
#     pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     return bool(re.match(pattern, email))
# print(is_valid_email("test@example.com"))
# print(is_valid_email("invalid-email"))





# Find the factorial of a number(recursive):
# def factorial(n):
#     return 1  if n == 0 else n * factorial(n-1)
# print(factorial(5))






# # find the factorial of a number :
# def factorial(n):
#     result=1
#     for i in range(2, n+1):
#         result *= i
#     return result
# print(factorial(5))




# Convert temperature from celsius to fahrenheit:
# def celsius_to_fahrenheit(c):
#     return (c * 9/5) + 32
# print(celsius_to_fahrenheit(0))
# print(celsius_to_fahrenheit(100))




# Convert temperature from fahrenheit to celsius:
# def fahrenheit_to_celsius(f):
#     return (f-32) * 5/9
# print(fahrenheit_to_celsius(32))
# print(fahrenheit_to_celsius(212))






# Count the number of digits in an integer:
# def count_digits(n):
#     return len(str(abs(n)))
# print(count_digits(123456))
# print(count_digits(-9876))





# Find the largest word in a sentence:
# def largest_word(sentence):
#     return max(sentence.split(), key=len)
# print(largest_word("Python is an amazing programming language."))





# Find the smallest word in a sentence:
# def smallest_word(sentence):
#     return min(sentence.split(), key=len)
# print(smallest_word("python is an amazing programming language"))





# Swap two numbers without using a temporary variable:
# def swap_numbers(a,b):
#     a,b =b,a
#     return a,b
# print(swap_numbers(5,10))





# Find the sum of all digit in a number:
# def sum_of_digits(n):
#     return sum(int(digit) for digit in str(abs(n)))
# print(sum_of_digits(12345))





# find the average of a list numbers:
# def average(list):
#     return sum(list)/len(list) if list else 0
# print(average([10,20,30,40,50]))





# check if a number is an armstrong:
# def is_armstrong(n):
#     return n == sum(int(digit) ** len(str(n)) for digit in str(n))
# print(is_armstrong(153))
# print(is_armstrong(9474))
# print(is_armstrong(123))





# find the GCD of two numbers:
# import math
# def find_gcd(a,b):
#     return math.gcd(a,b)
# print(find_gcd(48,18))




# convert a decimal to binary number:
# def decimal_to_binary(n):
#     return bin(n)[2:]
# print(decimal_to_binary(10))




# Check if two string are anagrams:
# from collections import Counter
# def is_anagram(s1,s2):
#     return Counter(s1) == Counter(s2)
# print(is_anagram("listen", "silent"))
# print(is_anagram("hello", "world"))





# Count the number of unique words in a sentence:
# def unique_count(sentence):
#     return len(set(sentence.split()))
# print(unique_count("Python is great and Python is easy"))





# Find the first non-repeating char in a string:
# from collections import Counter
# def first_non_repeating(s):
#     count = Counter(s)
#     for char in s:
#         if count[char] == 1:
#             return char
#     return None
# print(first_non_repeating("swiss"))





# Check if a string is a palindrome :
# def is_palindrome(s):
#     s = "". join(s.lower().split())
#     return s == s[::-1]
# print(is_palindrome("A man a plan a canal panama"))
# print(is_palindrome("hello"))





# Check if a list is sorted:
# def is_sorted(list):
#     return list == sorted(list)
# print(is_sorted([1,2,3,4,5]))
# print(is_sorted([5,3,2,1]))





# Convert a list of integers to a string with dashes:
# def list_to_dash_string(list):
#     return "-".join(map(str, list))
# print(list_to_dash_string([1,2,3,4,5]))





# Find the common element between two lists:
# def common_element(list1, list2):
#     return list(set(list1) & set(list2))
# print(common_element([1,2,3,4],[3,4,5,6]))





# find the most frequent element in a list:
# from collections import Counter
# def most_frequent(list):
#     return Counter(list).most_common(1)[0][0]
# print(most_frequent([1,2,3,1,2,1,4,1]))





# find the second largest number in a list:
# def second_largest(list):
#     return sorted(set(list))[-2] if len(set(list)) > 1 else None
# print(second_largest([10,20,4,45,99]))





# Count the number of even and odd numbers in a list:
# def count_even_odd(list):
#     evens = sum(1 for x in list if x % 2 == 0)
#     odds = len(list) - evens
#     return evens, odds
# print(count_even_odd([1,2,3,4,5,6,7,8,9]))





# Count the number of even and odd numbers in list:
# def count_even_odd(list):
#     evens = sum(1 for x in list if x % 2 == 0)
#     odds = len(list) - evens
#     return evens, odds
# print(count_even_odd([1,2,3,4,5,6,7,8,9]))






# find the intersection of two lists:
# def list_intersection(list1, list2):
#     return list(set(list1) & set(list2))
# print(list_intersection([1,2,3,4],[3,4,5,6]))




# find the union of two lists:
# def list_union(list1,list2):
#     return list(set(list1) | set(list2))
# print(list_union([1,2,3,4],[3,4,5,6]))




# # Merge two sorted lists:
# def merge_sorted_lists(list1, list2):
#     return sorted(list1 + list2)
# print(merge_sorted_lists([1,3,5],[2,4,6]))





# # find the maximum and minimum elements in a list:
# def find_max_min(list):
#     return max(list), min(list)
# print(find_max_min([10,20,30,40,50]))





# # Remove duplicate from the list:
# def remove_duplicates(lst):
#     return list(set(lst))
# print(remove_duplicates([1,2,2,2,3,4,4,4,5]))




# # Reverse words in a sentence:
# def reverse_words(sentence):
#     return " ".join(sentence.split()[::-1])
# print(reverse_words("Hello world Python"))







# find the median of a list:
# import statistics
# def find_median(list):
#     return statistics.median(list)
# print(find_median([1,2,3,4,5]))
# print(find_median([1,2,3,4,5,6]))






# # find the mode of a list:
# import statistics
# def find_mode(list):
#     return statistics.mode(list)
# print(find_mode([1,2,2,3,4,4,4,4,5]))





# # Convert a list of string to uppercase:
# def to_upper_case(list):
#     return [word.upper() for word in list]
# print(to_upper_case(["hello","world"]))






# # Check if a year is a leap year:
# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# print(is_leap_year(2020))
# print(is_leap_year(2023))






# # Count the Occurrence of each char in a string:
# from collections import Counter
# def char_count(s):
#     return dict(Counter(s))
# print(char_count("banana"))





# # Find the largest palindromic substring:
# def is_palindrome(s):
#     return s == s[::-1]
# def longest_palindrome(s):
#     n = len(s)
#     max_palindrome = ""
#     for i in range(n):
#         for j in range(i, n):
#             substr = s[i:j + 1]
#             if is_palindrome(substr) and len(substr)> len(max_palindrome):
#                 max_palindrome = substr
#         return max_palindrome
# print(longest_palindrome("babad"))






# # find all permutation of string:
# from itertools import permutations
# def all_permutations(s):
#     return ["".join(p) for p in permutations(s)]
# print(all_permutations("abc"))




# find the first repeating char in a string:
# def first_repeating_char(s):
#     seen = set()
#     for char in s:
#         if char in seen:
#             return char
#         seen.add(char)
#     return None
# print(first_repeating_char("abca"))




# # find the first non-repeating word in a sentence:
# from collections import Counter
# def first_non_repeating_word(sentence):
#     words = sentence.split()
#     count = Counter(words)
#     for word in words:
#         if count[word] == 1:
#             return word
#     return None
# print(first_non_repeating_word("apple banana orange apple banana mango"))






# # Generate a random password:
# import random 
# import string
# def generate_passwors(length=8):
#     chars = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(random.choice(chars) for _ in range(length))
# print(generate_passwors(10))





# # find the intersection of multiple lists:
# def intersection_multiple_lists(*lists):
#     return list(set.intersection(*map(set, lists)))
# print(intersection_multiple_lists([1,2,3],[2,3,4],[3,4,5]))




# # flatten a nested list:
# def flatten_list(nested_list):
#     return [item for sublist in nested_list for item in sublist]
# print(flatten_list([[1,2],[3,4],[5,6]]))




# Capitalize the first letter of each word in a sentence:
# def capitalize_word(sentence):
#     return sentence.title()
# print(capitalize_word("hello world python"))




# # find the frequency of words in a sentence:
# from collections import Counter
# def word_frequency(sentence):
#     words = sentence.split()
#     return dict(Counter(words))
# print(word_frequency("apple banana apple orange banana apple"))





# check if a string contian only digits:
# def is_only_digits(s):
#     return s.isdigit()
# print(is_only_digits("123456"))
# print(is_only_digits("1234wfwf"))




# replace all spaces in a string with a given char:
# def replace_spaces(s, char):
#     return s.replace(" ", char)
# print(replace_spaces("Hello World", "_"))




# Convert a list of integers to a single integer:
# def list_to_integer(list):
#     return int("".join(map(str,list)))
# print(list_to_integer([1,2,3,4,5]))





# Count the number of lowercase and uppercase letter in a string :
# def count_case(s):
#     lower = sum(1 for char in s if char.islower())
#     upper = sum(1 for char in s if char.isupper())
#     return lower, upper
# print(count_case("Hello World PYTHONS"))




# Check if two string are rotations of each other:
# def is_rotation(s1,s2):
#     return len(s1) == len(s2) and s1 in s2 + s2
# print(is_rotation("abcde", "deabc"))
# print(is_rotation("hello", "loleh"))




# count the number of substring in a string:
# def count_substring(s, sub):
#     return s.count(sub)
# print(count_substring("banana", "a"))






# 12th : find min and max value.
# list = [9,11,0,370,55,40,2]
# max = list[0]
# min = list[0]
# for i in list:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print("Max :",max)
# print("Min :",min)




# 13th : convert list into string.
# list = ['a','b','c']
# l = "".join(list)
# print(l)









# 15th : remove the duplicates.
# list = [1,1,1,2,2,3,3,4,5,6,6,7,8]
# print(set(list))



# 16th : intersection of two list.
# def intersect(list1,list2):
#     l1 = set(list1)
#     l2 = set(list2)
#     lists = l1.intersection(l2)
#     return list(lists)
# x = [1,9,3,0]
# y = [1,2,3,4]
# res = intersect(x,y)
# print(res)



# 17th : common numbers in two list.
# def ele(list1,list2):
#     common = []
#     count = 0
#     for i in list1:
#         for j in list2:
#             if(i == j):
#                 common.append(i)
#                 count = count + 1
#     print(common)
#     print(count)
# l1 = [2,4,5,6,7]
# l2 = [2,4,8,9,6]
# ele(l1,l2)




#18th : list convert into the dict.
# def list_to_dic():
#     keys = [1,2,3,4]
#     values = ["one","two","three","four"]
#     result = dict(zip(keys,values))
#     print(result)
# list_to_dic()




# 19th : insert and check value in list.
# list = ["kanpur","pulhrayan","lucknow","bhopal","indore"]
# print(list)

# list.insert(1,"banglour")
# print(list)

# if "orai" in list:
#     print("found")
# else:
#     print("not found")






# 20th : add element by append.
# list = ["kanpur","pulhrayan","lucknow","bhopal","indore"]
# print(list)
# list.append("sehore")
# print(list)



# # 21th : iterate the value by for loop.
# list = ["kanpur","pulhrayan","lucknow","bhopal","indore"]
# print(list)
# for i in list:
#     print(i)




# # 22th : fetch element using index number
# list = ["kanpur","pulhrayan","lucknow","bhopal","indore"]
# print(list)
# print(list[1])



# # 23th : remove all element.
# list = ["kanpur","pulhrayan","lucknow","bhopal","indore"]
# print(list)
# list.clear()
# print(list)

# 24th : remove by pop func.
# list = ["kanpur","pulhrayan","lucknow","bhopal","indore"]
# print(list)
# list.pop(4)
# print(list)
# list.remove("kanpur")
# print(list)



# # 25th : update
# list = ["kanpur","lucknow","bhopal","indore"]
# print(list)
# list[3] = "pune"
# print(list)



# 26th : access by slice
# list = ["kanpur","pulhrayan","lucknow","bhopal","indore"]
# print(list)
# print(list[0:])
# print(list[0::2])
# print(list[3])
# print(list[3], list[4])



# 27th  : add valaue in set.
# set = {10,20,30,40,50}
# set.add(60)
# print(set)



# 28th : remove from set.
# s1 = {10,20,30,40,50}
# s1.remove(50)
# print(s1)

# s1 = {1,2,3}
# s2 = {2,3,4}
# s3 = {3,4,5}
# s4 = s1.intersection(s2,s3)
# print(s4)




# 29th : symmetric_difference.
# s1 = {1,2,3}
# s2 = {2,3,4}
# s4 = s2.symmetric_difference(s1)
# print(s4)



# 30th : find min and max in the tuple.
# tuple = (10,20,30,40,50,60)
# print(tuple)
# print(max(tuple))
# print(min(tuple))




# 31th : concatenate.
# tuple1 = ("ronaldo","massi","neymar","maradona")
# print(tuple1)
# tuple2 = (10,20,30,40,50)
# print(tuple2)
# print(tuple1+tuple2)




# 32th : lenght of tuple.
# tuple = ("ronaldo", "messi", "neymar", "maradona")
# print(tuple)
# print(len(tuple))




# 33th : Range of indexing.
# tuple = ("ronaldo","mess","neymar")
# print(tuple)
# print(tuple[1:4])



# 34th : check existence of an item in tuple.
# tuple = ("ronaldo", "messi", "neymar", "maradona")
# if "aran" in tuple:
#     print("Found!")
# else:
#     print("Not Found!")




# 35th : Access values in  a tuple.
# tuple = ("ronaldo", "messi", "neymar", "maradona")
# print(tuple)
# print(tuple[0])
# print(tuple[1::])





# 36th : count occurance of the tuple.
# def pre(tup,ele):
#     return tup.count(ele)
# tuple1 = (1,2,3,2,2,4)
# print(pre(tuple1,1))




# 37th : remove element from a tuple.
# def pre(tup,ele):
#     l = list(tup)
#     l.remove(ele)
#     return tuple(l)
# tuple1 = (1,2,3,4)
# print(pre(tuple1,3))



# # 38th : find duplicate.
# def pre(tup):
#     seen = set()
#     duplicate = set()
#     for item in tup:
#         if item in seen:
#             duplicate.add(item)
#         else:
#             seen.add(item)
#     return tuple(duplicate)
# tuple1 = (1,1,2,2,3,4,5,5,6,6)
# print(pre(tuple1))





# 39th : sort the tuple.
# def pre(tup):
#     return tuple(sorted(tup))
# tuple1 = (5,6,8,3,2,1)
# print(pre(tuple1))




# 40th : print all keys and values from dict.
# dict = {"apple":10,"banana":5,"orange":4,"guava":6}
# print("Get dic keys :",dict.keys())
# print("Get dic value :",dict.values())
# print("Get dic items :",dict.items())

# print(dict.pop("banana"))
# print(dict)







# 41th : find the min and max value
# fruits = {"apple":10,"banana":5,"orange":4,"guava":6}
# print("min value key :",min(fruits))
# print("max value key :",max(fruits))




# 42th : function proggramming.
# sum = lambda a, b: a + b
# result = sum(3, 5)
# print(result)  # Output: 8



# 43th : sorting list.
# pairs = [(1,2),(3,1),(5,0),(2,3)]
# pairs.sort(key=lambda x:x[1])
# print(pairs)



# 44th : FIltering even numbers using lambda.
# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = list(filter(lambda x : x%2 == 0, numbers))
# print(even_numbers)





# 45th : multiply element of  list by 2 using lambda.
# numbers = [1,2,3,4,5]
# double_number = list(map(lambda x:x*2, numbers))
# print(double_number)





# 46th : factorial.
# factorial = lambda n:1 if n == 0 else n * factorial(n-1)
# print(factorial(5))




# 47th : sorting a list of string by lenght using.
# string = ["ronaldo", "messi", "neymar", "maradona"]
# string.sort(key = lambda x: len(x))
# print(string)





# 48th : remove all vowels.
# remove = lambda s: " ".join([char for char in s if char not in "aeuioAEUIO"])
# print(remove("kamni"))





# 49th : concatenate two list.
# list1 = [1,2,3]
# list2 = [3,4,5]
# concat_items = lambda l1, l2 : l1 + l2
# print(concat_items(list1,list2))




# 50th : check if a string contain only digits using lambda.
# is_digits = lambda s: s.isdigit()
# print(is_digits("12345"))
# print(is_digits("1234&5"))





# 51th : check string is palindrome.
# palindrome = lambda s: s== s[::-1]
# print(palindrome("madam"))
# print(palindrome("vikas"))





# 52th :find the product of two numbers.
# product = lambda x, y:x*y
# print(product(4,5))




# 53th : find the longest string.
# string = ["ronaldo", "messi", "neymar", "maradona"]
# longest_string = max(string,key=lambda x:len(x))
# print(longest_string)






# 54th : calculate the cube of each number using.
# numbers = [1,2,3,4,5]
# cubes = list(map(lambda x:x ** 3, numbers))
# print(cubes)




# 55th : check number is prime.
# is_prime = lambda n: all(n%i != 0 for i in range(2, int(n ** 0.5) + 1)) if n > 1 else False
# print(is_prime(7))
# print(is_prime(9))



# 56th : generate function, sum of all number in range.
# num = int(input("Enter a number :"))
# total = sum(x for x in range(1,num+1))
# print("Sum of num :", total)


# 57th: find the multiply of all even numbers.
# num = 4
# even = 1
# for x in (x for x in range(1,num+1)if x%2 == 0):
#     even *= x
# print(even)



# 58th : count divisible by 3.
# num = int(input("Enter a number :"))
# count = sum(1 for x in range(1,num+1) if x%3 == 0)
# print(count)




# 59th : filter palidrome words.
# words = ["madam","hello","racecar","level","world"]
# palindrome = (word for word in words if word == word[::-1])
# print(list(palindrome))




# # 60th : generate fibonacci numbers.
# def fibe(n):
#     a,b = 0,1
#     while a <= n:
#         yield a
#         a,b = b,a+b
# result = fibe(100)
# print(list(result))





# 61th : count vowels in a string.
# string = "hello world"
# vowels = sum(1 for char in string if char in "aeuioAEUIO")
# print(vowels)


# 62th : create dict from two list.
# keys = ['a','B','C']
# vowels = [1,2,3]
# result = {key : value for key,value in zip(keys,vowels)}
# print(result)




# 63th : find maximum value in a list of tuple.
# tuple = [(1,2),(3,4),(5,6),(7,8)]
# max_tuple = max((t for t in tuple), key=lambda x:x[1])
# print(max_tuple)





# 64th : count occurence of a char in a string.
# string = "abcaefnkfknrfknwadfmvn"
# char = sum(1 for char in string if char == "a")
# print(char)



# 65th : find the intersection.
# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
# intersection = (x for x in list1 if x in list2)
# print(list(intersection))




# 66th : List comprehension : square from 1 to 10.
# square = [x ** 2 for x in range(1,11)]
# print(square)



# 67th : even numbers 1 to 20.
# evens = [x for x in range(1,21) if x%2 == 0]
# print(evens)



# 68th : create a list of string in uppercase.
# words = ['hello','kamni','vikas','python']
# uppers = [word.upper() for word in words]
# print(uppers)




# 69th : lenght of each words in a list.
# words = ['apple', 'banana','chery','date']
# lenght = [len(word) for word in words]
# print(lenght)




# 70th : print the words longer that 4 char.
# words = ['cat','dog','elephant','giraffe','mouse']
# long_words = [word for word in words if len(word) > 4]
# print(long_words)





# 71th : reverse string.
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("vikas"))




# 72th : check for palindrome.
# def is_palindrome(s):
#     return s == s[::-1]
# print(is_palindrome("racecar"))
# print(is_palindrome("hello"))




# 73th : FizzBuzz.
# def fizzbuzz(n):
#     result = []
#     for i in range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append("fuzzBuzz")
#         elif i%3 == 0:
#             result.append("Fizz")
#         elif i%5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(str(i))
#     return result
# print(fizzbuzz(15))







# 74th : count the vowels in string.
# def count_vowels(s):
#     return sum(1 for char in s.lower() if char in 'aeuio')
# print(count_vowels("vikas"))





# # 75th : count occurence of a char in a string.
# def count_char_occu(s,char):
#     return s.count(char)
# print(count_char_occu("hello","l"))





# # 76th : find the union of two lists.
# def union(arr1,arr2):
#     return list(set(arr1) | set(arr2))
# print(union([1,2,3],[2,3,4]))



# 77th : find the duplicate char in a string.
# from collections import Counter
# def find_duplicates(s):
#     counter = Counter(s)
#     duplicates = {char: count for char, count in counter.items() if count > 1}
#     return duplicates
# s = "programming"
# print(find_duplicates(s))





# # 78th : check if two string are anagrams.
# def is_anagram(s1,s2):
#     return sorted(s1) == sorted(s2)
# s1 = "listen"
# s2 = "silent"
# print(is_anagram(s1,s2))



# 79th : find the non-repeating char.
# from collections import Counter
# def first_non_repeating(s):
#     counter = Counter(s)
#     for char in s:
#         if counter[char] == 1:
#             return char
#     return None
# s = "swiss"
# print(first_non_repeating(s))




# # 80th : count occurenceof a char in string.
# def count_char_occu(s,char):
#     return s.count(char)
# s = "banana"
# char = "a"
# print(count_char_occu(s,char))






# 81th : remove duplicate from a string.
# def remove_duplicate(s):
#     return " ".join(sorted(set(s), key=s.index))
# s = "banana"
# print(remove_duplicate(s))





# 82th : check if a string contain only digits.
# def is_digit_only(s):
#     return s.isdigit()
# s = "123445"
# print(is_digit_only(s))




# 83th : find the most frequent cahr in string.
# from collections import Counter
# def most_freuent_char(s):
#     counter = Counter(s)
#     return max(counter, key=counter.get)
# s = "banana"
# print(most_freuent_char(s))






# # 84th : one string is rotation of another.
# def is_rotation(s1,s2):
#     return len(s1) == len(s2) and s2 in (s1+s2)
# s1 = "waterbottle"
# s2 = "erbottlewat"
# print(is_rotation(s1,s2))






# 85th : remove the all occurence of char.
# def remove_char(s,char):
#     return s.replace(char, " ")
# s = "hello world"
# char = "o"
# print(remove_char(s,char))





# OOPS :
# 86th : create class car with attributes.
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def display_info(self):
#         print(f"Car make : {self.make}")
#         print(f"Car model : {self.model}")
#         print(f"Car year : {self.year}")
# obj = Car("Toyota","Corolla",2020)
# obj.display_info()





# 87th : create class and function to calculate the area, perimeter.
# class rectangle:
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
#     def area(self):
#         return self.lenght * self.lenght
#     def perimeter(self):
#         return 2 * (self.lenght + self.width)
# rect = rectangle(10,5)
# print(f"Area : {rect.area()}")
# print(f"Perimeter : {rect.perimeter()}")







# # 88th : create class bankaccount with functions.
# class bankaccount:
#     def __init__(self,balance = 0):
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"Depositd : {amount}")
#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"withdraw : {amount}")
#         else:
#             print("Insufficient funds")
#     def get_balance(self):
#         return self.balance
# account = bankaccount()
# account.deposit(500)
# account.withdraw(200)
# print(F"Current balance : {account.get_balance()}")





# 89th : Create a class date with attributes.
# class date:
#     def __init__(self,day,month,year):
#         self.day = day
#         self.month = month
#         self.year = year
#     def display_date(self):
#         print(f"{self.day:02d}/{self.month:02d}/{self.year}")
# obj = date(5,12,2024)
# obj.display_date()



# 90th : Multiple Inheritance.
# class A:
#     def displayA(self):
#         print("I am class A")
# class B:
#     def displayB(self):
#         print("I am class B")
# class C(A,B):
#     def displayC(self):
#         print("I am class C")
# obj = C()
# obj.displayA()
# obj.displayB()
# obj.displayC()




# 91th : Encapsulation.
# class pre:
#     __name = "prince"
#     def __init__(self):
#         print(self.__name)
# obj = pre()



# 92th : use the super function.
# class pre:
#     def display(self):
#         print("Welcome to python")
# class repre(pre):
#     def display(self):
#         super().display()
#         print("welcome to python1.0")
# obj = repre()
# obj.display()



# 93th : create a class by static method.
# class pre:
#     @staticmethod
#     def add(a,b):
#         return a + b
# result = pre.add(10,20)
# print(result)




# 94th : encapsulation create class with private attributes.
# class person:
#     def __init__(self,name):
#         self.name = name
#         self._age = 0
#     def set_age(self,age):
#         if age > 0:
#             self._age = age
#         else:
#             print("Age must be a positive number.")
#     def  get_age(self):
#         return self._age
# obj = person("prince")
# obj.set_age(25)
# print(obj.get_age())
# obj.set_age(-5)




# 101th : encapsulationn with class level.
# class student:
#     def __init__(self,name):
#         self.__name = name
#         self.__grade = 0
#     def set_grade(self,grade):
#         if 0 <= grade <= 100:
#             self.__grade = grade
#         else:
#             print("Grade must be between 0 and 100.")
#     def get_grade(self):
#         return self.__grade
# obj = student("Prince")
# obj.set_grade(85)
# print(obj.get_grade())
# obj.set_grade(110)




# # 102th : method inheritance with super() and parameters.
# class animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# class bird(animal):
#     def __init__(self, name, age, wing_span):
#         super().__init__(name, age)
#         self.wing_span = wing_span
#     def display_info(self):
#         print(f"name : {self.name}, age : {self.age}, wing_span : {self.wing_span} meters")
# obj = bird("Eagle", 3, 2.5)
# obj.display_info()





# 103th : multiple inheritance.
# class Engine:
#     def start(Self):
#         print("Engine started")
# class Transmission:
#     def shift(self):
#         print("Transmission shifted")
# class Car(Engine,Transmission):
#     def drive(self):
#         self.start()
#         self.shift()
#         print("Car is driving")
# obj = Car()
# obj.drive()






# 104th : Polymorphism with method overloading.
# class math:
#     def add(self,*args):
#         return sum(args)
# obj = math()
# print(obj.add(2,4))
# print(obj.add(2,4,6))



# # 105th : polymorphism with __str__ method.
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Person : {self.name}, Age : {self.age}"
# class Employee(person):
#     def __init__(self, name, age, job_title):
#         super().__init__(name, age)
#         self.job_title = job_title
#     def __str__(self):
#         return f"Employee  {self.name}, Age : {self.age}, job_title : {self.job_title}"
# obj = person("prince", 22)
# obj1 = Employee("bob",40,"manager")
# print(obj)
# print(obj1)




# 106th : override the sound.
# class animal:
#     def sound(self):
#         print("Animal makes a sound.")
# class dog(animal):
#     def sound(self):
#         print("Dog barks")
# class cat(animal):
#     def sound(self):
#         print("cat meows")
# obj = [dog(), cat()]
# for animal in obj:
#     animal.sound()




# 107th : create calculator class
# class calculator:
#     def add(self,a,b,c = 0):
#         return a+b+c
# obj = calculator()
# print(obj.add(5,4))
# print(obj.add(3,5,4))


# # 108th : abstract class
# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         pass
# class car(vehicle):
#     def move(self):
#         print("car is driving")

# class bicycle(vehicle):
#     def move(self):
#         print("bicycle is pedaling")
# obj = [car(),bicycle()]
# for vehicle in obj:
#     vehicle.move()



# # 109th : abstract class 
# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
# class triangle(shape):
#     def draw(self):
#         print("Drawing a triangle")
# class square(shape):
#     def draw(self):
#         print("Drawing a square")
# obj = triangle()
# obj1 = square()
# obj.draw()
# obj1.draw()





# 110th : Abstraction for a report generation system
# from abc import ABC, abstractmethod
# class report(ABC):
#     @abstractmethod
#     def generate_report(self):
#         pass
# class pdfreport(report):
#     def generate_report(self):
#         return "Generating pdf report"
# class excelreport(report):
#     def generate_report(self):
#         return "generating excel report"
# obj = pdfreport()
# obj1 = excelreport()
# print(obj.generate_report())
# print(obj1.generate_report())





# # 111th : method magic: __init__(self,..)
# class point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"point({self.x}, {self.y})"
# obj = point(3,4)
# print(obj)



# 112th : __str__(self)-string
# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def __str__(self):
#         return f"Circle with radius {self.radius}"
# obj = circle(5)
# print(obj)



# 113th : __add__(self,other)
# class vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __add__(self,other):
#         return vector(self.x+other.x, self.y + other.y)
#     def __repr__(self):
#         return f"vector ({self.x}, {self.y})"
    
# obj = vector(1,2)
# obj1 = vector(3,4)
# obj2 = obj + obj1
# print(obj2)




# # 114th : __getitem__(self,key)
# class matrix:
#     def __init__(self,data):
#         self.data = data
#     def __getitem__(self,index):
#         return self.data[index]

# obj = matrix([[1,2,3],[4,5,6],[7,8,9]])
# print(obj[1])
# print(obj[1][2])




# 115th : __contain__(self)
# class bag:
#     def __init__(self,items):
#         self.items = items
#     def __contains__(self,item):
#         return item in self.items
# obj = bag([1,2,3,4,5])
# print(3 in obj)
# print(6 in obj)



# # 116th : __iter__(self)
# class range:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
#         self.current = start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         self.current += 1
#         return self.current - 1
# obj = range(3,7)
# for num in obj:
#     print(num)



# 117th : __call__(self, ..)
# class multiplier:
#     def __init__(self,factor):
#         self.factor = factor
#     def __call__(self, number):
#         return number * self.factor
# obj = multiplier(2)
# print(obj(5))




# 118th : __del__(self)
# class box:
#     def __init__(self,items):
#         self.items = items
#     def __len__(self):
#         return len(self.items)
# obj = box([1,2,3,4])
# print(len(obj))



# 119th : __del__(self)
# class person:
#     def __init__(self,name):
#         self.name = name
#         print(f"{self.name} created")
#     def __del__(self):
#         print(f"{self.name} destroyed")
# obj = person("prince")
# del obj






# # 120th: Create a iterator for a list.
# number = [10,20,30,40,50,60,70,80]
# iterator = iter(number)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



# # 121th: create an iterator for a string.
# word = "AI"
# iterator = iter(word)
# print(next(iterator))
# print(next(iterator))



# 122th: iterator while loop and stopiteration.
# num = [1,2,3,4,5,6,7,8]
# it = iter(num)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break


# number = [10,20,30,40,50,60,70,80]
# for num in number:
#     print(num)


# str = "prince"
# for ch in str:
#     print(ch)


# class Evennumbers:
#     def __init__(self, limit):
#         self.num = 0
#         self.limit = limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.num += 2
#         if self.num <= self.limit:
#             return self.num
#         else:
#             raise StopIteration
# evens = Evennumbers(10)
# for e in evens:
#     print(e)




# # 123th: fibonacci Iterator.
# class Fibonacci:
#     def __init__(self,n):
#         self.a, self.b = 0,1
#         self.count = 0 
#         self.n = n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count < self.n:
#             result = self.a
#             self.a, self.b = self.b, self.a + self.b
#             self.count += 1
#             return result
#         else:
#             raise StopIteration
# for num in Fibonacci(7):
#     print(num)




# # 124th: use of generator: fibonacci.
# def fibonacci(n):
#     a,b = 0,1
#     for _ in range(n):
#         yield a
#         a,b = b, a+b
# for num in fibonacci(9):
#     print(num)




# # 125: Enven number.
# def even_numbers(limit):
#     for i in range(2 ,limit + 1,2):
#         yield i
# for e in even_numbers(10):
#     print(e)



# # 126th: Factorial Generator.
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#         yield fact
# for f in factorial(7):
#     print(f)




# # 127th: with out yield key.
# g = (x*x for x in range(5))
# for val in g:
#     print(val)