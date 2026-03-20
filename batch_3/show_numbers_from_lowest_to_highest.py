inputted = []

while True:
    numbers = input("Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid Input")
        break
    inputted.append(int(numbers))

if inputted:
    inputted.sort()
    no_duplicate =  list(dict.fromkeys(inputted))
    print("The inputted numbers are: ", no_duplicate)