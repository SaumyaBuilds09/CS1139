print("              Addition Table")
print("     ", end="")
for i in range(1, 10):
    print("%4d" % i, end="")
print()
print("     " + "-" * 37)

for i in range(1, 10):
    print("%3d |" % i, end="")
    for j in range(1, 10):
        print("%4d" % (i + j), end="")
    print()