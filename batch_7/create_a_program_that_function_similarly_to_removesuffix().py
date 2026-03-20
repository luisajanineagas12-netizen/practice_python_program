user_text = input("Enter text: ")
suffix_to_remove = input("Enter suffix: ")
print(user_text[:-len(suffix_to_remove)] if user_text.endswith(suffix_to_remove) else user_text)
