numbers = [int(input("Enter a Number: "))for i in range(10)]

unique = [num for num in numbers if numbers.count(num) ==1]
print(unique)
