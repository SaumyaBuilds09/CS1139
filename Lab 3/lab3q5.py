 n = int(input("Enter a 5-digit number: "))
a = n // 10000
b = (n // 1000) % 10
c = (n // 100) % 10
d = (n // 10) % 10
e = n % 10

# Assume the first digit is the largest
largest = a
position = 1
# Compare with the second digit
if b > largest:
        largest = b
        position = 2

# Compare with the third digit
if c > largest:
    largest = c
    position = 3

# Compare with the fourth digit
if d > largest:
    largest = d
    position = 4

# Compare with the fifth digit
if e > largest:
    largest = e
    position = 5
print("Largest digit:", largest)
print("Position from left:", position)
