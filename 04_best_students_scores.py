students_score = {
    "Ivan":5.00,
    "Alex":3.50,
    "Maria":5.50,
    "Georgy":5.00,
}

best_students_scores = {}


for key, value in students_score.items(): 
    if value > 4:
        best_students_scores[key] = value
        print(f"{key:<10} - {value}")






