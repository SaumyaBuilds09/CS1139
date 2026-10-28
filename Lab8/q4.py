s = input("Enter a string: ")
ch = input("Enter a character: ")

count = 0
positions = []

for i in range(len(s)):
    if s[i] == ch:
        count += 1
        positions.append(i)

print("Count:", count)

if count == 0:
    print("Positions: -1")
else:
    print("Positions:", *positions)