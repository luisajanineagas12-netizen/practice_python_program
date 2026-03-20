inputted = []

while True:
    numbers = input("Please enter a number: ")
    if not numbers.isdigit():
        print("Invalid Input")
        break
    inputted.append(int(numbers))

if inputted:
    highest_duplicate = max(set(inputted), key=inputted.count)
    print("The number with highest duplicate: ", highest_duplicate)