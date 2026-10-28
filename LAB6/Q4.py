N = int(input("Enter a positive integer: "))

if N <= 0:
    print("Invalid input")
else:
    num = N
    octal = ""

    while num > 0:
        remainder = num % 8
        octal = str(remainder) + octal
        num = num // 8
    print("Octal equivalent:", octal)
    if octal == oct(N)[2:]:
        print("Result matches oct()")
    else:
        print("Result does not match oct()")