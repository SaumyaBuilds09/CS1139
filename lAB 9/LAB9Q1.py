numbers=list(map(int,input("enter").split()))
even=[]
odd=[]
for n in numbers:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
        
print("even",even)
print("odd",odd)