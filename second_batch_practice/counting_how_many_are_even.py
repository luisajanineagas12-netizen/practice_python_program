even_counter = 0

for i in range(10):
    num = int(input(f"Enter number: "))
    if num % 2 == 0:
        even_counter += 1

print(f"Total even numbers: {even_counter}")
