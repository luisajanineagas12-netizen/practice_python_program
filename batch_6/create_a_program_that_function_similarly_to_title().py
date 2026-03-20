user_text = input("Enter text: ")
print(" ".join((chr(ord(word[0]) - 32) if "a" <= word[0] <= "z" else word[0]) +
               "".join(chr(ord(character) + 32) if "A" <= character <= "Z" else character for character in word[1:])
               for word in user_text.split()))