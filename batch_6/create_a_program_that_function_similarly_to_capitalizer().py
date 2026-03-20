text = input("Enter a sentence: ")
print((chr(ord(text[0]) - 32) if "a" <= text[0] <= "z" else text[0]) +
      "".join(chr(ord(character) + 32) if "A" <= character <= "Z" else character for character in text[1:]) if text else "")