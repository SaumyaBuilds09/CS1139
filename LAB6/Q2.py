N = int(input("Enter N: "))
if N < 1 or N > 1000:
    print("Invalid input")
else:
    slot = 1
    while slot <= 1000:
        if slot % N != 0 or slot % 4 == 0:
            slot += 1
            continue

        print(slot, end=" ")
        slot += 1
    print()