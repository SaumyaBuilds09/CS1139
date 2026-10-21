c=input("enter colour: Blue or Red")
m=input("Enter mode: Steady or flashing")
if c=='blue' and m=='steady':
    print("steady blue,Clear view")
elif c=='blue' and m=='flashing':
    print("Flashing blue,clouds due")
elif c=='red' and m=='steady':
    print("steady red,rain ahead")
else:
    print("Flashing red,snow instead")