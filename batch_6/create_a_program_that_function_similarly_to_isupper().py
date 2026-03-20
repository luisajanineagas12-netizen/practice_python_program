text = input("Enter text: ")
print(all(not("a" <= character <= "z") for character in text))