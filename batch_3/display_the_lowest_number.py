inputted = []

while True:
    numbers = input("Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid Input")
        break
    inputted.append(int(numbers))
    print(min(inputted))