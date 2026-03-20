user_text = input("Enter text: ")
substring_to_count = input("Enter substring: ")
count_occurrences = 0
for position in range(len(user_text) - len(substring_to_count) + 1):
    if user_text[position:position+len(substring_to_count)] == substring_to_count:
        count_occurrences += 1
print(count_occurrences)
