n = int(input("Enter an integer: "))
if n < 2:
    print("Invalid input")
else:
    i = 2
    prime = True

    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i = i + 1

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")
