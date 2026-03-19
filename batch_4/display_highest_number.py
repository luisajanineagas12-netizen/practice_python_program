inputted = []

while True:
    numbers = input("Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid Input")
        break

    inputted.append(int(numbers))
    highest_number = max(set(inputted))
    print(highest_number)