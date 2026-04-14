

# Check if a list id sorted:
# lst = [1,2,3,4,5]
# print(lst == sorted(lst))



# Find the missing number in list:
# nums = [1,3,4,5]
# missing = sum(range(1,6)) - sum(nums)
# print(missing)




# FInd the intersection of two list:
# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# common = list(set(list1) & set(list2))
# print(common)



# Find the longest word in a sentence :
# s = "python is an amazing programming language"
# longest = max(s.split(), key=len)
# print(longest)



# Find the factorial :
# num = 5
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(fact)



# Find the sum of digits of a number:
# num = 1234
# sum_digits = sum(int(digit) for digit in str(num))
# print(sum_digits)




# Remove the space without using replace():
# s = "Hello World"
# s_no_space = "".join(c for c in s if c != " ")
# print(s_no_space)



# Find the n-th fibonacci number:
# n = 10
# a,b = 0,1
# for _ in range(n - 1):
#     a,b = b,a + b
# print(b)



# Count the number of words in a string:
# s = "python is awesome"
# count = len(s.split())
# print(count)



# Find the sum of the first n natural number:
# n = 10
# sum_n = n * (n + 1) // 2
# print(sum_n)



# Write a python function to check if a given string is a palindrome or not. ++
# def is_palindrome(string):
#     return string == string[::-1]

# print(is_palindrome("madam"))
# print(is_palindrome("vikas"))








# Write a python program to sort a list of integers in ascending order.
# my_list = [3,1,8,22,15]
# my_list.sort()
# print(my_list)









# Write a python program to find the factorial of the given number.++
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
    
# print(factorial(5))










# Write a program to find the greatest comman divisor(GCD) of two numbers.
# def gcd(num1, num2):
#     if num2 == 0:
#         return num1
#     else:
#         return gcd(num2, num1 % num2)

# print(gcd(12, 4))









# Write a python program to check if a given number is prime or not.++
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(11))
# print(is_prime(4))









# Write a python program to find the second largest number in list.
# my_list = [3,5,1,8,2]
# my_list.sort()
# print(my_list)
# print(my_list[-2])
# print(my_list[-1])
# print(my_list[0])






# Write a python program to generate a random passward of a given length.++
# import random 
# import string

# def generate_password(lenght):
#     password = ''.join(random.choices(string.ascii_letters + string.digits, k=lenght))
#     return password
# print(generate_password(4))

 








# Write a python program to count the number of vowels in a gives string.++
# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for i in string:
#         if i in vowels:
#             count += 1
#     return count

# print(count_vowels("vikas"))









# Write a python program to print the vowels from the gives string.++
# str = input("enter the string :")
# for i in str:
#     if i in "aeiou":
#         print(i, end=" ")








# Write a python program to reverse a given list.++
# my_list = [1,2,3,4,5,6,7,8]
# my_list.reverse()
# print(my_list)



# Write a python program to find the sum of all the multiples of 3 or 5 below given number.
# def sum_multiples(num):
#     sum = 0
#     for i in range(num):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#     return sum

# print(sum_multiples(10))



# Generate Random num of float:
# gives a random float number between 0 and 1
# import random
# num = random.random()
# print(num)



# gives a random flaot number in specified range.
# num = random.uniform(1, 100)
# print(num)



# num = random.randint(1, 100)
# print(num)


# num = random.randrange(0, 100, 2)
# print(num)



# numlist = random.sample(range(0, 100), 3)
# print(numlist)






# print the fibonacci series:++
# num = int(input("Enter any number :"))
# n1, n2 = 0, 1
# sum = 0
# if num <= 0:
#     print("Please enter number greater than 0")
# else:
#     for i in range(0, num):
#         print(sum, end=" ")
#         n1 = n2
#         n2 = sum
#         sum = n1 + n2




# Given two arrays, write a python function to return the interseection of the two?
# for example, x = [1,5,9,0] and y = [3,0,2,9] it should return [9,0].

# def intesect_arr(arr1, arr2):
#     set1 = set(arr1)
#     set2 = set(arr2)

#     sets = set1.intersection(set2)
#     return list(sets)

# x = [1,5,0,9]
# y = [3,0,2,9]
# res = intesect_arr(x,y)
# print(res)






# compute square roots of any number: real number.
# num = float(input("Enter a number: "))

# sqr = num ** 0.5
# print("The square of %0.3f is %0.3f" %(num, sqr))





