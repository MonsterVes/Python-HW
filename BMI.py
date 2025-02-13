w = weight_in_kg = 57           # Weight in kilograms
h = height_in_meters = 1.68     # Height in meters

# round(x,2) is showing only the first digit after the floating point, when the second one is 0
body_mass_index = round((w/(h*h)),2)
print(f"BMI: {body_mass_index:.2f}") 