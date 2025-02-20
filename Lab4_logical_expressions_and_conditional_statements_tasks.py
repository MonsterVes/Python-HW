# logical_expressions_and_conditional_statements_tasks.py

# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes a number as input and checks if it is positive, negative, or zero.
"""

### Your code here

print(f"{' Positive, negative, or zero ':-^70}")
print()

user_input = float(input("Enter a number: "))
if user_input<0:
    print(f"Number {user_input} is negative.") 
elif user_input==0:
    print(f"Number {user_input} is zero")   
else:
    print(f"Number {user_input} is positive.")

print()

### EXPECTED OUTPUT:
# "Enter a number: -2.45"
# "Number -2.45 is negative."


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program to check whether a year input by the user is a leap year or not. Use the rule for Gregorian calendar:
    Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
    For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
"""

### Your code here
print(f"{' Leap year ':-^70}")
print()

user_input = int(input("Enter a year: "))
if user_input%100==0 and user_input%400==0:
    print(f"{user_input} is a leap year")  
elif user_input%4==0 and user_input%100!=0:
    print(f"{user_input} is a leap year")   
else:
    print(f"{user_input} is NOT a leap year") 

print()

### EXPECTED OUTPUT:
# Enter a year: 2024
# 2024 is a leap year

# Enter a year: 2050
# 2050 is not leap year.


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Develop a simple temperature converter program that converts temperatures from Fahrenheit to Celsius and vice versa based on user choice. Make a user-friendly interface as given in EXPECTED OUTPUT:.

    Temperature conversions use the following formulas:
    Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
    Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
"""

### Your code here

print(f"{' Temperature converter ':-^70}")
print()

print(f"{' Fahrenheit/Celsius Converter ':*^50}")
print(f"{'# 1 => Convert to Fahrenheit':<48} #")
print(f"{'# 2 => Convert to Celsius':<48} #")
print('*'*50)

user_input_format = int(input("Enter your choice [1/2]: "))
if user_input_format == 1:
    cel_to_far_convert = float(input("Enter temperature in C: "))
    print(f"{cel_to_far_convert} C = {(cel_to_far_convert*9/5)+32:.2f} F")
elif user_input_format == 2:
    far_to_cel_convert = float(input("Enter temperature in F: "))
    print(f"{far_to_cel_convert} F = {(far_to_cel_convert-32)*5/9:.2f} C")
else:
    print("Not a valid choice.")
   
print()

### EXPECTED OUTPUT:
# **********Fahrenheit/Celsius Converter ***********
# # 1 => Convert to Fahrenheit                     #
# # 2 => Convert to Celsius                        #
# **************************************************
# Enter your choice [1/2]: 1
# Enter temperature in C: 20
# 20.0C = 68.0F


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Write a Body mass index (BMI) calculator program, which asks the user for:
    weight in kilograms
    height in meters

    Calculate the BMI = W / (H*H)
    where:
    W = weight in kilograms
    H = height in meters

    Display to the user the BMI and basic category, using next table:

    | ------------------------------- | ----------- |
    | category                        | BMI         |
    | ------------------------------- | ----------- |
    | Underweight (Severe thinness)   | < 16.0      |
    | Underweight (Moderate thinness) | 16.0 - 16.9 |
    | Underweight (Mild thinness)     | 17.0 - 18.4 |
    | Normal range                    | 18.5 - 24.9 |
    | Overweight (Pre-obese)          | 25.0 - 29.9 |
    | Obese (Class I)                 | 30.0 - 34.9 |
    | Obese (Class II)                | 35.0 - 39.9 |
    | Obese (Class III)               | ≥ 40.0      |
    | ------------------------------- | ----------- |
"""

### Your code here
print(f"{' BMI ':-^70}")
print()

user_weight = float(input("Enter weight in kilograms: "))
user_height = float(input("Enter height in meters: "))
BMI = round(user_weight/(user_height*user_height),2)

if BMI < 16:
    print(f"Your BMI = {BMI}, Category: Underweight (Severe thinness)")
elif BMI < 17:
    print(f"Your BMI = {BMI}, Category: Underweight (Moderate thinness)")
elif BMI < 18.5:
    print(f"Your BMI = {BMI}, Category: Underweight (Mild thinness)")
elif BMI < 25:
    print(f"Your BMI = {BMI}, Category: Normal range")
elif BMI < 30:
    print(f"Your BMI = {BMI}, Category: Overweight (Pre-obese)")
elif BMI < 35:
    print(f"Your BMI = {BMI}, Category: Obese (Class I)")
elif BMI < 40:
    print(f"Your BMI = {BMI}, Category: Obese (Class II)")
else:
    print(f"Your BMI = {BMI}, Category: Obese (Class III)")

print()



### EXPECTED OUTPUT:
# Enter weight in kilograms: 92
# Enter height in meters: 1.78
# Your BMI = 29.04, Category: Overweight (Pre-obese)