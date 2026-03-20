user_text = input("Enter text: ")
substring_to_find = input("Enter substring: ")
found_position = -1
for position in range(len(user_text) - len(substring_to_find), -1, -1):
    if user_text[position:position+len(substring_to_find)] == substring_to_find:
        found_position = position
        break
print(found_position if found_position != -1 else "Not found")
