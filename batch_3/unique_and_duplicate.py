inputted = []

while True:
    numbers = input("Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid Input")
        break
    if numbers in inputted:
        print("Duplicate")
    else:
        print("Unique")
        inputted.append(numbers)