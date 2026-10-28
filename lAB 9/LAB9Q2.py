sentence=input()
words=sentence.split()
result=[]
for word in words:
    if len(word)>3:
        result.append(word)
        
print(result)