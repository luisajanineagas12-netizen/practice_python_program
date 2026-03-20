user_text = input("Enter text: ")
prefix_to_remove = input("Enter prefix: ")
print("Outcome: ", user_text[len(prefix_to_remove):] if user_text.startswith(prefix_to_remove) else user_text)
