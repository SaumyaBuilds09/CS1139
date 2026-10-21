a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))

a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

# Check for invalid equations
if a1 == 0 and b1 == 0:
    print("Invalid first line")
elif a2 == 0 and b2 == 0:
    print("Invalid second line")

else:
    # Determinant
    D = a1 * b2 - a2 * b1

    if D == 0:
        # Check whether lines are coincident
        if a1 * b2 == a2 * b1 and a1 * c2 == a2 * c1:
            print("The lines are coincident")
        else:
            print("The lines are parallel")

    else:
        # Cramer's Rule
        x = (c1 * b2 - c2 * b1) / D
        y = (a1 * c2 - a2 * c1) / D

        print(f"Point of intersection: ({x:.2f}, {y:.2f})")
        