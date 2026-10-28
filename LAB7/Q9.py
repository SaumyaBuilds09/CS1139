s = input("Enter integers separated by spaces: ")
parts = s.split()

numbers = []
for item in parts:
    numbers += [int(item)]

n = len(numbers)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] < numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Descending order:", numbers)