# Access element of the list:
# list  = [1,2,3,4,5,6,7]
# x = list[3]
# print("First element :",x)





# Convert string to int using single line of code:
# a = "5"
# print(int(a))




# convert a string to a list:
# s = "where are you going"
# print(s.split(" ")) 






# Check for leap year:
# year = int(input("Enter a year : "))
# if(year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))

# elif(year % 4 == 0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))

# else:
#     print("{0} is not a leap year".format(year)) 









# Swap 2 variables: second method.
# x = 5 
# y = 10
# x, y = y, x

# print("The value of x after swapping", x)
# print("The value of y after swapping", y)






# def is_palindrome(string):
#     return string == string[::-1]

# print(is_palindrome("madam"))
# print(is_palindrome("vikas"))








# find the factorial number : +++
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
    
# print(factorial(5))








# Check the number is prime or not: ++
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(11))
# print(is_prime(4))







# Write a python program to count the number of vowels in a gives string.
# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for i in string:
#         if i in vowels:
#             count += 1
#     return count

# print(count_vowels("vikas"))




# Generate an infinite fibonnacci seriesby using the generators:
# def fibonacci():
#     a,b, =0,1
#     while True:
#         yield a
#         a,b=b,a+b

# f1 = fibonacci()
# print(next(f1)) 
# print(next(f1))     
# print(next(f1))     
# print(next(f1))     
# print(next(f1))     
# print(next(f1))     
# print(next(f1))         
    





# Sort without using the keyword
# list1 = [42,2,12,6,45,7,22,5,1,19]
# n = len(list1)

# for i in range(n):
#     for j in range(i+1,n):
#         if list1[i] > list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]
# print(list1)







# Write a code to check the whether a string is palindrome or not:
# s = input("enter the string : ")
# if s == s[::-1]:
#     print("Yes Palindrome")
# else:
#     print("No")



# Alternative way :
# s = "madam"
# n = len(s)
# x = 0
# for i in range(n):
#     if s[i] != s[n-i-1]:
#         x = 1
#         break


# if x == 0:
#     print("Yes Palindrome")
# else:
#     print("No")







# sort a particular dictionary or sort a particular dictionary by using a dictionary comprehension:
# dict1 = {575: "Apple", 876: "Mango",
#         132: "Grapes", 782: "Banana"}
# d=  sorted(dict1.keys())
# dict2 = {}
# for i in d:
#     dict2[i] = dict1[i]

# print(dict2)






# sort a dictionary by values:
# dict1 = {575: "Apple", 876: "Mango", 132: "Graphes", 782: "Banana"}
# dict2 = {key:value for key, value in sorted(dict1.items(), key = lambda x: x[1])}
# print(dict2) 






# Print all the pair with given sum:
# list1 = [8,7,2,5,3,1]
# n = len(list1)
# k = 10

# for i in range(n):
#     for j in range(i+1, n):
#         if (list1[i]+list1[j]) == k:
#             print(list1[i], list1[j])










# FIbonnacci using the recursion :
# def recur_fib(n):
#     if n <= 1:
#         return n
#     else:
#         return(recur_fib(n-1) + recur_fib(n-2))
# nterms = int(input("How many terms : "))
# if nterms <= 0:
#     print("Please enter a positive integer")
# else:
#     for i in range(nterms):
#         print(recur_fib(i))





 
# find the output 
# intput = "the sky is blue"
# output = "blue is sky the"

# s = "the sky is blue"
# l = s.split()
# l = l[::-1]
# l = " ".join(l)
# print(s)
# print(l)











# find the max repeatted charcter in a string without having on2 complexity:
# s = "kmaninininirfskmankm"
# ch = {}
# for i in s:
#     if i in ch:
#         ch[i] += 1
#     else:
#         ch[i] = 1

# print(ch)

# max_char = max(ch, key = ch.get)
# print(max_char)




# Check the number is prime or not : +++
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(110))
# print(is_prime(22))









# Find the factorial of the numbers: +++
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num -1)
# print(factorial(5))






# Generate Random num of float: +++
# gives a random float number between 0 and 1
# import random
# num = random.random()
# print(num)

# gives a random flaot number in specified range.
# num = random.uniform(1, 100)
# print(num)

# num = random.randint(1, 100)
# print(num)

# num = random.randrange(0, 100, 2)
# print(num)

