user_text = input("Enter text: ")
prefix_to_check = input("Enter prefix: ")
print(user_text[:len(prefix_to_check)] == prefix_to_check)
