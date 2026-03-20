user_text = input("Enter text: ")
print("".join(chr(ord(character) + 32) if "A" <= character <= "Z" else character for character in user_text))