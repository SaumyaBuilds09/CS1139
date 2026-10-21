
n = int(input("Enter the number of terms: "))
a = 1
b = 1
i = 1
if n <= 0:
    print("Invalid input")
else:
    while i <= n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        i = i + 1
