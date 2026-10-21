n = int(input("Enter a 3-digit number: "))

a = n // 100
b = (n // 10) % 10
c = n % 10

sum_digits = a + b + c

if n % sum_digits == 0:
    print(n, "is a Harshad number")
else:
    print(n, "is not a Harshad number")