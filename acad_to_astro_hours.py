x = 40  # Academical Hour
y = 60  # Astronomical Hour
z = 20  # Break (per 3 academical hours)
n = 64  # Course lenght in academical hours

course_length_var1 = ((n*x + (n/4)*z))/y
print("Var1: ", course_length_var1)

course_lenght_var2 = ((4*x+z)*(n/4))/y
print("Var2: ", course_lenght_var2)