# numlist = random.sample(range(0, 100), 3)
# print(numlist)





# FIbonnacci using the recursion :
# def recur_fib(n):
#     if n <= 1:
#         return n
#     else:
#         return(recur_fib(n-1) + recur_fib(n-2))
# nterms = int(input("How many terms : "))
# if nterms <= 0:
#     print("Please enter a positive integer")
# else:
#     for i in range(nterms):
#         print(recur_fib(i))


  


# Write a program to print prime numbers between 100 and 200. ++
# for num in range(100,200):
#     if all(num%i != 0 for i in range(2, num)):
#         print(num)




# write a sort function to sort the element in a list: ++
# l = [13,45,67,9,90,1,2,5,90]
# l.sort(reverse = False)
# print(l)









# write a sorting function without using the list.sort function (descending order)
# data_list = [13,45,67,9,90,1,2,5,900]
# new_list = []

# while data_list:
#     min = data_list[0]
#     for x in data_list:
#         if x > min:
#             min = x
#     new_list.append(min)
#     data_list.remove(min)
# print(new_list)






# write a proram to print fibonacci series: +++
# def f(n):
#     if n == 0 : 
#         return 0
#     elif n == 1:
#         return 1
#     else: 
#         return f(n-1) +f (n-2)
    
# for i in range(0,12):
#     print(f(i))










# Write a program to print a list in reverse :
# li = [13,45,67,9,90,1,2,5,900]
# li.reverse()
# print(li)








# Write a program to check the string is a palidrome or not: ++++
# def is_palindrome(string):
#     return string == string[::-1]

# print(is_palindrome("madam"))







# write a program to print set of duplicates in a list: ++
# l = [1,1,1,33,3,33,3,4,4,4,55,5,9,5,9,6,7,1]
# print(set([x for x in l if l.count(x) > 1]))





# Docstring are declared using '''triple single quotes'''. :
# def myfunction():
#     '''Docstring triple double quotes
#     docstring and does not nothing really.'''

#     return None
# print(myfunction.__doc__)





# dict and list comprehension : 
# x = [i for i in range(10)]
# print(x)

# x = [i for i in range(10) if (i>5)]
# print(x)




# convert list into a string:
# list  = ['a', 'b', 'c']
# l = " ".join(list)
# print(l)



# Find out the commom letters between two strings
# def common_letters():
#     str1 = input("Enter the first string: ")
#     str2 = input("Enter the second string: ")
#     s1 = set(str1)
#     s2 = set(str2)
#     l = s1 & s2
#     print(l)

# common_letters()





#remove the duplicate char.
# def common_letters():
#     str1 = input("Enter the first string: ")
#     s1 = set(str1)
#     l = s1 
#     print(l)

# common_letters()




# # Reverse String:
# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("kamni"))




# # Check for Palindrome:
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("racecar"))
# print(is_palindrome("hello"))





# # FizzBuzz:
# def fizzbuzz(n):
#     result = []
#     for i in range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append("FuzzBuzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#         elif i % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(str(i))
#     return result

# print(fizzbuzz(15))




# Count Vowels in a string :
# def count_vowels(s):
#     return sum(1 for char in s.lower() if char in 'aeiou')

# print(count_vowels("kamni"))






# Fibonacci sequence: return the nth fibonacci number.
# def fibonacci(n):
#     a,b = 0, 1
#     for _ in range(n):
#         a,b = b,a+b
#     return a

# print(fibonacci(10))




# Merge two sorted list: 
# def merge_sorted_lists(list1,list2):
#     return sorted(list1+list2)

# print(merge_sorted_lists([1,3,5],[2,4,6]))






# # Check for Anagrams:
# def are_anagrams(s1,s2):
#     return sorted(s1) == sorted(s2)

# print(are_anagrams("listen", "silent"))
# print(are_anagrams("hello", "world"))





# Remove the Duplicate from the list:
# def remove_duplicates(lst):
#     return list(set(lst))

# print(remove_duplicates([1,2,3,2,4,4,5,6,6]))






# # Find the factorial of a number:
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)


# print(factorial(5))




# # Find the maximum element in a list:
# def find_max(lst):
#     return max(lst)

# print(find_max([1,2,3,4,5]))



# # handle exception:
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")






# # Check if a number is prime:
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
        
#     return True

# print(is_prime(7))
# print(is_prime(10))




