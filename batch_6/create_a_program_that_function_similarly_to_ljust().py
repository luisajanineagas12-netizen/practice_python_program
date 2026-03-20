text = input("Enter text: ")
desired_width = int(input("Enter width: "))
print(text + "*" * (desired_width - len(text)) if len(text) < desired_width else text)