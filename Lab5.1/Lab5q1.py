X = int(input("Enter the first number"))
Y = int(input("Enter the second number"))
N = int(input("Enter the divisor"))
for i in range(X+1,Y+1):
    if i%N==0:
        print(i)
