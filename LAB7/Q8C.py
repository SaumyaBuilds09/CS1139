s = input("Enter integers separated by spaces: ")
parts = s.split()

numbers = []
for item in parts:
    numbers += [int(item)]

if len(numbers) == 0:
    print("List is empty")
else:
    smallest = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]

    print("Smallest element:", smallest)