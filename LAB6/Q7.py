print("N\tN^2\tN^3\tSquare Root")

for N in range(1, 16):
    square = N ** 2
    cube = N ** 3
    root = N ** 0.5

    print("%d\t%d\t%d\t%.4f" %
          (N, square, cube, root))