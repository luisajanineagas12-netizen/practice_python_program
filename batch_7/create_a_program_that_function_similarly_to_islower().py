user_text = input("Enter text: ")
print(all(not("A" <= character <= "Z") for character in user_text))

