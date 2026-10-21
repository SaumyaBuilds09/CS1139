shape=input('Enter the type of shape')
if shape=="square":
    side=float(input())
    area=side*side
    print("area",area)
elif shape=="rectangle":
     length=float(input())
     breadth=float(input())
     area=breadth*length
     print("area",area)
elif shape=="circle":
     radius=float(input())
     area=3.14*radius*radius
elif shape=="triangle":
     base=float(input())
     altitude=float(input())
     area=0.5*base*altitude
     print(area)
else:
    print("Invalid shape")
    