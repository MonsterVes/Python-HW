# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program which will ask the user to enter 3 names.
	The names, should be stored into a list 'names'.
    Create another list 'sorted_name' which will have names, sorted alphabetically. Do not change the original 'names' list.

    TIP: use list.sort() method to sort a list. Note, that the sort() method works "in-place",
"""

### Your code here
print(f"{' Name list sort ':-^70}")
print()

names = []

user_input_name1 = input("Enter 1st name: ")
names.append(user_input_name1)
user_input_name2 = input("Enter 2nd name: ")
names.append(user_input_name2)
user_input_name3 = input("Enter 3rd name: ")
names.append(user_input_name3)

sorted_name = names[:]
sorted_name.sort()
print(f"Originally entered names: {names}")
print(f"Sorted names: {sorted_name}")

print()


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

print(f"{' Palindrome check ':-^70}")
print()

user_input = input("Enter a word: ")
user_input_list = list(user_input.lower())
reverse_input = user_input_list[:]
reverse_input.reverse()
if user_input_list == reverse_input:
    print (f"The word '{user_input}' is a palindrome")
else:
    print (f"The word '{user_input}' is not a palindrome")

print()



### EXPECTED OUTPUT:
# Enter a word : Racecar
# The word 'Racecar' is a palindrome

# Enter a word : car
# The word 'car' is not a palindrome