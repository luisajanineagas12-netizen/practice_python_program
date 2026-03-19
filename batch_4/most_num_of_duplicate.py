inputted = []

while True:
    numbers = input("Please enter a number: ")
    if numbers.isdigit():
        print("Invalid Input")
        break

    inputted.append(int(numbers))
    highest_duplicate = max(set(inputted), key=inputted.count)
    print(highest_duplicate)