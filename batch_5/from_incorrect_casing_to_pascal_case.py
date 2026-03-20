fullname = input("Enter your full name in incorrect casing: ")

words = fullname.split()
pascal_case = ""

for word in words:
    pascal_case += word.capitalize()

print(pascal_case)