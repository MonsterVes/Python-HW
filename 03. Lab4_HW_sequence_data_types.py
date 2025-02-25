# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter three numbers: start, stop, and step.
    Create a range object using these values and convert it to a list named 'numbers'.

    TIP: Use the range(start, stop, step) function and list() to convert it to a list.
"""

### Your code here
# print(f"{' Start, stop, and step ':-^70}")
# print()

# start = int(input("Enter start: "))
# stop = int(input("Enter stop: "))
# step = int(input("Enter step: "))

# numbers = list(range(start, stop, step))
# print(f"Generated list: {numbers}")

# print()

### EXPECTED OUTPUT:
# Enter start: 2
# Enter stop: 10
# Enter step: 2
# Generated list: [2, 4, 6, 8]

# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a list of numbers separated by spaces.
    Then, ask for two indices 'start' and 'end' to slice the list.
    Create a new list 'sliced_list' containing elements from 'start' to 'end' (excluding 'end').

    TIP: Use list slicing syntax list[start:end] to extract a sublist.
"""

### Your code here
""" NOT WORKING

print(f"{' Slice the list ':-^70}")
print()

list_of_numbers = input("Enter numbers separated by spaces: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

converted_list = int(list_of_numbers.replace(" ",""))
sliced_list= converted_list[start:end]

print(sliced_list)
"""

### EXPECTED OUTPUT:
# Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9
# Enter start index: 2
# Enter end index: 6 
# Sliced list: [3, 4, 5, 6]

# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Write a program that generates a list of numbers from 1 to 50 using range().
    Then, create a new list 'evens' that contains only the even numbers from this list using slicing.

    TIP: Use range(start, stop) to create the initial list.
        Use slicing with a step to extract every second element.
"""

### Your code here

# print(f"{' Slice even numbers ':-^70}")
# print()

# numbers = list(range(1,51))
# print(numbers)
# even_numbers = numbers[1:51:2]
# print(even_numbers)

## EXPECTED OUTPUT:
# Original list: [1, 2, 3, ..., 50]
# Even numbers: [2, 4, 6, ..., 50]

# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Write a program that generates a list of numbers from 100 to 50 (inclusive), counting down by 5.
    Then, create a new list 'first_half' that contains only the first half of this list using slicing.

    TIP: Use range(start, stop, step) to create the initial list.
        Use slicing to extract the first half.
"""

### Your code here
# print(f"{' Countdown by 5 ':-^70}")
# print()

# generated_list = list(range(100,49,-5))
# half = round(len(generated_list)/2)
# half_list = generated_list[:half]
# print(f"Original list: {generated_list}")
# print(f"First half: {half_list}")

# print()

### EXPECTED OUTPUT:
# Original list: [100, 95, 90, ..., 50]
# First half: [100, 95, 90, ..., 75]

# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a word.
    Create a new string 'reversed_word' that contains the word in reverse order using slicing.

    TIP: Use slicing with a negative step to reverse a string.
"""

### Your code here
# print(f"{' Reverse word ':-^70}")
# print()

# word = input("Enter a word: ")
# word_len = len(word)
# reversed_word = word[::-1]
# print(reversed_word)

# print()

### EXPECTED OUTPUT:
# Enter a word: Python
# Reversed word: nohtyP

# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
    Write a program that generates a list of numbers from 10 to 100 with a step of 10.
    Then, create a new list 'middle_part' containing all elements except the first and last two using slicing.

    TIP: Use range(start, stop, step) to create the initial list.
         Use slicing to remove the first and last two elements.
"""

### Your code here
# print(f"{' 10 to 100 with a step of 10 without the first and last two ':-^70}")
# print()

# numbers = list(range(10,101,10))
# lenght = len(numbers)-2
# middle_part = numbers[2:lenght]
# print(middle_part)

# print()

### EXPECTED OUTPUT:
# Original list: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Middle part: [30, 40, 50, 60, 70, 80]

# ---------------------------------- Task 7 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a sentence.
    Create a new string 'every_second_char' that contains every second character from the sentence using slicing.

    TIP: Use slicing with a step to extract every second character.
"""

### Your code here

# print(f"{' Every second char ':-^70}")
# print()

# sentence = input("Enter a sentence: ")
# print(f"Every second character: {sentence[::2]}")

# print()

### EXPECTED OUTPUT:
# Enter a sentence: Python slicing is powerful!
# Every second character: Pto lcn spwru!


# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program which will ask the user to enter 3 names.
	The names, should be stored into a list 'names'.
    Create another list 'sorted_name' which will have names, sorted alphabetically. Do not change the original 'names' list.

    TIP: use list.sort() method to sort a list. Note, that the sort() method works "in-place",
"""

### Your code here
# print(f"{' Name list sort ':-^70}")
# print()

# names = []

# user_input_name1 = input("Enter 1st name: ")
# names.append(user_input_name1)
# user_input_name2 = input("Enter 2nd name: ")
# names.append(user_input_name2)
# user_input_name3 = input("Enter 3rd name: ")
# names.append(user_input_name3)

# sorted_name = names[:]
# sorted_name.sort()
# print(f"Originally entered names: {names}")
# print(f"Sorted names: {sorted_name}")

# print()


### EXPECTED OUTPUT:
# Enter 1st name: Maria
# Enter 2d name: Ivan
# Enter 3d name: Asen

# Originally entered names:  ['Maria', 'Ivan', 'Asen']
# Sorted names: ['Asen', 'Ivan', 'Maria']


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a word and then checks if the word is a palindrome.
    A palindrome is a word that reads the same forward and backward, ignoring case.

    Tip: you can use str.lower() to convert a string to lowercase
"""

### Your code here

# print(f"{' Palindrome check ':-^70}")
# print()

# user_input = input("Enter a word: ")
# user_input_list = list(user_input.lower())
# reverse_input = user_input_list[:]
# reverse_input.reverse()
# if user_input_list == reverse_input:
#     print (f"The word '{user_input}' is a palindrome")
# else:
#     print (f"The word '{user_input}' is not a palindrome")

# print()



### EXPECTED OUTPUT:
# Enter a word : Racecar
# The word 'Racecar' is a palindrome

# Enter a word : car
# The word 'car' is not a palindrome