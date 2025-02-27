# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes an integer n and prints a triangle pattern of stars (*). The number of stars in the first line is 1, in the second line is 2, and so on up to n stars in the n-th line.
"""

### Your code here

# user_input= int(input("Enter number of rows: "))
# for n in range(1,user_input+1):
#     print("*"*n)

# ------------------- Pyramid ------------------- #
    
# user_input= int(input("Enter number of rows: "))

# for n in range(user_input):
#     print(" "*(user_input-1)+"*"*(n+1)+"*"*n)
#     user_input -= 1


### EXPECTED OUTPUT:
# Enter stars number: 4
# *
# **
# ***
# ****


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a script that prompts the user to enter words, one at a time.
    The user should continue to enter words until they enter '0'.
    After the user enters '0', the script should display all the words that start with a vowel (a, e, i, o, u).
"""

### Your code

# words_with_vowels = []

# while True:
#     user_input = input("Enter a word (or '0' to stop): ").lower()
#     if user_input != "0":
#         if user_input[0] in ("a", "e", "i", "o", "u"):
#             words_with_vowels.append(user_input)
#     else:
#         print(f"Words that start with a vowel: {words_with_vowels}")
#         break
    
    
    
        

### EXPECTED OUTPUT:
# Enter a word (or '0' to stop): atom
# Enter a word (or '0' to stop): see
# Enter a word (or '0' to stop): end
# Enter a word (or '0' to stop): 0
# Words that start with a vowel: ['atom', 'end']


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Write a script that takes a list of strings and returns a dictionary,
    where each key is a string length and each value is a list of strings of that length.
"""

### Given:
words = ["hello", "world", "python", "is", "fun", "and", "useful"]

### Your code here

# d = {len(count):[word for word in words if len(word) == len(count)] for count in words }
# print(d)

### EXPECTED OUTPUT:
# {5: ['hello', 'world'], 6: ['python'], 2: ['is'], 3: ['fun', 'and'], 7: ['useful']}


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    In a supermarket inventory system, there are two sets of product categories:
    1. Categories that need refrigeration.
    2. Categories on sale this week.

    Write a script, which performs the following tasks:
    a. Find and print the categories that are both refrigerated and on sale.
    b. Find and print categories that are on sale but do not require refrigeration.
    c. Suggest new sale categories from the refrigerated items which are not yet on sale.

    Note: The category names are assumed to be in lowercase.
"""

### Given
refrigerated = {'dairy', 'meats', 'frozen foods', 'seafood', 'deli'}
sale = {'cereals', 'dairy', 'snacks', 'frozen foods', 'beverages'}

#USING SETS

# ref_and_sale = refrigerated.intersection(sale)
# sale_no_ref = sale - ref_and_sale
# new_sale_cat = refrigerated - sale

# print(f"Categories both refrigerated and on sale: {ref_and_sale}")
# print(f"Sale categories not needing refrigeration: {sale_no_ref}")
# print(f"Suggested new sale categories from refrigerated items: {new_sale_cat}")

# USING COMPREHENSION

# ref_and_sale = {r for r in refrigerated if r in sale}
# sale_no_ref = {r for r in sale if r not in refrigerated}
# new_sale_cat = {r for r in refrigerated if r not in sale}

# print(f"Categories both refrigerated and on sale: {ref_and_sale}")
# print(f"Sale categories not needing refrigeration: {sale_no_ref}")
# print(f"Suggested new sale categories from refrigerated items: {new_sale_cat}")

### Your code here

### EXPECTED OUTPUT:
# Categories both refrigerated and on sale: {'dairy', 'frozen foods'}
# Sale categories not needing refrigeration: {'snacks', 'beverages', 'cereals'}
# Suggested new sale categories from refrigerated items: {'seafood', 'deli', 'meats'}