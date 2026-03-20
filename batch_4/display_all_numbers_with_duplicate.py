duplicate = []

numbers = [input("Enter a Number: ") for i in range(10)]

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicate:
        duplicate.append(num)
print("The numbers with duplicates are: ", duplicate)