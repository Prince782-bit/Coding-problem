# # do variables ka value swap kro without third variable.
# a = 10 
# b = 20
# a, b = b, a
# print("a =",a, "b =",b)



# # # number even hai ya odd check kro.
# num = 7
# if num%2 == 0:
#     print("Even")
# else:
#     print("Odd")



# # 3 numbers me sabse bada number find kro.
# a = 15
# b = 25
# c = 10
# if a >= b and a >= c:
#     print("Largest =",a)
# elif b>=a and b >= c:
#     print("Largest =",b)
# else:
#     print("Largest =",c)



# # Reverse a string.
# text = "python"
# rev = text[::-1]
# print("Reverse string:", rev)



# # string palindrome hai yai nhi check kro.
# text = "madam"
# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")




# # string me vowels count kro.
# text = "education"
# count = 0
# for ch in text:
#     if ch in "aeiuoAEUIO":
#         count += 1
# print("Vowel count =",count)




# # Factorial of a number.
# num = 5
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print("Factorial =", fact)



# check prime hai ya nhi check kro.
# num = 11
# is_prime = True
# if num <= 1:
#     is_prime = False
# else:
#     for i in range(2, num):
#         if num%i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print("Prime number")
# else: 
#     print("Not prime number")



# # first n fibonacci numbers print kro.
# n = 7
# a = 0
# b = 1
# for i in range(n):
#     print(a, end= " ")
#     a, b = b, a + b



# # ek number ke digits ke sum nikalo.
# num = 1234
# sum_digits = 0
# while num > 0:
#     digit = num % 10
#     sum_digits += digit
#     num = num // 10
# print("Sum of digits =", sum_digits)



# # reverse the number.
# num = 1234
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# print("Reversed number =", rev)





# # number armstrong hai ya nhi check kro.
# num = 153
# temp = num
# sum_val = 0
# while temp > 0:
#     digit = temp%10
#     sum_val += digit ** 3
#     temp = temp // 10
# if sum_val == num:
#     print("Armstrong number")
# else:
#     print("Not armstrong number")





# # list me duplicate elements find kro.
# nums = [1,2,3,2,4,5,1]
# duplicates = []
# for i in nums:
#     if nums.count(i) > 1 and i not in duplicates:
#         duplicates.append(i)
# print("duplicates =", duplicates)




# # list se duplicate remove kro.
# nums = [1,2,2,3,4,4,5]
# unique = []
# for i in nums:
#     if i not in unique:
#         unique.append(i)
# print("unique list =", unique)




# # List ka second largest number find kro.
# nums = [10,20,4,45,99]
# largest = second = nums[0]
# for i in nums:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i < second and i != largest:
#         second = i
# print("second largest =", second)




# # list ko ascending order me sort kro without using built-in sort.
# num = [5,2,8,1,3]
# for i in range(len(num)):
#     for j in range(i + 1, len(num)):
#         if num[i] > num[j]:
#             num[i], num[j] = num[j], num[i]
# print("sorted list =",num)




# # string me har char kitni baar aaya, count kro.
# text = "hello"
# freg = {}
# for ch in text:
#     if ch in freg:
#         freg[ch] += 1
#     else:
#         freg[ch] = 1
# print(freg)




# # do lists ke common elements find kro.
# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# common = []
# for i in list1:
#     if i in list2 and i not in common:
#         common.append(i)
# print("Common elements =", common)



# # do strings anagram hain ya nhi check kro.
# s1 = "listen"
# s2 = "silent"
# if sorted(s1) == sorted(s2):
#     print("Anagram")



# # 2 numbers par basic operation kro.
# a = 10
# b = 5
# print("Add =", a+b)
# print("Sub =", a-b)
# print("Mul =",a * b)
# print("Divi =",a / b)



# # year leap year hai ya nhi check kro.
# year = 2024
# if(year%4 == 0 and year%100 != 0) or (year%400 == 0):
#     print("leap year")
# else:
#     print("not a loop year")



# # string me total words count kro.
# text = "I am learning python"
# words = text.split()
# print("Total words =",len(words))




# # string se spaces remove kro.
# text = "hello world python"
# result = ""
# for ch in text:
#     if ch != " ":
#         result += ch
# print("Without spaces:", result)




