a1=int(input("enter the first angle of the triangle"))
a2=int(input("enter the first angle of the triangle"))
a3=int(input("enter the first angle of the triangle"))
if a1<=0 or a2<=0 or a3<=0 or a1+a2+a3!=180:
    print("triangle cannot be formed")
elif a1==90 or a2==90 or a3==90:
    print("right-angled triangle")
elif a1>90 or a2>90 or a3>90:
    print("obtuse-angled triangle")
else:
    print("acute-angled triangle")