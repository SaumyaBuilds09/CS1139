s = input("Enter integers separated by spaces: ")
parts = s.split()

numbers = []
for item in parts:
    numbers += [int(item)]

product = 1

for i in range(len(numbers)):
    product *= numbers[i]

print("Product:", product)