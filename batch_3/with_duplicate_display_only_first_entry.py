numbers = [int(input("Enter a Number: "))for i in range(10)]

order_by_insertion = list(dict.fromkeys(numbers))
print(order_by_insertion)