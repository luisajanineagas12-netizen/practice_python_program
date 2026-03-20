fullname = input("Enter your full name in incorrect casing: ")

words = fullname.split()
snake_case = ""

for i in range(len(words)):
    word = words[i].lower()
    if i > 0:
        snake_case += "_"
    snake_case += word

print(snake_case)