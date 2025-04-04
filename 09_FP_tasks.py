# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Given is a list celsius_temps = [0, 30, 100] with Celsius temperatures.
Write a function, which will convert all temperatures in the list from Celsius to Fahrenheit.
The formula for conversion is: Fahrenheit = (Celsius * 9/5) + 32
This task should help you practice with map for transformation purposes.
"""
### GIVEN:
# celsius_temps = [0, 30, 100]

# ### YOUR CODE HERE

# def conver_C_to_F(list_of_temps):
#     return map(lambda temp: (temp*9/5) + 32, list_of_temps)

# print(list(conver_C_to_F(celsius_temps)))

### EXPECTED OUTPUT:
# [32.0, 86.0, 212.0]


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Given is a list with users data. Write a function which will return a list of all user names, for those users who have positive balance.
This task should help you practice with map and filter function for transformation/filtering purposes.
"""

### GIVEN:
users = [
    {'name':'Maria', 'balance': 2000},
    {'name':'Petar', 'balance': -189},
    {'name':'Ivan', 'balance': 3200},
    {'name':'Asen', 'balance': -2890},
]

### YOUR CODE HERE

# def find_positive_balance_users(user_dict):
#     positive_balance = filter(lambda users: users["balance"]>0, users)
#     names_with_positive_balance = map(lambda users: users["name"], positive_balance)
#     return names_with_positive_balance

# print(list(find_positive_balance_users(users))) 


### EXPECTED OUTPUT:
# ['Maria', 'Ivan']

# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Given is a list of Douglas Adams quotes. Write a function which will output in the console only the words that starts with letter 't' and are longer than 3 symbols. For simplicity, assume that words a space separated tokens.
This task should help you practice with map and filter function for transformation/filtering purposes.
"""

### GIVEN:
quotes = [
    'Nothing travels faster than the speed of light, with the possible exception of bad news, which obeys its own special laws',
    'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.'
]

### YOUR CODE HERE
def filter_words(text):
    quotes = map(lambda quote: quote.split(" "), text)
    # filtered_words = [word for word in quotes if word.startswith("t") and len(word)>3]

    # filtered = filter(lambda word: word.startswith("t"), quotes)
    return quotes

    # return [word for word in quotes if word.startswith("t") and len(word)>3]
    
   
#     for quote in text:
#         filtered = [word for word in quote.split(" ") if word.startswith("t") and len(word)>3]

    
print(list(filter_words(quotes)))



### EXPECTED OUTPUT:
# [['travels', 'than'], ['that', 'trying']]



# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Given the list of Douglas Adams quotes, write a function that finds the total number of words across all quotes. For simplicity, 
assume that words are space-separated tokens. Use the reduce function to accumulate the total count.
This task should help you practice using map and reduce for aggregation purposes.
"""

### GIVEN:
quotes = [
    'Nothing travels faster than the speed of light, with the possible exception of bad news, which obeys its own special laws',
    'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.'
]

### YOUR CODE HERE

### EXPECTED OUTPUT:
# [21, 21]


