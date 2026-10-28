s = input("Enter a string: ")

i = 0
j = len(s) - 1
palindrome = True

while i < j:
    if s[i] != s[j]:
        palindrome = False
        break

    i += 1
    j -= 1

if palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")