# Sum of digit in a number:
# def sum_of_digits(n):
#     return sum(int(digit) for digit in str(n))

# print(sum_of_digits(1234))





# COunt Occurrence of a character in a string :
# def count_char_occurrences(s, char):
#     return s.count(char)

# print(count_char_occurrences("hello","l"))





# Find the intersection of two list:
# def intersection(list1,list2):
#     return list(set(list1) & set(list2))
# print(intersection([1,2,3,4],[3,4,5,6]))










# # Find the second largest element in a list:
# def second_largest(arr: list):
#     arr.sort()
#     return arr[-2]


# print(second_largest([1,3,2,5,4]))





# # Fibonacci series: generate fibonacci series up to n terms.
# def fibonacci(n):
#     fib = [0,1]
#     for i in range(2, n):
#         fib.append(fib[i-1] + fib[i-2])
#     return fib

# print(fibonacci(7))




# # Find the missing number in an array: 
# def find_missing(arr):
#     n = len(arr) + 1
#     total_sum = n * (n+1)//2
#     return total_sum - sum(arr)

# print(find_missing([1,2,4,5,6]))






# # Find the common element between two lists:
# def common_element(list1, list2):
#     return list(set(list1) & set(list2))

# print(common_element([1,2,3,4],[3,4,5,6]))




# find the length of a string without using len():
# def string_lenght(s):
#     count = 0
#     for char in s:
#         count += 1
#     return count

# print(string_lenght("kamni"))





# # Find the first non-repeating character:
# def first_non_repeating_char(s):
#     for char in s:
#         if s.count(char) == 1:
#             return char
#     return None

# print(first_non_repeating_char("swiss"))





# Find all permutations of a string:
# from itertools import permutations
# def string_permutations(s):
#     return [''.join(p) for p in permutations(s)]

# print(string_permutations("abc"))




 
# Find the minimum element in a list:
# def min_element(arr):
#     return min(arr)
# print(min_element([1,3,2,5,4]))




# Check for an even number:
# def is_prime(n):
#     return n%2 == 0
# print(is_prime(4))




# Generate all subsets of a set:
# def subsets(nums):
#     result = [[]]
#     for num in nums:
#         result += [curr + [num] for curr in result]
#     return result
    
# print(subsets([1,2,3]))




# # Find the mode(most frequent element):
# from collections import Counter
# def find_mode(arr):
#     Count = Counter(arr)
#     return Count.most_common(1)[0][0]
# print(find_mode([1,2,3,3,4,5,5,5,5,6,6,6,6,6,6]))





# # Find the union of two lists:
# def union(arr1, arr2):
#     return list(set(arr1) | set(arr2))

# print(union([1,2,3],[2,3,4]))





# # FInd the least common multiple(LCM):
# import math
# def lcm(a, b):
#     return abs(a * b)// math.gcd(a,b)
# print(lcm(4,5))








# # Find the greatest common divisor:
# import math
# def gcd(a,b):
#     return math.gcd(a,b)

# print(gcd(24, 36))




# Check if a string contains only digits:
# def is_digit(s):
#     return s.isdigit()

# print(is_digit("123354"))





 # FInd the union of the two list:
# def union(arr1, arr2):
#     return list(set(arr1)|set(arr2))
# print(union([1,2,3], [3,4,5]))



# # Count the occurance in the string:
# def count(s, char):
#     return s.count(char)
# print(count("vikkkkasss","k"))




# count the vowels in string:
# def count(s):
#     return sum(1 for char in s.lower() if char in 'aeiou')
# print(count("vikassaa"))





# create the FIZZBUZZ:
# def fizzbuzz(n):
#     result = []
#     for i in range(1, n+1):
#         if i%3 == 0 and i%5 == 0:
#             result.append("FizzBuzz")
#         elif i%5 == 0:
#             result.append("Fizz")
#         elif i%3 == 0:
#             result.append("Buzz")
#         else:
#             result.append(str(i))
#     return result
# print(fizzbuzz(15))







# Check the palindrome:
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))



# Reverse String:
# def reverse(s):
#     return s[::-1]
# print(reverse("kamni"))





# Print the words longer than 4 char:
# worls = ['cat','dog','elephant','giraffe','mouse']
# long_words = [word for word in worls if len(word)>4]
# print(long_words)





# Length of each words in a list:
# words = ['apple','banana','vikas','date']
# lenght = [len(word) for word in words]
# print(lenght)




