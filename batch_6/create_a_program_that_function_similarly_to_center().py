user_text = input("Enter text: ")
desired_width = int(input("Enter width: "))
spaces_needed = desired_width - len(user_text)
print(" " * (spaces_needed // 2) + user_text + " " * (spaces_needed - spaces_needed // 2) if spaces_needed > 0 else user_text)