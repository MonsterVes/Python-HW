from datetime import datetime, date, timedelta

# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Create a function (format_current_date) that returns the current date and time in the format "YYYY-MM-DD HH:MM:SS".
"""

### YOUR CODE HERE:

# def format_current_date():
#         return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# print(format_current_date())

### TEST:
# print(format_current_date())

### EXPECTED OUTPUT:
# Output will vary depending on when the function is called. Example: "2024-02-11 22:34:56"


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Write a function (days_between) that calculates the number of days between two dates given in the format "YYYY-MM-DD".
"""

### YOUR CODE HERE:

# def days_between(first_date, second_date):
#     format_first_date = datetime.strptime(first_date, "%Y-%m-%d")
#     format_second_date = datetime.strptime(second_date, "%Y-%m-%d")
#     return abs((datetime.date(format_first_date)-datetime.date(format_second_date)).days)

# print(days_between("2024-01-01", "2024-02-01"))

### TEST:
# print(days_between("2024-01-01", "2024-02-01"))

### EXPECTED OUTPUT:
# 31


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Write a function (get_weekday) that takes a date in the format "YYYY-MM-DD" and returns the name of the day of the week.
"""

### YOUR CODE HERE:

# def get_weekday(date_to_convert):
#     date_formatting = datetime.strptime(date_to_convert, "%Y-%m-%d")
#     return date_formatting.strftime("%A")

# print(get_weekday("2024-02-11"))

### TEST:
# print(get_weekday("2024-02-11"))

### EXPECTED OUTPUT:
# "Sunday"


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Write a function (calc_days_untill_birthdate), that calculates the remaining days from current date to your next birthday day.
"""

### YOUR CODE HERE:

# def calc_days_until_birthdate(birthdate):
#     format_birthday = datetime.strptime(birthdate, "%d.%m.%Y")
#     this_year_bd = format_birthday.replace(year = datetime.today().year)
#     if this_year_bd > datetime.today():
#         return (this_year_bd - datetime.today()).days
#     else:
#         next_year_bd = this_year_bd.replace(year = datetime.today().year +1)
#         return (next_year_bd - datetime.today()).days
    
# birthdate = "08.04.2025"
# print(f"Days until next birthday: {calc_days_until_birthdate(birthdate)}")

### TEST:
# birthdate = "25.02.1990" # 25th February 1990
# print(f"Days until next birthday: {calc_days_until_birthdate(birthdate)}")


### EXPECTED OUTPUT:
# if today date is "15.02.2024", the output should be:
# Days until next birthday: 9