# Create a list of string in uppercase:
# words = ['hello','kamni','vikas','python']
# upper = [word.upper() for word in words]
# print(upper)



# Even number 1 to 20:
# even = [x for x in range(1,21) if x%2 == 0]
# print(even)



# List comprehension : square from the 1 to 10:
# square = [x ** 2 for x in range(1,11)]
# print(square)



# Find the intersection of two list :
# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
# intersection = (x for x in list1 if x in list2)
# print(list(intersection))



# Count the occurance of a char in a string :
# string = "abcabcabcabc"
# char = sum(1 for char in string if char == 'a')
# print(char)


# Remove the duplicate from the list :
# num = [1,2,2,3,3,4,4,5,5]
# unique = (x for i, x in enumerate(num) if x not in num[:i])
# print(list(unique))



# Find the maximum value in a list of tuple:
# tuple = [(1,2), (3,4), (5,6), (7,8)]
# max_tuple = max((t for t in tuple), key=lambda x: x[1])
# print(max_tuple)



# # create dict from the two list :
# keys = ['a','b','c']
# values = [1,2,3]
# result = {key:value for key, value in zip(keys, values)}
# print(result)





# count the vowels in string:
# string = "hello vikas"
# vowels = sum(1 for char in string if char in "aeiouAEUIO")
# print(vowels)





# Generate the fibinacci numbers:
# def febo(n):
#     a, b = 0 ,1
#     while a <= n:
#         yield a
#         a, b = b, a+b

# result = febo(100)
# print(list(result))




# Count divisible by 3:
# num = int(input("Enter a number: "))
# count = sum(1 for x in range(1, num+1)if x%3 == 0)
# print(count)




# Calculate the cube of each number using lambda :
# numbers = [1,2,3,4,5]
# cube = list(map(lambda x: x**3, numbers))
# print(cube)



# sum of all number in range :
# num = int(input("Enter a num : "))
# total = sum(x for x in range(1,num+1))
# print("sum of num : ", total)




# Find the multiply of all even numbers :
# num = 5
# even = 1
# for x in (x for x in range(1,num+1) if x%2 == 0):
#     even *= x

# print(even)








# Swapping numbers :
# num1 = 10
# num2 = 20

# print("Value of num1 before swapping :", num1)
# print("Value of num2 before swapping :", num2)
# num1,num2=num2,num1
# print("Value of num1 after the swapping : ", num1)
# print("Value of num1 after the swapping : ", num2)





# Check the number is prime or not :
# num = 6
# count = 0
# if num > 1:
#     for i in range(1, num+1):
#         if (num%i) == 0:
#           count = count + 1
#     if count == 2:
#        print("Number is prime")
#     else:
#        print("Number is not prime") 





# Remove all occurence of char:
# def remove_char(s,char):
#    return s.replace(char, "")
# s = "hello world"
# char = "o"
# print(remove_char(s,char))


# One string is rotation of another :
# def is_rotation(s1,s2):
#    return  len(s1) == len(s2) and s2 in (s1+s2)
# s1 = "waterbottle"
# s2 = "erbottlewat"
# print(is_rotation(s1,s2))



# Find the most frequent char in string :
# from collections import Counter
# def most_frequent_char(s):
#    counter = Counter(s)
#    return max(counter, key=counter.get)
# s = "banananaaannnnn"
# print(most_frequent_char(s))



# Check if a string contain only digits :
# def is_digit_only(s):
#    return s.isdigit()

# s = "12345"
# print(is_digit_only(s))





# Remove duplicate from the string :
# def remove_duplicate(s):
#    return "".join(sorted(set(s), key=s.index))
# s = "banana"
# print(remove_duplicate(s))


# Count occurences of a char in string : 
# def count_char_occur(s, char):
#    return s.count(char)
# s = "banana khaogi kaaamnia"
# char = "a"
# print(count_char_occur(s,char))


# # Find the duplicates char in a string : 
# from collections import Counter
# def find_duplicates(s):
#    counter = Counter(s)
#    duplicates = {char: count for char, count in counter.items() if count > 1}
#    return duplicates
# s = "programming"
# print(find_duplicates(s))


# Check two string are anagram : 
# def is_anagram(s1,s2):
#    return sorted(s1) == sorted(s2)

