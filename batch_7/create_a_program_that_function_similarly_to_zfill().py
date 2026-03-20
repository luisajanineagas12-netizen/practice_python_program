user_text = input("Enter text: ")
desired_width = int(input("Enter width: "))
print("0" * (desired_width - len(user_text)) + user_text if len(user_text) < desired_width else user_text)
