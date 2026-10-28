N = int(input("Enter N: "))

if N <= 0:
    print("Invalid input")
else:
    number = 1

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(number, end=" ")
            number += 1
        print()