# s1 = "listen"
# s2 = "silent"
# print(is_anagram(s1,s2))







# monkey fetching : 
# class test:
#     def __init__(self, x):
#         self.a=x
#     def get_data(self):
#         print("Some code to fetch data from database.")
#     def f1(self):
#         self.get_data()
#     def f2(self):
#         self.get_data()

# t1 = test(5)
# # t1.f1()
# # t1.f2()

# def new_get_data(self):
#     print("Some code to fetch data from test data")
# test.get_data=new_get_data
# print("Alter Monkey patchnig")
# t1.f1()
# t1.f2()







# def isPrime(num):
#     for i in range(2, num):
#         if num%i==0:
#             return False
#     return True

# def primeGenerator(n):
#     num=2
#     while n:
#         if isPrime(num):
#             yield num

#             n-=1
#         num+=1
#     return 

# it = primeGenerator(10)
# for e in it:
#     print(e,end=' ')






# l1 = [10,23.4,3+4,'abc',True,40]
# print(l1)
# t2 = []
# for e in l1:
#     if type(e) == float:
#         t2.append(e)

# print(t2)







# ASSERT statement: syntax = assert condition, "optional error message"
# imp note : assert is mainly used during development and testing, not in production.
# x = -10 
# assert x > 0, "x must be positive"
# print("x is positive")


# Using assert in a function:
# def divide(a,b):
#     assert b != 0, "Division by zero not allowed"
#     return a / b
# print(divide(10,2))
# print(divide(10,0))









# Yield keyword : is used in function to turn it into a generator . instead of returning a single value and exiting like return, yield pauses
# the function, saves it state, and can resume later.
# Why use it : to create iterators without writing a class, to generate large sequences effiently(memory friendly). useful in lazy evaluation.


# Simlple generator with yield :
# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# # Using the generator:
# for num in count_up_to(4):
#     print(num)



# how it work : yield return a value, the function remembers it state and continues from the same place when called again.
# USING next():
# def my_gen():
#     yield "Hello"
#     yield "Prince"
# gen = my_gen()
# print(next(gen))
# print(next(gen))








# SUPER() FUNCTION : is used to call a method from the parent class in a child class. it is commonly used in inhertance to reuse methods 
# or constructors.

# Calling parent constructor using super() :
# class Parent:
#     def __init__(self):
#         print("Parent constructor")
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor")
# c = Child()


# Using super in method overriding :
# class Animal:
#     def speak(self):
#         print("Animal speaks")
# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print("Dog barks")
# d = Dog()
# d.speak()







# Global keyword : use case = to modify a global variable inside a function, to share data across multiple function.
# Without global(error):
# x = 10
# def update():
#     x = x + 5 # error: local variable referenced before assignment.
#     print(x)
# update()



# # with gllobal correct :
# x = 10
# def update():
#     global x
#     x = x + 5
#     print("Inside function:", x)
# update()
# print("Outside function:", x)


# Declaring and uding a global variable inside a function:
# def create_global():
#     global y
#     y = 100
# create_global()
# print("Global y:", y)


# 1
# str = "interview"
# vowels = "aeiou"
# count = 0
# for ch in str:
#     if ch in vowels:
#         count += 1
# print(count)


# 2
# nums = [1,2,3,3,4,4,5]
# uniquie = list(set(nums))
# print(uniquie)


# 3
# str = "python"
# freq = {}
# for ch in str:
#     freq[ch] = freq.get(ch,0)+1
# print(freq)


# 4
# n = 7
# for i in range(2,n):
#     if n%i == 0:
#         print("Not prime")
#         break
# else:
#     print("prime")


# 5
# num = 5
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# print(fact)



# 6
# n = 5
# a,b = 0,1
# for i in range(n):
#     print(a,end=" ")
#     a,b = b, a+b


# 7
# nums = [1,2,3,4,5,6]
# even = [x for x in nums if x%2 == 0]
# print(even)



# str = "python"
# count = 0
# for _ in str:
#     count += 1
# print(count)



# s1 = "listen"
# s2 = "silent"
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")



# problem 1: Reverse a string 
# def reverse_string(s):
#     return s[::-1]

# text = "Python"
# print("Reversed String : ", reverse_string(text))
# [::-1] is slicing that reverses the string.



# problem 2: Check if a number is prime
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# n = 7
# print(f"{n} is prime:", is_prime(n))
# A prime number has only two factor: 1 and itself.




