duplicate = []
unique = []
numbers = [input("Enter a Number: ") for i in range(10)]

for n in numbers:
    if n in unique:
        if n not in duplicate:
            duplicate.append(n)
    else:
        unique.append(n)
print(duplicate)