# # string me uppercase aur lowercase count kro.
# text = "PyTHon"
# upper = 0
# lower = 0
# for ch in text:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
# print("Uppercase =", upper)
# print("Lowercase =", lower)




# # list ka smallest number find kro.
# num = [12,5,8,1,15]
# smallest = num[0]
# for i in num:
#     if i < smallest:
#         smallest = i
# print("Smallest =",smallest)




# # list ke sabhi elements ka total sum nikalo.
# num = [10,20,30,40]
# total = 0
# for i in num:
#     total += i
# print("Sum =", total)



# # list ke sabhi elements ka multiplication nikalo.
# num = [2,3,4]
# result = 1
# for i in num:
#     result *= i
# print("Multiplication =",result)




# # string ki length find kro without using len().
# text = "python"
# count = 0
# for ch in text:
#     count += 1
# print("Length =", count)




# # list ki length find kro without using len().
# num = [10,20,30,40,50]
# count = 0
# for i in num:
#     count += 1
# print("Length of list =", count)




# # perfect number hai ya nhi check kro.
# num = 28
# sum_div = 0
# for i in range(1, num):
#     if num%i == 0:
#         sum_div += i
# if sum_div == num:
#     print("Perfect number")
# else:
#     print("Not perfect number")





# # number ke sare factors print kro.
# num = 12
# print("factors are:")
# for i in range(1, num + 1):
#     if num%i == 0:
#         print(i, end=" ")




# # number positive, negative ya zero hai check kro.
# num = -5
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")




# # celsius ko fahrenheit me convert kro.
# celsius = 25
# fahreheit = (celsius * 9/5) + 32
# print("Fahreheit =", fahreheit)





# # char vowel hai ya consonat check kro.
# ch = "e"
# if ch in "aeuioAEUIO":
#     print("Vowel")
# else:
#     print("consonant")




# # kisi number ka table print kro.
# num = 5
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)




# # char ka ASCII value find kro.
# ch = "A"
# print("ASCII Value =", ord(ch))




# # string me shirf digit hai ya nhi check kro.
# text = "12345"
# if text.isdigit():
#     print("Only digits")
# else:
#     print("Not only digits")




# # string me ek char replace kro.
# text = "banana"
# new_text = ""
# for ch in text:
#     if ch == "a":
#         new_text += "o"
#     else:
#         new_text += ch
# print("Updated string =", new_text)





# # list me kisi element ka index find kro.
# num = [10,20,30,40]
# target = 30
# for i in range(len(num)):
#     if num[i] == target:
#         print("Index =", i)
#         break




# # do lists ko merge kro.
# list1 = [1,2,3]
# list2 = [4,5,6]
# merged = list1 + list2
# print("Mergef list :",merged)








# # create and print dict.
# student = {
#     "name": "prince",
#     "age": 21,
#     "course": "Btech"
# }
# print(student)




# # Access value from dict.
# student = {
#     "name": "prince",
#     "age":31,
#     "course": "Btech"
# }
# print("Name:", student["name"])
# print("Age:",student["age"])





# # add new kay_value pair in dict.
# student = {
#     "name":"prince",
#     "age": 21
# }
# student["city"] = "delhi"
# print(student)




# # update dict value.
# student = {
#     "name":"prince",
#     "age": 21
# }
# student["age"] = 22
# print(student)



# # loop through dict.
# student = {
#     "name":"prince",
#     "age":21,
#     "course":"Btech"
# }
# for key, value in student.items():
#     print(key, ":",value)





# # count frequency of element in list using dict.
# num = [1,2,2,3,1,4,2]
# freq = {}
# for i in num:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)





# # find char frequency in string using dict.
# text = "hello"
# freq = {}
# for ch in text:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq)





# # acces tuple element.
# colors = ("red","green","blue")
# print(colors[0])
# print(colors[1])




# # count element in tuple.
# num = (1,2,3,2,4,2)
# print("Count of 2:",num.count(2))



# # find index in tuple.
# num = (10,20,30,40)
# print("Index of 30:",num.index(30))



# # convert list into tuple.
# num = [1,2,3,4]
# result = tuple(num)
# print(result)



