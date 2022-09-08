numbers = []
start = int(input("Pick a start number"))
stop = int(input("pick a stop number"))


for x in range(start, stop):
    print(x)
    numbers.append(x)

print(f"sum is: {sum(numbers)}")