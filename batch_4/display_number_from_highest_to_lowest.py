inputted = []

while True:
    numbers = input("Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid Input")
        break

    inputted.append(int(numbers))
    inputted.sort(reverse=True)
    no_duplicate = list(dict.fromkeys(inputted))
    print(no_duplicate)