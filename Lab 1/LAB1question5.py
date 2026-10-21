x=int(input("enter a positive integer"))
y=int(input("enter a positive integer"))
if x<0 or y<0:
    print("Invalid Input")
if y%x==0:
    print("y is divisible by x")
else:
    print("y is not divisible by x")
