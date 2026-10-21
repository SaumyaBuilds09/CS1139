radius=int(input("enter the radius of the circle between 0-100"))
if radius>100 or radius<0:
    print("invalid input")
else:   
    area=radius*radius*3.14
    print("area", area)
    
