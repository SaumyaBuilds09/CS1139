N = int(input("Enter N: "))

if N < 1:
    print("Invalid input")
else:
    num = 1

    while num <= N:
        temp = num
        digits = 0
        while temp > 0:
            digits += 1
            temp //= 10

        temp = num
        total = 0
        while temp > 0:
            digit = temp % 10
            total += digit ** digits
            temp //= 10

        if total == num:
            print(num, end=" ")

        num += 1

    print()