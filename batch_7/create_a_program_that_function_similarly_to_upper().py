user_text = input("Enter text: ")
print("".join(chr(ord(character) - 32) if "a" <= character <= "z" else character for character in user_text))
