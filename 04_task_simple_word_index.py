text = """apple and banana one apple one banana a red apple and a green apple"""

# Convert text to list
text_to_list = text.split(" ")

# Conver list to dict
word_count = {k:text_to_list.count(k) for k in text_to_list}

# Print key-value pairs
for key, value in word_count.items():
    print(f"{key} - {value}")