# # create and print set.
# num = {1,2,3,4,5}
# print(num)



# # remove duplicate using set.
# nums = [1,2,2,3,4,4,5]
# unique = list(set(nums))
# print("Unique :",unique)




# # common element using set.
# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# common = set(list1) & set(list2)
# print("Common:",common)



# # union of two sets.
# set1 = {1,2,3}
# set2 = {3,4,5}
# print("union :", set1 | set2)



#  intersection of two set.
# set1 = {1,2,3}
# set2 = {3,4,5}
# print("intersection :", set1 & set2)



# # difference of two sets.
# set1 = {1,2,3}
# set2 = {3,4,5}
# print("difference :", set1 - set2)





# # find missing numbers in sequence.
# num = [1,2,3,5,6]
# n = 6
# expect_sum = n*(n+1)//2
# actual_sum = 0
# for i in num:
#     actual_sum += i
# missing = expect_sum - actual_sum
# print("missing number:",missing) 















# # function banao jo 2 numbers ka add kro.
# def add(a, b):
#     return a + b
# result = add(10,20)
# print("Sum :",result)




# # function ke through evem/odd check kro.
# def check_even_odd(num):
#     if num%2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(check_even_odd(9))





# # function se 3 numbers me largest find kro.
# def largest(a,b,c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print("Largest :", largest(12,45,22))




# # function banao jo string reverse kre.
# def revese_string(text):
#     return text[::-1]
# print(revese_string("python"))




# # function ke through palindrome check kro.
# def is_palindrome(text):
#     return text == text[::-1]
# print(is_palindrome("madam"))




# # true/false nhi, proper message do.
# def is_palindrome(text):
#     if text == text[::-1]:
#         return "Palindrome"
#     else:
#         return "Not palindrome"
# print(is_palindrome("madam"))




# # string me total char count kro.
# text = "hello"
# count = 0
# for ch in text:
#     count += 1
# print("Char :", count)




# # string me kisi specific char ko count kro.
# text = "banana"
# target = "a"
# count = 0
# for ch in text:
#     if ch == target:
#         count += 1
# print("count =",count)




# # string ka first non-repeating char find kro.
# text = "aabbcddee"
# for ch in text:
#     if text.count(ch) == 1:
#         print("First non-repeating char :", ch)
#         break




# # string se duplicate char remove kro.
# text = "programming"
# result = ""
# for ch in text:
#     if ch not in result:
#         result += ch
# print("Without duplicates :", result)




# # list me kitne even aur odd number hai count kre.
# nums = [1,2,3,4,5,6]
# even = 0
# odd = 0
# for i in nums:
#     if i%2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even:",even)
# print("Odd:", odd)




# # list se positive aur negative numbers alag kro.
# num = [10,-2,5,-7,-1]
# positive = []
# negative = []
# for i in num:
#     if i >= 0:
#         positive.append(i)
#     else:
#         negative.append(i)
# print("positive :",positive)
# print("negative:", negative)





# # find the sum of even numbers in list.
# nums = [1,2,3,4,5,6]
# sum_even = 0
# for i in nums:
#     if i%2 == 0:
#         sum_even += i
# print("sum of even numbers:",sum_even)





# # find the sum of odd number.
# num = [1,2,3,4,5,6]
# sum_odd = 0
# for i in num:
#     if i%2 != 0:
#         sum_odd += i
# print("Sum of odd number:",sum_odd)




# # check if element exists in list.
# num = [10,20,30,40]
# target = 20
# if target in num:
#     print("element found")
# else:
#     print("element not found")





# # print star pattern square.
# for i in range(4):
#     for j in range(4):
#         print("*", end=" ")
#     print()




# # print star pattern right triangle.
# for i in range(1,6):
#     for j in range(i):
#         print("*", end=" ")
#     print()





# # print number pattern.
# for i in range(1,6):
#     for j in range(1, i + 1):
#         print(j , end = " ")
#     print()




# # print reverse star pattern.
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end= " ")
#     print()

 


# # print reverse number pattern.
# for i in range(5,0,-1):
#     for j in range(1, i + 1):
#         print(j , end = " ")
#     print()