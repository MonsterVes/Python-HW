# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Write a function named 'calculate_area' that takes two parameters (length and width)
and returns the area of a rectangle.
"""

### Your code here

# def calcualte_area(lenght, width):
#     return lenght*width

# print(calcualte_area(5, 10))

### EXPECTED OUTPUT:
# calculate_area(10, 5) should return 50


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a function 'is_even' that takes a single integer argument and returns True
if the number is even, and False otherwise.
"""

### Your code here
# def is_even(number):
#     if number%2==0:
#         return True
#     else:
#         return False
    
# print(is_even(4))
# print(is_even(5))

### EXPECTED OUTPUT:
# is_even(4) should return True
# is_even(5) should return False




# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Write a function named 'multiply_elements' that takes a list of integers and returns the product of all the elements in the list.
"""


### YOUR CODE HERE

# def multiply_elements(elements):
#     result = 1
#     for num in elements:
#         result*=num
#     return result

# print(multiply_elements([2, 3, 4]))


### TEST:
# print(multiply_elements([2, 3, 4]))

### EXPECTED OUTPUT:
# 24


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a function 'count_vowels' that takes a string and returns the count of vowels (a, e, i, o, u) in the string.
"""


### YOUR CODE HERE

# def count_vowels(string):
#     total_count = 0
#     for letter in string.lower():
#         if letter in ("a", "e", "i", "o", "u"):
#             total_count += 1
#     return total_count

# print(count_vowels("hello"))
# print(count_vowels("world"))

### TEST:
# print(count_vowels("hello"))
# print(count_vowels("world"))

### EXPECTED OUTPUT:
# 2
# 1


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'reverse_string' that takes a string and returns the string reversed.
"""

### YOUR CODE HERE

# def reverse_string(string):
#     reversed = string[::-1]
#     return reversed
# print(reverse_string("hello"))

### TEST:
# print(reverse_string("hello"))

### EXPECTED OUTPUT:
# "olleh"


# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
Write a function 'find_max' that takes a list of numbers and returns the largest number in the list.
"""


### YOUR CODE HERE

# def find_max(list_of_numbers):
#     max_number = max(list_of_numbers)
#     return max_number

# print(find_max([1, 3, 2, 8, 5]))

### TEST:
# print(find_max([1, 3, 2, 8, 5]))

### EXPECTED OUTPUT:
# 8


# ---------------------------------- Task 7 ---------------------------------- #
""" DESCRIPTION:
Create a function 'remove_duplicates' that takes a list and removes duplicate elements, returning a new list with unique elements.
"""


### YOUR CODE HERE

# def remove_duplicates(list_of_elements):
#     unique_elements_set = set(list_of_elements)
#     unique_elements_list = list(unique_elements_set)
#     return unique_elements_list

# print(remove_duplicates([1, 2, 2, 3, 4, 3]))

### TEST:
# print(remove_duplicates([1, 2, 2, 3, 4, 3]))

### EXPECTED OUTPUT:
# [1, 2, 3, 4]


# ---------------------------------- Task 8 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'is_palindrome' that checks if a given string is a palindrome.
"""

### YOUR CODE HERE

# def is_palindrome(string):
#     reversed = string[::-1]
#     if string == reversed:
#         return True
#     else:
#         return False
    
# print(is_palindrome("madam"))
# print(is_palindrome("hello"))    

### TEST:
# print(is_palindrome("madam"))
# print(is_palindrome("hello"))

### EXPECTED OUTPUT:
# True
# False

# ---------------------------------- Task 9 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'add' that takes two arguments and returns their sum.
"""

### Your code here

# add = lambda x, y: x+y

# print(add(2,3))

### EXPECTED OUTPUT:
# add(2, 3) should return 5


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Write a function named 'convert_temperature' that takes two parameters:
a temperature and the unit ('C' for Celsius, 'F' for Fahrenheit).
The function should convert the temperature to the other unit and return it.
"""

### Your code here

# def convert_temperature(temp, unit):
#     if unit == "C":
#         return (temp*9/5) +32
#     elif unit == "F":
#         return (temp-32)*5/9

# print(convert_temperature(32,"C"))
# print(convert_temperature(89.6,"F"))

### EXPECTED OUTPUT:
# convert_temperature(32, 'C') should return 89.6 (Fahrenheit)
# convert_temperature(89.6, 'F') should return 32 (Celsius)


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Create a function 'filter_words' that takes a list of words and a minimum length, and
returns a list of words that are longer than the given minimum length.
"""

### Your code here

# def filter_words(list_of_words, min_len):
#     new_list = []
#     for word in list_of_words:
#         if len(word) > min_len:
#             new_list.append(word)
#     return new_list

# print(filter_words(["apple", "pear", "banana", "cherry"], 5))

### EXPECTED OUTPUT:
# filter_words(["apple", "pear", "banana", "cherry"], 5) should return ['banana', 'cherry']


# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
Write a lambda expression 'sort_by_last_letter' that sorts a list of strings based on
the last letter of each string. Use this lambda expression to sort a given list,
using the sorted() built-in function.
"""

### Your code here

# def sort_by_last_letter (list_of_str):
#     return sorted(list_of_str,key = lambda str: str[-1])


# print(sort_by_last_letter(["cherry", "banana", "apple" ]))

### EXPECTED OUTPUT:
# sort_by_last_letter(["banana", "apple", "cherry"]) should return ['banana', 'apple', 'cherry']