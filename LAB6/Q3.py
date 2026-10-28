N = int(input("Enter number of lines: "))
if N <= 0:
    print("Invalid input")
else:
    print("Pattern A:")
    i = 1
    while i <= N:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        print()
        i += 1
    print("\nPattern B:")
    i = 1
    while i <= N:
        j = N
        while j >= i:
            print("*", end=" ")
            j -= 1
        print()
        i += 1
    print("\nPattern C:")
    i = 1
    while i <= N:
        j = 1
        while j <= i:
            print("*", end=" ")
            j += 1
        print()
        i += 1