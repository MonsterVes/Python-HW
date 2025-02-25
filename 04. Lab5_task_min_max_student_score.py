students_score = {
    "Ivan":5.00,
    "Alex":3.50,
    "Maria":5.50,
    "Georgy":5.00,
}

print(f"{max(students_score,  key = students_score.get)} - {max(students_score.values())}")
print(f"{min(students_score,  key = students_score.get)} - {min(students_score.values())}")