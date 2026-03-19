numbers = []

for num in range(0, 101):
    if '0' not in str(num):
        numbers.append(num)

print(numbers)
