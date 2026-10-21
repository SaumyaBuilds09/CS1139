x1=int(input("enter the x1 coordinate"))
y1=int(input("enter the y1 coordinate"))
r=int(input("Enter the radius of the circle"))
x2=int(input("enter the x2 coordinate"))
y2=int(input("enter the y2 coordinate"))
distance=((x2-x1)**2+(y2-y1)**2)**0.5
if distance<r:
    print("the point lies inside the circle")
elif distance==r:
    print("the point lies on the boundary of the circle")
else:
    print("the point lies outside of the circle")