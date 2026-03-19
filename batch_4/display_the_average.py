inputted = []

while True:
    numbers = input("Please enter a number: ")
    if not numbers.isdigit():
        print("Invalid Input")
        break

    inputted.append(int(numbers))
    average = sum(inputted) / len(inputted)
    print("The average is: ", average)