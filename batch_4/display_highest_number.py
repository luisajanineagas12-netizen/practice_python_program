inputted = []

while True:
    numbers = input("Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid Input")
        break
    inputted.append(int(numbers))

if inputted:
    highest_number = max(set(inputted))
    print(highest_number)