user_text = input("Enter text: ")
suffix_to_check = input("Enter suffix: ")
print(user_text[-len(suffix_to_check):] == suffix_to_check if len(suffix_to_check) <= len(user_text) else False)