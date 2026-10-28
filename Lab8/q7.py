s = input("Enter a string: ")

changes = 0
left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        changes += 1

    left += 1
    right -= 1

print("Changes needed:", changes)