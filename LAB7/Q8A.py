s = input("Enter integers separated by spaces: ")
parts = s.split()

numbers = []
for item in parts:
    numbers += [int(item)]

total = 0

for i in range(len(numbers)):
    total += numbers[i]

print("Sum:", total)