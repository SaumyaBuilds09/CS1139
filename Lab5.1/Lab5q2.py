n = int(input("Enter a positive integer: "))
total = 0
while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10
print("Sum of digits =", total)
