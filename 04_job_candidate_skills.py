required_skills = {'Python', 'Django', 'SQL', 'Git'}
candidate_skills = {'Python', 'Flask', 'Git', 'JavaScript'}

matched_skills = required_skills.intersection(candidate_skills)
missing_skills = required_skills - candidate_skills
extra_skills = candidate_skills - required_skills

print(f"Matched Skills: {", ".join(matched_skills)}")
print(f"Missing Skills: {", ".join(missing_skills)}")
print(f"Extra Skills: {", ".join(extra_skills)}")

