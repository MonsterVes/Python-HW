x = 40  # Academical Hour
y = 60  # Astronomical Hour
z = 15  # Break (per 3 academical hours)
n = 64  # Course lenght in academical hours

course_length_var1 = ((n*x + (n/3)*z)-z)/y
print("Var1: ", course_length_var1)

course_lenght_var2 = ((3*x+z)*(n/3)-z)/y
print("Var2: ", course_lenght_var2)