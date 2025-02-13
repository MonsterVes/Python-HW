x = 40  # Academical Hour
y = 60  # Astronomical Hour
z = 20  # Break (per 3 academical hours)
n = 64  # Course lenght in academical hours

course_length_var1 = (((n*x + (n/4)*z))/y)
print(f"Total duration in astronomical hours: {course_length_var1:.2f}")

course_length_var2 = ((4*x+z)*(n/4))/y
print(f"Total duration in astronomical hours: {course_length_var2:.2f}")

