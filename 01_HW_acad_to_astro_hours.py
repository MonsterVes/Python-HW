x = academic_hour = 40
y = astronomical_hour = 60
z = break_duration = 20         # Break (per 3 academical hours)
n = course_legnt_in_acad_hours = 64

# round(x,2) is showing only the first digit after the floating point, when the second one is 0
course_length_astronomical_hours_var1 = (((n*x + (n/4)*z))/y)
print(f"Total duration in astronomical hours: {course_length_astronomical_hours_var1:.2f}") 

course_length_astronomical_hours_var2 = ((4*x+z)*(n/4))/y
print(f"Total duration in astronomical hours: {course_length_astronomical_hours_var2:.2f}") 

