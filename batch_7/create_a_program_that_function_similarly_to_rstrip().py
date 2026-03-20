user_text = input("Enter text: ")
position_in_text = len(user_text) - 1
while position_in_text >= 0 and user_text[position_in_text] == " ":
    position_in_text -= 1
print(user_text[:position_in_text+1])