# problem 3: Find the largest element in a list.
# def find_largest(lst):
#     return max(lst)
# number = [12, 45, 23, 67, 34]
# print("Largest number: ", find_largest(number))
# The built-in function maX() return the maximum value from a list.



# problem 4: Check for palindrome
# def is_palindrome(s):
#     s = s.lower().replace(" ", "")
#     return s == s[::-1]
# word = "madam"
# print(f"{word} is palindrome:", is_palindrome(word))
# we compare the string with its reverse.




# problem 5: COnvert frequency of element in a list
# def count_frequency(lst):
#     freq = {}
#     for item in lst:
#         freq[item] = freq.get(item, 0) + 1
#     return freq
# items = ["apple", "banana","apple", "orange","banana", "apple"]
# print("Frequency:", count_frequency(items))
# we use a dictionary to store each element and its counts.





# problem 6: Fibonacci series
# def fibonacci(n):
#     a, b = 0, 1 
#     for _ in range(n):
#         print(a, end = " ")
#         a, b = b, a + b
# fibonacci(7)
# Each item is the sum of the previous two items.




# problem 7: Factorial Using recursion
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print("Factorial of 5:", factorial(5))
# Factorial(n) = n * factorial(n - 1) untill n = 1.




# problem 8: Check if two string are anagrams
# def are_anarams(str1,str2):
#     return sorted(str1.lower()) == sorted(str2.lower())
# print(are_anarams("listen", "silent"))
# two string are anagrams if thier sorted versions are identical.



# problem 9: Find second largest number in a list.
# def second_largest(nums):
#     first = second = float("-inf")
#     for n in nums:
#         if n > first:
#             second = first
#             first = n
#         elif first > n > second:
#             second = n
#     return second
# numbers = [10,20,4,45,99]
# print("Second largest:", second_largest(numbers))




# problem 10: count vowels in a string.
# def count_vowels(s):
#     vowels = "aeiouAEUIO"
#     count = sum(1 for char in s if char in vowels)
#     return count
# text = "Data Analysis with python"
# print("Vowels count:", count_vowels(text))
# We check each char and count if it a vowel.




# problem 11: Check Armstrong Number
# def is_armstrong(num):
#     temp = num
#     sum_ = 0
#     digits = len(str(num))
#     while temp > 0:
#         digit = temp % 10
#         sum_ += digit ** digits
#         temp //= 10
#     return sum_ == num
# n = 153
# print(f"{n} is Armstrong:", is_armstrong(n))





# problem 12: Remove duplicates from a list
# def remove_duplicates(lst):
#     seen = []
#     for i in lst:
#         if i not in seen:
#             seen.append(i)
#     return seen
# numbers = [1,2,2,3,4,4,5]
# print("After removing duplicates:", remove_duplicates(numbers))




# problem 13: Find missing number in a list.
# def find_missing(nums):
#     n = len(nums) + 1
#     total = n * (n + 1) // 2
#     return total - sum(nums)
# nums = [1,2,3,5]
# print("Missing number:", find_missing(nums))




# problem 14: Find all pairs with a given sum
# def find_pairs(nums, target):
#     pairs = []
#     seen = set()
#     for num in nums:
#         diff = target - num
#         if diff in seen:
#             pairs.append((diff, num))
#         seen.add(num)
#     return pairs
# nums = [2,4,3,5,7,8,9]
# target = 10
# print("Pair with sum 10:", find_pairs(nums, target))





# problem 15: Find longest word in a sentence.
# def longest_word(sentence):
#     words = sentence.split()
#     return max(words, key=len)
# sentence = "Data Analysis with python is powerful"
# print("Longest word:", longest_word(sentence))



# problem 16: sum of all elements in a list.
# def sum_list(lst):
#     return sum(lst)
# numbers = [10,20,30,40,50]
# print("Sum of list:", sum_list(numbers))



# problem 17: Even or odd number.
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "odd"
# n = 15
# print(f"{n} is", check_even_odd(n))



# problem 18: Find the largest of three numbers
# def largest_of(a,b,c):
#     if a >= b and a >= c:
#         return a 
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print("Largest number:", largest_of(25,45,10))




# problem 19: count digit in number.
# def count(num):
#     return len(str(num))
# print("Number of digits:", count(498543))



# problem 20: print mutliplication table.
# def multi(n):
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")
# multi(5)