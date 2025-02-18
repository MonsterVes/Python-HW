
# ---------------------------------- Task 1 ---------------------------------- #
### Description:
#  Alice is 30 years old and her favorite color is black. Your task is to
#  store that information into variables and to print a greeting from Alice in
#  the console "Hello, my name is Alice, I am 30 years old, and my favorite color is black"
#  using the variables.

### Given:
name = 'Alice'
age = 30
color = 'black'

### Your code here
print(f"{' Task 1 ':-^70}")
print()
print(f"Hello, my name is {name}, I am {age} years old, and my favorite color is {color}.")
print()

### Expected output
# Hello, my name is Alice, I am 30 years old, and my favorite color is black.

# ---------------------------------- Task 2 ---------------------------------- #
### Description:
#  Create two numeric variables representing the year Alice was born and the current year.
#  Calculate Alice's age using these variables and an f-string, then print the result.

### Given:
birth_year = 1993
current_year = 2025

### Your code here
print(f"{' Task 2 ':-^70}")
print()
print(f"Alice is {current_year - birth_year} years old.")
print()

### Expected output
# Alice is 30 years old.

# ---------------------------------- Task 3 ---------------------------------- #
### Description:
#  Format the following number 1234567.89 to be displayed as a currency with two decimal places.
#  Example: "$1,234,567.89". Use an f-string to format and print the result.

### Given:
amount = 1234567.89

### Your code here
print(f"{' Task 3 ':-^70}")
print()
print(f"${amount:,}")
print()

### Expected output
# $1,234,567.89

# ---------------------------------- Task 4 ---------------------------------- #
### Description:
#  Create a simple receipt format for the given shopping list items.
#  Use f-strings to format each item name aligned to the left and its price
#  aligned to the right. Each line should be 30 characters wide.

### Given:
item1_name = "Milk"
item1_price = 1.99

item2_name = "Bread"
item2_price = 2.49

item3_name = "Eggs"
item3_price = 3.59

total = item1_price + item2_price + item3_price

### Your code here
print(f"{' Task 4 ':-^70}")
print()
print(f"{item1_name:<26}{item1_price}")
print(f"{item2_name:<26}{item2_price}")
print(f"{item3_name:<26}{item3_price}")
print(f"{'-':-^30}")
print(f"{'Total: ':<{30-len(str(total))}}{total}")
print()

### Expected output
# Milk                           1.99
# Bread                          2.49
# Eggs                           3.59

# ---------------------------------- Task 5 ---------------------------------- #
### Description:
#  Alice is participating in a running marathon. She ran 42.195 kilometers in 3 hours, 45 minutes, and 30 seconds.
#  Calculate her average pace (minutes per kilometer) and total time in hours and print them using f-strings.
#  Format the pace to two decimal places.

### Given:
distance_km = 42.195
hours = 3
minutes = 45
seconds = 30

### Your code here

print(f"{' Task 5 ':-^70}")
print()
pace = (hours*60 + minutes + seconds/60/60)/distance_km
total_time_in_hours = hours + minutes/60 + seconds/60/60
print (f"Alice's pace: {pace:.2f} minutes/km")
print (f"Total time: {total_time_in_hours:.2f} hours")
print()

### Expected output
# Alice's pace: 5.33 minutes/km
# Total time: 3.75 hours

