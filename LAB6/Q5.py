N = int(input("Enter number of students: "))
if N < 2 or N > 100:
    print("Invalid number of students")
else:
    first = int(input("Enter distance: "))
    second = 0

    if first <= 0:
        print("Invalid distance")
    else:
        valid = True
        i = 1

        while i < N:
            distance = int(input("Enter distance: "))

            if distance <= 0:
                valid = False
            else:
                if distance > first:
                    second = first
                    first = distance
                elif distance < first and distance > second:
                    second = distance

            i += 1

        if not valid:
            print("Invalid distance")
        elif second == 0:
            print("At least two different distances are required")
        else:
            print(first)
            print(second)