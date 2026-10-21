n = int(input("Enter a 4-digit number: "))
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n  % 10


first_sum = a+b
last_sum = c+d
print("Sum of first two digits:", first_sum)
print("Sum of last two digits:", last_sum)
if first_sum == last_sum:
    print("The two sums are equal.")
else:
    print("The two sums are not equal.")
